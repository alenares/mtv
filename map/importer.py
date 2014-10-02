import os, os.path, tempfile, zipfile
import shutil, traceback
from django.contrib.gis.utils import LayerMapping
from utils import MAPPING_FEATURES
from models import Building, LandUse, River, Road, AdministrativeBoundary, AdministrativeCenter

FEATURES = { 'building' : Building,
             'landuse'  : LandUse,
             'road'     : Road,
             'river'    : River,
             'boundary' : AdministrativeBoundary,
             'center'   : AdministrativeCenter
}

def import_data(shapefile, feature_type):
    fd,fname = tempfile.mkstemp(suffix=".zip")
    os.close(fd)
    f = open(fname, "wb")
    for chunk in shapefile.chunks():
        f.write(chunk)
    f.close()
    if not zipfile.is_zipfile(fname):
        os.remove(fname)
        return "Not a valid zip archive!"
    
    zip = zipfile.ZipFile(fname)

    required_suffixes = [".shp", ".shx", ".dbf", ".prj"]
    has_suffix = {}
    for suffix in required_suffixes:
        has_suffix[suffix] = False
    
    for info in zip.infolist():
        extension = os.path.splitext(info.filename)[1].lower()
        if extension in required_suffixes:
            has_suffix[extension] = True

    for suffix in required_suffixes:
        if not has_suffix[suffix]:
            zip.close()
            os.remove(fname)
            return "Archive missing required "+suffix+" file!"
    
    shapefile_name = None
    dst_dir = tempfile.mkdtemp()
    for info in zip.infolist():
        if info.filename.endswith(".shp"):
            shapefile_name = info.filename
        dst_file = os.path.join(dst_dir, info.filename)
        f = open(dst_file, "wb")
        f.write(zip.read(info.filename))
        f.close()
    zip.close()
    
    try:
        lm = LayerMapping(  FEATURES[feature_type], 
                            os.path.join(dst_dir,shapefile_name), 
                            MAPPING_FEATURES[feature_type])
        lm.save()
        os.remove(fname)
        shutil.rmtree(dst_dir)
        return
    except:
        traceback.print_exc()
        os.remove(fname)
        shutil.rmtree(dst_dir)
        return "Not a valid shapefile!"
    
    
    
    
    
