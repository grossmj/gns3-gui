# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/grossmj/PycharmProjects/gns3-gui/gns3/modules/qemu/ui/qemu_preferences_page.ui'
#
# Created: Mon Sep 22 20:59:01 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_QemuPreferencesPageWidget(object):
    def setupUi(self, QemuPreferencesPageWidget):
        QemuPreferencesPageWidget.setObjectName(_fromUtf8("QemuPreferencesPageWidget"))
        QemuPreferencesPageWidget.resize(432, 586)
        self.verticalLayout_2 = QtGui.QVBoxLayout(QemuPreferencesPageWidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.uiTabWidget = QtGui.QTabWidget(QemuPreferencesPageWidget)
        self.uiTabWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.uiTabWidget.setObjectName(_fromUtf8("uiTabWidget"))
        self.uiServerSettingsTabWidget = QtGui.QWidget()
        self.uiServerSettingsTabWidget.setObjectName(_fromUtf8("uiServerSettingsTabWidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.uiServerSettingsTabWidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.uiUseLocalServercheckBox = QtGui.QCheckBox(self.uiServerSettingsTabWidget)
        self.uiUseLocalServercheckBox.setChecked(True)
        self.uiUseLocalServercheckBox.setObjectName(_fromUtf8("uiUseLocalServercheckBox"))
        self.verticalLayout_3.addWidget(self.uiUseLocalServercheckBox)
        self.uiRemoteServersGroupBox = QtGui.QGroupBox(self.uiServerSettingsTabWidget)
        self.uiRemoteServersGroupBox.setObjectName(_fromUtf8("uiRemoteServersGroupBox"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout(self.uiRemoteServersGroupBox)
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.uiRemoteServersTreeWidget = QtGui.QTreeWidget(self.uiRemoteServersGroupBox)
        self.uiRemoteServersTreeWidget.setEnabled(False)
        self.uiRemoteServersTreeWidget.setObjectName(_fromUtf8("uiRemoteServersTreeWidget"))
        self.horizontalLayout_11.addWidget(self.uiRemoteServersTreeWidget)
        self.verticalLayout_3.addWidget(self.uiRemoteServersGroupBox)
        self.uiTabWidget.addTab(self.uiServerSettingsTabWidget, _fromUtf8(""))
        self.uiAdvancedSettingsTabWidget = QtGui.QWidget()
        self.uiAdvancedSettingsTabWidget.setObjectName(_fromUtf8("uiAdvancedSettingsTabWidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.uiAdvancedSettingsTabWidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.uiConsolePortRangeGroupBox = QtGui.QGroupBox(self.uiAdvancedSettingsTabWidget)
        self.uiConsolePortRangeGroupBox.setObjectName(_fromUtf8("uiConsolePortRangeGroupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.uiConsolePortRangeGroupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.uiConsoleStartPortSpinBox = QtGui.QSpinBox(self.uiConsolePortRangeGroupBox)
        self.uiConsoleStartPortSpinBox.setSuffix(_fromUtf8(" TCP"))
        self.uiConsoleStartPortSpinBox.setMinimum(1)
        self.uiConsoleStartPortSpinBox.setMaximum(65535)
        self.uiConsoleStartPortSpinBox.setProperty("value", 1)
        self.uiConsoleStartPortSpinBox.setObjectName(_fromUtf8("uiConsoleStartPortSpinBox"))
        self.horizontalLayout.addWidget(self.uiConsoleStartPortSpinBox)
        self.uiConsolePortRangeLabel = QtGui.QLabel(self.uiConsolePortRangeGroupBox)
        self.uiConsolePortRangeLabel.setObjectName(_fromUtf8("uiConsolePortRangeLabel"))
        self.horizontalLayout.addWidget(self.uiConsolePortRangeLabel)
        self.uiConsoleEndPortSpinBox = QtGui.QSpinBox(self.uiConsolePortRangeGroupBox)
        self.uiConsoleEndPortSpinBox.setSuffix(_fromUtf8(" TCP"))
        self.uiConsoleEndPortSpinBox.setMinimum(1)
        self.uiConsoleEndPortSpinBox.setMaximum(65535)
        self.uiConsoleEndPortSpinBox.setProperty("value", 1)
        self.uiConsoleEndPortSpinBox.setObjectName(_fromUtf8("uiConsoleEndPortSpinBox"))
        self.horizontalLayout.addWidget(self.uiConsoleEndPortSpinBox)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout_2.addWidget(self.uiConsolePortRangeGroupBox, 0, 0, 1, 2)
        self.uiUDPPortRangeGroupBox = QtGui.QGroupBox(self.uiAdvancedSettingsTabWidget)
        self.uiUDPPortRangeGroupBox.setObjectName(_fromUtf8("uiUDPPortRangeGroupBox"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.uiUDPPortRangeGroupBox)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.uiUDPStartPortSpinBox = QtGui.QSpinBox(self.uiUDPPortRangeGroupBox)
        self.uiUDPStartPortSpinBox.setSuffix(_fromUtf8(" UDP"))
        self.uiUDPStartPortSpinBox.setMinimum(1)
        self.uiUDPStartPortSpinBox.setMaximum(65535)
        self.uiUDPStartPortSpinBox.setProperty("value", 1)
        self.uiUDPStartPortSpinBox.setObjectName(_fromUtf8("uiUDPStartPortSpinBox"))
        self.horizontalLayout_4.addWidget(self.uiUDPStartPortSpinBox)
        self.uiUDPPortRangeLabel = QtGui.QLabel(self.uiUDPPortRangeGroupBox)
        self.uiUDPPortRangeLabel.setObjectName(_fromUtf8("uiUDPPortRangeLabel"))
        self.horizontalLayout_4.addWidget(self.uiUDPPortRangeLabel)
        self.uiUDPEndPortSpinBox = QtGui.QSpinBox(self.uiUDPPortRangeGroupBox)
        self.uiUDPEndPortSpinBox.setSuffix(_fromUtf8(" UDP"))
        self.uiUDPEndPortSpinBox.setMinimum(1)
        self.uiUDPEndPortSpinBox.setMaximum(65535)
        self.uiUDPEndPortSpinBox.setProperty("value", 1)
        self.uiUDPEndPortSpinBox.setObjectName(_fromUtf8("uiUDPEndPortSpinBox"))
        self.horizontalLayout_4.addWidget(self.uiUDPEndPortSpinBox)
        spacerItem1 = QtGui.QSpacerItem(147, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.gridLayout_2.addWidget(self.uiUDPPortRangeGroupBox, 1, 0, 1, 2)
        self.uiRestoreDefaultsPushButton = QtGui.QPushButton(self.uiAdvancedSettingsTabWidget)
        self.uiRestoreDefaultsPushButton.setObjectName(_fromUtf8("uiRestoreDefaultsPushButton"))
        self.gridLayout_2.addWidget(self.uiRestoreDefaultsPushButton, 2, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(254, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 2, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 304, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 3, 0, 1, 1)
        self.uiTabWidget.addTab(self.uiAdvancedSettingsTabWidget, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.uiTabWidget)

        self.retranslateUi(QemuPreferencesPageWidget)
        self.uiTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(QemuPreferencesPageWidget)

    def retranslateUi(self, QemuPreferencesPageWidget):
        QemuPreferencesPageWidget.setWindowTitle(_translate("QemuPreferencesPageWidget", "QEMU", None))
        self.uiUseLocalServercheckBox.setText(_translate("QemuPreferencesPageWidget", "Use the local server", None))
        self.uiRemoteServersGroupBox.setTitle(_translate("QemuPreferencesPageWidget", "Remote servers", None))
        self.uiRemoteServersTreeWidget.headerItem().setText(0, _translate("QemuPreferencesPageWidget", "Host", None))
        self.uiRemoteServersTreeWidget.headerItem().setText(1, _translate("QemuPreferencesPageWidget", "Port", None))
        self.uiTabWidget.setTabText(self.uiTabWidget.indexOf(self.uiServerSettingsTabWidget), _translate("QemuPreferencesPageWidget", "Server settings", None))
        self.uiConsolePortRangeGroupBox.setTitle(_translate("QemuPreferencesPageWidget", "Console port range", None))
        self.uiConsolePortRangeLabel.setText(_translate("QemuPreferencesPageWidget", "to", None))
        self.uiUDPPortRangeGroupBox.setTitle(_translate("QemuPreferencesPageWidget", "UDP tunneling port range", None))
        self.uiUDPPortRangeLabel.setText(_translate("QemuPreferencesPageWidget", "to", None))
        self.uiRestoreDefaultsPushButton.setText(_translate("QemuPreferencesPageWidget", "Restore defaults", None))
        self.uiTabWidget.setTabText(self.uiTabWidget.indexOf(self.uiAdvancedSettingsTabWidget), _translate("QemuPreferencesPageWidget", "Advanced settings", None))

