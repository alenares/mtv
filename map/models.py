from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from utils import LANDUSE_CATEGORIES, BUILDING_CATEGORIES, ADMINISTRATIVE_CATEGORIES

        
class AdministrativeUnit(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    display = models.CharField(max_length=50)
    category = models.CharField(max_length=20, choices=ADMINISTRATIVE_CATEGORIES)
    admin_unit = models.ForeignKey('self', blank=True, null=True)
    remarks = models.TextField(blank = True)
    
    def __unicode__(self):
            return self.display

class AdministrativeBoundary(models.Model):
    admin_unit = models.ForeignKey(AdministrativeUnit)
    remarks = models.TextField(blank = True)
    
    # GeoDjango-specific: a geometry field (PolygonField), and
    # overriding the default manager with a GeoManager instance.
    geometry = models.PolygonField()
    objects = models.GeoManager()
    
    def __unicode__(self):
        return "Boundary of %s" % (self.admin_unit.display) 

class AdministrativeCenter(models.Model):
    admin_unit = models.ForeignKey(AdministrativeUnit)
    remarks = models.TextField(blank = True)
    lon = models.FloatField(blank = True)
    lat = models.FloatField(blank = True)
    
    geometry = models.PointField(blank = True)
    objects = models.GeoManager()
    
    def __unicode__(self):
        return "Center of %s" % (self.admin_unit.display)  

    def save(self, *args, **kwargs):
        if self.lon == None or self.lat == None:
            if self.geometry == None:
                self.lon = 0.0
                self.lat = 0.0
                self.geometry = Point(0.0, 0.0)
            else:
                self.lon = self.geometry.coords[0]
                self.lat = self.geometry.coords[1]
        elif self.geometry == None:
            self.geometry = Point(self.lon, self.lat)
        super(AdministrativeCenter, self).save(*args, **kwargs) # Call the "real" save() method.
   

class Building(models.Model):
    name = models.CharField(max_length=50, blank = True)
    category = models.CharField(max_length=20, choices=BUILDING_CATEGORIES)
    admin_unit = models.ForeignKey(AdministrativeUnit)
    remarks = models.TextField(blank = True)
    lon = models.FloatField(blank = True)
    lat = models.FloatField(blank = True)
    
    geometry = models.PointField(blank = True)
    objects = models.GeoManager()
    
    def __unicode__(self):
        if self.name is not None:
            return self.name
        else:
            return "%s in %s" % (self.category, self.admin_unit.display)  

    def save(self, *args, **kwargs):
        if self.lon == None or self.lat == None:
            if self.geometry == None:
                self.lon = 0.0
                self.lat = 0.0
                self.geometry = Point(0.0, 0.0)
            else:
                self.lon = self.geometry.coords[0]
                self.lat = self.geometry.coords[1]
        elif self.geometry == None:
            self.geometry = Point(self.lon, self.lat)
        super(Building, self).save(*args, **kwargs) # Call the "real" save() method.
    
class LandUse(models.Model):
    name = models.CharField(max_length=50, blank = True)
    category = models.CharField(max_length=20, choices=LANDUSE_CATEGORIES)
    admin_unit = models.ForeignKey(AdministrativeUnit)
    remarks = models.TextField(blank = True)

    geometry = models.PolygonField()
    objects = models.GeoManager()
    
    def __unicode__(self):
        if self.name is not None:
            return self.name
        else:
            return "%s in %s" % (self.category, self.admin_unit.display)     

class River(models.Model):
    name = models.CharField(max_length=50, blank = True)
    admin_unit = models.ForeignKey(AdministrativeUnit)
    remarks = models.TextField(blank = True)

    geometry = models.LineStringField()
    objects = models.GeoManager()
    
    def __unicode__(self):
        if self.name is not None:
            return self.name
        else:
            return "river in %s" % ( self.admin_unit.display)     

class Road(models.Model):
    name = models.CharField(max_length=50, blank = True)
    admin_unit = models.ForeignKey(AdministrativeUnit)
    remarks = models.TextField(blank = True)

    geometry = models.LineStringField()
    objects = models.GeoManager()
    
    def __unicode__(self):
        if self.name is not None:
            return self.name
        else:
            return "road in %s" % ( self.admin_unit.display)     


