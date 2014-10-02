from django import forms

FEATURE_TYPE = [("building", "Building"),
                ("river", "River"),
                ("road", "Road"),
                ("landuse", "Land Use"),
                ("boundary", "Administrative Boundary"),
                ("center", "Administrative Center")]

class ImportShapefileForm(forms.Form):
    import_file = forms.FileField(label="Select a Zipped Shapefile")
    feature_type = forms.ChoiceField(choices=FEATURE_TYPE, initial="building")
