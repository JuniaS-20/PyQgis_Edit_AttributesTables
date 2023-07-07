# PyQgis_Edit_AttributesTables
This PyQgis script, based on the Qgis python API, is designed to help automate daily GIS tasks
This PyQgis script, based on the Qgis python API, is designed to help automate daily GIS tasks, in particular editing attribute tables for vector data. This script presents 3 operations, which you can test for yourself using the enclosed test data https://drive.google.com/file/d/1ne54vZlDBU1p-JIapM-Z_FVA7fzLFlz2/view?usp=drive_link. You can then adapt them to your own needs.
- Renaming fields in an attribute table: For practical reasons, when you want to insert vector-type spatial data into a PostgreSQL-type spatial database, for example, you'd like them to be structurally homogeneous and field-named, to facilitate query execution. However, this is not always the case. So this code snippet comes in handy when you want to homogenize the attribute tables of several data of the same type and from the same project with a single click.

- Layer attribute table joins: automatically across multiple layers.

- Deletion of fields no longer required.
##################################################################################

Test script with data.
1.	Here we aim to have all the attribute tables of the hydrological measurement stations with the same field names as presented in the script header. To do this, simply add all the layers in the STATION directory to the Qgis project, keeping parts 2 and 3 of the script as comments. Before running the script, take a look at the various tables to see the chaos before renaming.
2.	The idea here is to retrieve the additional information from the Alindao station, which is the outlet of the Alindao sub-basin, and attach it to the Alindao table.
For the script to work, don't forget to replace the paths where the sub-basins and stations are located, and the output path where the attached file will be written. Again, keep parts 1 and 3 as comments before running the script.
3.	Here we want to delete the PAYS_2 and KM2 fields from the attached Alindao file. Again, comment on parts 1 and 2.
NB: To avoid renaming or deleting unwanted fields, the best way would be to copy each part and take it individually as a separate script, while keeping the header that calls the processing functions.

- 4. REPROJECT_LAYERS Added is a piece of code that reprojects layers.
It lets you reproject all your vector or raster layers from your Qgis project to the CRS you want.
Good luck and please let me know of any difficulties or requirements.
