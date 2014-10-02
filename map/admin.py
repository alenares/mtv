from django.contrib.gis import admin
from models import Building, LandUse, River, Road, AdministrativeBoundary, AdministrativeCenter, AdministrativeUnit

class BuildingAdmin(admin.GeoModelAdmin):
    list_display = ('name', 'category', 'admin_unit')
    list_filter = ('category', 'admin_unit__name')

class LandUseAdmin(admin.GeoModelAdmin):
    list_display = ('name', 'category', 'admin_unit')
    list_filter = ('category', 'admin_unit__name')

class RiverAdmin(admin.GeoModelAdmin):
    list_display = ('name','admin_unit')
    list_filter = ('admin_unit__name',)

class RoadAdmin(admin.GeoModelAdmin):
    list_display = ('name','admin_unit')
    list_filter = ('admin_unit__name',)
    
admin.site.register(AdministrativeUnit, admin.GeoModelAdmin)
admin.site.register(AdministrativeBoundary, admin.GeoModelAdmin)
admin.site.register(AdministrativeCenter, admin.GeoModelAdmin)
admin.site.register(Building, BuildingAdmin)
admin.site.register(LandUse, LandUseAdmin)
admin.site.register(River, RiverAdmin)
admin.site.register(Road, RoadAdmin)
