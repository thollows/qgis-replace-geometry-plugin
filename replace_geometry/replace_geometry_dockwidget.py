# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ReplaceGeometryDockWidget
                                 A QGIS plugin
 A QGIS 3 plugin to replace an existing feature's geometry
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2019-02-15
        git sha              : $Format:%H$
        copyright            : (C) 2019 by Tony Hollows
        email                : tony.hollows@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import pyqtSignal
from qgis.utils import iface
from qgis.gui import QgsMessageBar

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'replace_geometry_dockwidget_base.ui'))


class ReplaceGeometryDockWidget(QtWidgets.QDockWidget, FORM_CLASS):

    closingPlugin = pyqtSignal()

    def __init__(self, parent=None):
        """Constructor."""
        super(ReplaceGeometryDockWidget, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://doc.qt.io/qt-5/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.pushButton.clicked.connect(self.swap)
        self.checkBox.clicked.connect(self.checkboxmsg)

    def checkboxmsg(self):
        if self.checkBox.isChecked() == True:
            iface.messageBar().pushMessage(
            'Caution: ',
            'Oldest feature (by fid) will be deleted after swapping attributes',
            level=0, duration=5)

    def swap(self):
        self.layer = iface.activeLayer()

        # Check that a vector layer has been selected
        try:
            if self.layer.type() != 0:
                iface.messageBar().pushMessage(
                'Error',
                'You must select a vector layer',
                level=1, duration=3)
                return
        except:
                iface.messageBar().pushMessage(
                'Error',
                'No layer selected',
                level=1, duration=3)
                return

        self.layername = self.layer.name()

        # Check layer is editable
        if not self.layer.isEditable():
            iface.messageBar().pushMessage(
            'Error',
            'Layer {} is not editable'.format(self.layername),
            level=1, duration=3)
            return

        # Save layer to ensure features have a valid fid
        self.layer.commitChanges()
        self.layer.startEditing()

        # Get selected features
        self.selection = self.layer.selectedFeatures()
        self.count = (len(self.selection))
        if self.count != 2:
            iface.messageBar().pushMessage(
            'Error',
            'Please select 2 features. ({} selected)'.format(self.count),
            level=1, duration=3)
            return

        # Get first fid and attributes
        for feature in self.selection:
            self.f1 = feature.id()
            self.attrs = feature.attributes()
            break
        self.a1 = dict(enumerate(self.attrs))
        # Remove fid from attributes
        del self.a1[0]

        # Get second fid and attributes
        for feature in self.selection:
            self.f2 = feature.id()
            self.attrs = feature.attributes()
        self.a2 = dict(enumerate(self.attrs))
        # Remove fid from attributes
        del self.a2[0]

        # Get oldest fid
        if self.f1 > self.f2:
            self.old_fid = self.f2
        else:
            self.old_fid = self.f1

        # Swap attributes
        self.layer.dataProvider().changeAttributeValues({ self.f1 : self.a2 })
        self.layer.dataProvider().changeAttributeValues({ self.f2 : self.a1 })

        # either delete the old feature or show the attribute table
        if self.checkBox.isChecked() == True:
            self.layer.deleteFeature(self.old_fid)
            iface.messageBar().pushMessage(
            'Info',
            'Feature: #{} deleted.'.format(self.old_fid),
            level=3, duration=2)
        else:
            # open attribute table
            iface.showAttributeTable(self.layer)

        # show message
        iface.messageBar().pushMessage(
        'Layer: {}'.format(self.layername),
        'Feature: #{} swapped with feature #{}'.format(self.f1, self.f2),
        level=3, duration=3)

        # refresh map
        if iface.mapCanvas().isCachingEnabled():
            self.layer.triggerRepaint()
        else:
            iface.mapCanvas().refresh()

    def closeEvent(self, event):
        self.closingPlugin.emit()
        event.accept()

    def closeEvent(self, event):
        self.closingPlugin.emit()
        event.accept()