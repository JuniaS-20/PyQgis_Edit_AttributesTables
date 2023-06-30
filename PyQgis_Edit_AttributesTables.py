"""
By Junior Muyumba 
2022/03/07 Montpellier.
You can reuse and redsitribute data and this code 
-------------------------------------------------------------
For more compréhension, read the Readme doc.

"""

## --------- This Part must not be commented it call the project ---------
from qgis.core import QgsProject
from qgis.core import *
from processing.core.Processing import Processing
Processing.initialize()
from processing.tools import *
layers = QgsProject.instance().mapLayers().values()
#print(layer.name())

## --------- -----------------------------------------
    

"""
In the exemple (1)we whish to have for all sations, the fields named as below:
-------------------------------------------------------------------------------------------------------------------
|NUM_SATIO |   PAYS    |  BASSIN  |   RIVIERE  |  NOM_SATIO |   LATITUDE | LONGITUDE |   SUPERFICIE |   DEBUT_OBS |          
-------------------------------------------------------------------------------------------------------------------

In the pert (2), we wish to add more infos from the station to the sub-watershed's table below
---------------------------------------------------
|    NOM    |   PAYS    |    KM2    |   EXUTOIRE  |           
---------------------------------------------------
part (3) we whish to delete some fields from attribute table.

!!!!! Before exécuting à part, comment others first and remove from the project layers not concerned by the task.

"""


######################################################################################################################♥
"""-----------------------------
1. RENAME FIELDS 
---------------------------------"""

for layer in layers:
#    print(layer.name())
    layer.startEditing()
        # Rename field ---------***
    for field in layer.fields():
        
        if field.name() == 'RIVIèrE'or field.name() == 'RIVIÞrE' or field.name() == 'Rivière':
            idx = layer.fields().indexFromName(field.name())
            layer.renameAttribute(idx, 'RIVIERE')
        elif field.name() == 'Nom_bassin'or field.name() == 'Nom_Bassin' or field.name() == 'NOM_BASSIN':
            idx = layer.fields().indexFromName(field.name())
            layer.renameAttribute(idx, 'BASSIN')
        elif field.name() == 'Bassin':
            idx = layer.fields().indexFromName(field.name())
            layer.renameAttribute(idx, 'BASSIN')
        elif field.name() == 'Num_statio' or field.name() == 'NUM_STATION' or field.name() == 'STATION':
            idx = layer.fields().indexFromName(field.name())
            layer.renameAttribute(idx, 'NUM_STATIO')
        elif field.name() == 'Nom_statio' or field.name() == 'NOM_STATIO' or field.name() == 'STATION0':
            idx = layer.fields().indexFromName(field.name())
            layer.renameAttribute(idx, 'NOM_STATIO')
        elif field.name() == 'Pays':
            idx = layer.fields().indexFromName(field.name())
            layer.renameAttribute(idx, 'PAYS')
        elif field.name() == 'Latitude' or field.name() == '_DD_':
            idx = layer.fields().indexFromName(field.name())
            layer.renameAttribute(idx, 'LATITUDE')
        elif field.name() == 'Longitude' or field.name() == '_DD_0':
            idx = layer.fields().indexFromName(field.name())
            layer.renameAttribute(idx, 'LONGITUDE')
        elif field.name() == 'Superficie':
            idx = layer.fields().indexFromName(field.name())
            layer.renameAttribute(idx, 'SUPERFICIE')
        elif field.name() == 'Date_debut' or field.name() == 'DATE_DEBUT':
            idx = layer.fields().indexFromName(field.name())
            layer.renameAttribute(idx, 'DEBUT_OBS')
            #****************************************************
        elif field.name() == 'DEBUT':
            idx = layer.fields().indexFromName(field.name())
            layer.renameAttribute(idx, 'DEBUT_OBS')
        elif field.name() == 'SUPERFICI':
            idx = layer.fields().indexFromName(field.name())
            layer.renameAttribute(idx, 'SUPERFICIE')


  
#    Close editing session and save changes
    layer.commitChanges()

################################################################################

"""-----------------------------
2. JOIN FIELDS 
---------------------------------"""

layers_names = []
layersPt_names = []
for layer in QgsProject.instance().mapLayers().values():
    
    if layer.geometryType() == 2:                                     # if the feature is a polygone(sub-watershed) 
        layers_names.append(layer.name())
 
    elif layer.geometryType() == 0:                                      # if the feature is a point(station)
        layersPt_names.append(layer.name())

     
    for i in layers_names:
        for e in layersPt_names:
            if i == e[:-2]:      #make the join only if the name of the station is equal to the name of the sub-catchment (line to be adapted according to the names of your data) 
                processing.run("native:joinattributestable", {'INPUT':'path_to_the_sub-watershed'+i+'.shp','FIELD':'NOM','INPUT_2':'path_to_stations'+e+'.shp','FIELD_2':'NOM_STATIO','FIELDS_TO_COPY':[],'METHOD':1,'DISCARD_NONMATCHING':False,'PREFIX':'','OUTPUT':'output_path'+i+'.shp'})



################################################################################

"""-----------------------------
3. JOIN FIELDS 
---------------------------------"""
# In this exemple we only want to delete the KM2 and PAYS_2 fields
for layer in layers:
#    print(layer.name())
    layer.startEditing()

    for field in layer.fields():
        
        if field.name() ==  'KM2'or field.name() ==  'PAYS_2':
            idx = layer.fields().indexFromName(field.name())
            layer.deleteAttribute(idx)
            
            

print("By Junior-Muyumba : muyumbaj2@gmail.com")
print("OK JAZZ".center(80,"♠"))
## -------------------------------- OK JAZZ ------------------------
