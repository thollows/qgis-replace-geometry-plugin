# qgis-replace-geometry-plugin
A QGIS 3 plugin to replace an existing features geometry

### Installation
Copy the replace_geometry folder into your QGIS plugins folder.
In Windows this is %AppData%\QGIS\QGIS3\profiles\default\python\plugins

Start QGIS and open the Plugin Manager in QGIS.

In the Installed plugins tab, check the 'Replace Geometry' plugin to activate.

Click the blue 'Replace Geometry' on the toolbar. This will open a small docked widget.

### Operation
The plugin allows an existing features geometry to be replaced with an entirely new geometry. 

Create a new geometry by copying/pasting or by drawing from scratch. Click the 'Swap Attributes' button to transpose each featues attributes. 
    
If 'Replace Geometry' is checked, the oldest feature (by fid) will be deleted. It can be undeleted with the 'Undo' button but the attributes will need to be swapped again with 'Replace Geometry' unchecked. 

If 'Replace Geometry' is unchecked the attributes wil be transposed and the layer's attribute table will be opened so the result can be checked before deleting the unwanted feature.
