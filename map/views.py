from django.shortcuts import render, redirect
from django.http import HttpResponse
from forms import ImportShapefileForm
from importer import import_data
import json
from models import Building, LandUse, River, Road, AdministrativeBoundary, AdministrativeCenter
from djgeojson.serializers import Serializer as GeoJSONSerializer

MODELS_LIST = {'building'  : Building,
               'landuse'   : LandUse,
               'river'     : River,
               'road'      : Road,
               'boundary'  : AdministrativeBoundary,
               'center'    : AdministrativeCenter
}

def index(request):
    template_name = 'index.html'
    form = ImportShapefileForm()
    context = {'form' : form, 'err_msg' : None}
    return render(request, template_name, context)

def import_shapefile(request):
    template_name = 'index.html'
    
    if request.method == 'POST':
        form = ImportShapefileForm( request.POST,
                                    request.FILES)
        if form.is_valid():
            shapefile = request.FILES['import_file']
            feature_type = request.POST['feature_type']
            
            err_msg = import_data(shapefile, feature_type)
        else:
            err_msg = "Please review the Upload form!"
        
        context = {'form' : form, 'err_msg' : err_msg}
        return render(request, template_name, context)

def feature_data(request, village_name, feature_type):
    response = MODELS_LIST[feature_type].objects.filter(admin_unit__name = village_name)
    json_response = GeoJSONSerializer().serialize(response, 
                                                  use_natural_keys=True,
                                                  geometry_field="geometry")
    return HttpResponse(json_response, content_type="application/json")

def village_layers(request, village_name):
    response = []
    queryset = Building.objects.filter(village__name = village_name)
    for village_layer in queryset:
        response.append([village_layer.layer])
    return HttpResponse(json.dumps(response))
