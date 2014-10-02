MAPPING_FEATURES = {'center' :
                    {'admin_unit' :
                        {'name' : 'Admin_unit'},
                    'remarks' : 'Remarks',
                    'geometry' : 'POINT' # For geometry fields use OGC name.
                    },
                    'boundary' :
                    {'admin_unit' : 
                        {'name' : 'Admin_unit'},
                    'remarks' : 'Remarks',
                    'geometry' : 'POLYGON'
                    },
                'building' :
                    {'name' : 'Name', 
                    'category' : 'Category',
                    'admin_unit' : 
                        {'name' : 'Admin_unit'},
                    'remarks' : 'Remarks',
                    'geometry' : 'POINT'
                    },
                'river' :
                    {'name' : 'Name',
                    'admin_unit' : 
                        {'name' : 'Admin_unit'},
                    'remarks' : 'Remarks',
                    'geometry' : 'LINESTRING'
                    },
                'road' :
                    {'name' : 'Name', 
                    'admin_unit' : 
                        {'name' : 'Admin_unit'},
                    'remarks' : 'Remarks',
                    'geometry' : 'LINESTRING'
                    },
                'landuse' :
                    {'name' : 'Name', 
                    'category' : 'Category',
                    'admin_unit' : 
                        {'name' : 'Admin_unit'},
                    'remarks' : 'Remarks',
                    'geometry' : 'POLYGON'
                    }                
}

BUILDING_CATEGORIES = (
        ('house', 'House'),
        ('community_center', 'Community Center'),
        ('school', 'School'),
        ('facility', 'Facility'),
        ('other', 'Other building'),
)
    
LANDUSE_CATEGORIES = (
        ('crop', 'Crop'),
        ('trees', 'Tree'),
        ('cleared', 'Cleared land'),
        ('other', 'Other land'),
)

ADMINISTRATIVE_CATEGORIES = (
        ('village', 'Village'),
        ('county', 'County'),
        ('other', 'Other'),
)


