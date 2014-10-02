var map;
var osmUrl='http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
var osmAttrib='Map data © OpenStreetMap contributors';
var control_layers;
var layerList=[];
var initVillage = "murole"
var villages = {
    "murole" : [-1.053, 29.616],
    "rushabarara" : [-1.11735, 29.63153],
    "nanga" : [0.5145, 32.0951],
    "kanyamahene" : [-1.1264, 29.71872],
    "kagezi" : [-1.1623, 29.61893],
    "bitongo" : [-1.32311, 29.64933],
    "ssanga" : [0.43486, 33.05999],
    "kanga" : [0.191594, 32.960642],
};
var layers = [
    "boundary",
    "landuse",
    "river",
    "road",
    "building"
]

var colormap = {
    "hospital":"#CC3399",
    "community centre":"#CC6633",
    "house":"#CCB333",
    "school":"#99CC33",
    "retail":"#D864B1",
    "commercial":"#006600",
    "river":"#CC3399",
    "road":"#C2C2C2",
    "crop":"#663300",
    "cleared":"#BDBD9D",
    "trees":"#00cc33"
};

function initmap() {
        // set up the map
        map = new L.Map('map');
    
        // create the tile layer with correct attribution
        var osm = new L.TileLayer(osmUrl, {minZoom: 8, maxZoom: 18, attribution: osmAttrib});		
        map.addLayer(osm);
        
        var baseMaps = {
            "Map": osm
        };

        control_layers = L.control.layers(baseMaps).addTo(map);
        L.control.scale().addTo(map); 
        setmap(initVillage);
}

function setmap(village) {
        var coord = villages[village];
        // set the new coordinates
        map.setView(coord, 14);
        for (index = 0; index < layerList.length; ++index) {
            map.removeLayer(layerList[index]);
            control_layers.removeLayer(layerList[index]);                   
        }
        layerList=[]
        getLayers(village);
}
        
function onEachFeature(feature, layer) {
    // does this feature have a property named Name?
    if (feature.properties && feature.properties.Name) {
        layer.bindPopup(feature.properties.Name);
    }
    if (feature.properties && feature.properties.category && feature.geometry.type){
        if(feature.geometry.type == "Point"){
            // default color
            var color = "#334DCC";
            var t = feature.properties.category;
            color = colormap[t] || color;
            layer.setStyle({
                "fillColor": color,
                "color": "#000",
                "weight": 2,
                "radius": 4,
                "opacity": 1,
                "fillOpacity": 1
            });
        }
        
        if(feature.geometry.type == "LineString"){
            // default color
            var color = "#334DCC";
            var t = feature.properties.category;
            color = colormap[t] || color;
            layer.setStyle({
                "color": color,
                "weight": 3,
                "opacity": 1,
                "fillOpacity": 0.8
            });
        }
        if(feature.geometry.type == "Polygon"){
            // default color
            var color = "#334DCC";
            var t = feature.properties.category;
            color = colormap[t] || color;
            layer.setStyle({
                "fillColor": color,
                "color": "#000",
                "weight": 2,
                "opacity": 1,
                "fillOpacity": 0.7
            });
        }
    }
}
        
function getLayers(village) {
    for(i = 0; i < layers.length; ++i) {
        getData(village, layers[i]); 
    }
}

function getData(village, layer) {
    $.getJSON( '/data/'+village +'/'+layer, function(response_data){
        mapLayer = L.geoJson(response_data, {
            pointToLayer: function (feature, latlng) {
                //alert(dblayer)
                return L.circleMarker(latlng, {});
            },
            onEachFeature: onEachFeature
        }).addTo(map);
        if(layer == "landuse" || layer == "boundary")
            mapLayer.bringToBack();
        if(layer == "building")
            mapLayer.bringToFront();
        control_layers.addOverlay(mapLayer, layer);
        layerList.push(mapLayer);
    });
}
