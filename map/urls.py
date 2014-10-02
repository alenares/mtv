from django.conf.urls import patterns, include, url
from django.contrib import admin
from djgeojson.views import GeoJSONLayerView
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'map.views.index', name='index'),
    url(r'^import$', 
        'map.views.import_shapefile', name='import_shapefile'),
    url(r'^data/(?P<village_name>[-\w]+)/(?P<feature_type>[-\w]+)$',
        'map.views.feature_data', name='feature_data'),
    #url(r'^data/(?P<village_name>[-\w]+)$', 'map.views.village_layers',
    #    name='village_layers'),
    # url(r'^map/', include('map.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
