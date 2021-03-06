# qgis-replace-geometry-plugin
A QGIS 3 plugin to replace an existing feature's geometry

### Installation

Copy the replace_geometry folder into your QGIS plugins folder.

In Windows this is %AppData%\QGIS\QGIS3\profiles\default\python\plugins

Start QGIS and open the Plugin Manager.

In the Installed plugins tab, check the 'Replace Geometry' plugin to activate.

### Operation

Click the blue 'Replace Geometry' icon on the toolbar. This will open a small docked widget.

Create a new geometry by copying/pasting an existing feature or by drawing from scratch. Select both the original and new features. Click the 'Swap Attributes' button to transpose each feature’s attributes.
    
If 'Replace Geometry' is checked, the oldest feature (by fid) will be deleted. It can be undeleted with the 'Undo' button but the attributes will need to be swapped again with 'Replace Geometry' unchecked. 

If 'Replace Geometry' is unchecked the attributes will be transposed and the layer's attribute table will be opened so the result can be checked before deleting the unwanted feature.
