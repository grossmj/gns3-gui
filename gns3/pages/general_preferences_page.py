# -*- coding: utf-8 -*-
#
# Copyright (C) 2014 GNS3 Technologies Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Configuration page for general preferences.
"""

import os
import shutil
from gns3.qt import QtGui, QtCore
from ..ui.general_preferences_page_ui import Ui_GeneralPreferencesPageWidget
from ..settings import GRAPHICS_VIEW_SETTINGS, GENERAL_SETTINGS, PRECONFIGURED_TELNET_CONSOLE_COMMANDS, PRECONFIGURED_SERIAL_CONSOLE_COMMANDS


class GeneralPreferencesPage(QtGui.QWidget, Ui_GeneralPreferencesPageWidget):
    """
    QWidget configuration page for general preferences.
    """

    def __init__(self):

        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self._remote_servers = {}

        # Load the pre-configured console commands
        for name, cmd in sorted(PRECONFIGURED_TELNET_CONSOLE_COMMANDS.items()):
            self.uiTelnetConsolePreconfiguredCommandComboBox.addItem(name, cmd)
        for name, cmd in sorted(PRECONFIGURED_SERIAL_CONSOLE_COMMANDS.items()):
            self.uiSerialConsolePreconfiguredCommandComboBox.addItem(name, cmd)

        # Display the path of the settings file
        settings = QtCore.QSettings()
        self.uiConfigurationFileLabel.setText(settings.fileName())

        self.uiProjectsPathToolButton.clicked.connect(self._projectsPathSlot)
        self.uiImagesPathToolButton.clicked.connect(self._imagesPathSlot)
        self.uiTemporaryFilesPathToolButton.clicked.connect(self._temporaryFilesPathSlot)
        self.uiImportConfigurationFilePushButton.clicked.connect(self._importConfigurationFileSlot)
        self.uiExportConfigurationFilePushButton.clicked.connect(self._exportConfigurationFileSlot)
        self.uiRestoreDefaultsPushButton.clicked.connect(self._restoreDefaultsSlot)
        self.uiTelnetConsolePreconfiguredCommandPushButton.clicked.connect(self._telnetConsolePreconfiguredCommandSlot)
        self.uiSerialConsolePreconfiguredCommandPushButton.clicked.connect(self._serialConsolePreconfiguredCommandSlot)
        self.uiDefaultLabelFontPushButton.clicked.connect(self._setDefaultLabelFontSlot)
        self.uiDefaultLabelColorPushButton.clicked.connect(self._setDefaultLabelColorSlot)
        self._default_label_color = QtGui.QColor(QtCore.Qt.black)

    def _projectsPathSlot(self):
        """
        Slot to select the projects directory path.
        """

        directory = self._general_settings["projects_path"]
        path = QtGui.QFileDialog.getExistingDirectory(self, "My projects directory", directory, QtGui.QFileDialog.ShowDirsOnly)
        if path:
            self.uiProjectsPathLineEdit.setText(path)
            self.uiProjectsPathLineEdit.setCursorPosition(0)

    def _imagesPathSlot(self):
        """
        Slot to select the images directory path.
        """

        directory = self._general_settings["images_path"]
        path = QtGui.QFileDialog.getExistingDirectory(self, "My images directory", directory, QtGui.QFileDialog.ShowDirsOnly)
        if path:
            self.uiImagesPathLineEdit.setText(path)
            self.uiImagesPathLineEdit.setCursorPosition(0)

    def _temporaryFilesPathSlot(self):
        """
        Slot to select the temporary files directory path.
        """

        directory = self._general_settings["temporary_files_path"]
        path = QtGui.QFileDialog.getExistingDirectory(self, "Temporary files directory", directory, QtGui.QFileDialog.ShowDirsOnly)
        if path:
            self.uiTemporaryFilesPathLineEdit.setText(path)
            self.uiTemporaryFilesPathLineEdit.setCursorPosition(0)

    def _restoreDefaultsSlot(self):
        """
        Slot to restore default settings
        """

        self._populateGeneralSettingWidgets(GENERAL_SETTINGS)
        self._populateGraphicsViewSettingWidgets(GRAPHICS_VIEW_SETTINGS)

    def _telnetConsolePreconfiguredCommandSlot(self):
        """
        Slot to set a chosen pre-configured Telnet console command.
        """

        self.uiTelnetConsoleCommandLineEdit.clear()
        command = self.uiTelnetConsolePreconfiguredCommandComboBox.itemData(self.uiTelnetConsolePreconfiguredCommandComboBox.currentIndex(), QtCore.Qt.UserRole)
        self.uiTelnetConsoleCommandLineEdit.setText(command)
        self.uiTelnetConsoleCommandLineEdit.setCursorPosition(0)

    def _serialConsolePreconfiguredCommandSlot(self):
        """
        Slot to set a chosen pre-configured serial console command.
        """

        self.uiSerialConsoleCommandLineEdit.clear()
        command = self.uiSerialConsolePreconfiguredCommandComboBox.itemData(self.uiSerialConsolePreconfiguredCommandComboBox.currentIndex(), QtCore.Qt.UserRole)
        self.uiSerialConsoleCommandLineEdit.setText(command)
        self.uiSerialConsoleCommandLineEdit.setCursorPosition(0)

    def _importConfigurationFileSlot(self):
        """
        Slot to import a configuration file.
        """

        settings = QtCore.QSettings()
        configuration_file_path = settings.fileName()
        directory = os.path.dirname(configuration_file_path)

        path = QtGui.QFileDialog.getOpenFileName(self, "Import configuration file", directory, "Configuration file (*.conf);;All files (*.*)")
        if not path:
            return

        try:
            shutil.copyfile(path, configuration_file_path)
        except (shutil.Error, IOError) as e:
            QtGui.QMessageBox.critical(self, "Import configuration file", "Cannot import configuration file: {}".format(e))
            return

        QtGui.QMessageBox.information(self, "Configuration file", "Configuration file imported, default settings will be applied after a restart")

        # restart the application
        from ..main_window import MainWindow
        main_window = MainWindow.instance()
        main_window.reboot_signal.emit()

    def _exportConfigurationFileSlot(self):
        """
        Slot to export a configuration file.
        """

        settings = QtCore.QSettings()
        configuration_file_path = settings.fileName()
        directory = os.path.dirname(configuration_file_path)

        path = QtGui.QFileDialog.getSaveFileName(self, "Export configuration file", directory, "Configuration file (*.conf);;All files (*.*)")
        if not path:
            return

        try:
            shutil.copyfile(configuration_file_path, path)
        except (shutil.Error, IOError) as e:
            QtGui.QMessageBox.critical(self, "Export configuration file", "Cannot export configuration file: {}".format(e))
            return

    def _setDefaultLabelFontSlot(self):
        """
        Slot to select the default label font.
        """

        selected_font, ok = QtGui.QFontDialog.getFont(self.uiDefaultLabelStylePlainTextEdit.font(), self)
        if ok:
            self.uiDefaultLabelStylePlainTextEdit.setFont(selected_font)


    def _setDefaultLabelColorSlot(self):
        """
        Slot to select the default label color.
        """

        color = QtGui.QColorDialog.getColor(self._default_label_color, self)
        if color.isValid():
            self._default_label_color = color
            self.uiDefaultLabelStylePlainTextEdit.setStyleSheet("color : {}".format(color.name()))

    def _populateGeneralSettingWidgets(self, settings):
        """
        Populates the widgets with the settings.

        :param settings: General settings
        """

        self.uiProjectsPathLineEdit.setText(settings["projects_path"])
        self.uiImagesPathLineEdit.setText(settings["images_path"])
        self.uiTemporaryFilesPathLineEdit.setText(settings["temporary_files_path"])
        self.uiCheckForUpdateCheckBox.setChecked(settings["check_for_update"])
        self.uiLinkManualModeCheckBox.setChecked(settings["link_manual_mode"])
        self.uiSlowStartAllSpinBox.setValue(settings["slow_device_start_all"])
        self.uiTelnetConsoleCommandLineEdit.setText(settings["telnet_console_command"])
        self.uiTelnetConsoleCommandLineEdit.setCursorPosition(0)
        index = self.uiTelnetConsolePreconfiguredCommandComboBox.findData(settings["telnet_console_command"])
        if index != -1:
            self.uiTelnetConsolePreconfiguredCommandComboBox.setCurrentIndex(index)
        self.uiSerialConsoleCommandLineEdit.setText(settings["serial_console_command"])
        self.uiSerialConsoleCommandLineEdit.setCursorPosition(0)
        index = self.uiSerialConsolePreconfiguredCommandComboBox.findData(settings["serial_console_command"])
        if index != -1:
            self.uiSerialConsolePreconfiguredCommandComboBox.setCurrentIndex(index)
        self.uiCloseConsoleWindowsOnDeleteCheckBox.setChecked(settings["auto_close_console"])
        self.uiBringConsoleWindowToFrontCheckBox.setChecked(settings["bring_console_to_front"])
        self.uiSlowConsoleAllDoubleSpinBox.setValue(settings["slow_console_all"])

    def _populateGraphicsViewSettingWidgets(self, settings):
        """
        Populates the widgets with the settings.

        :param settings: Graphics view settings
        """

        self.uiSceneWidthSpinBox.setValue(settings["scene_width"])
        self.uiSceneHeightSpinBox.setValue(settings["scene_height"])
        self.uiRectangleSelectedItemCheckBox.setChecked(settings["draw_rectangle_selected_item"])
        self.uiDrawLinkStatusPointsCheckBox.setChecked(settings["draw_link_status_points"])

        qt_font = QtGui.QFont()
        if qt_font.fromString(settings["default_label_font"]):
            self.uiDefaultLabelStylePlainTextEdit.setFont(qt_font)
        qt_color = QtGui.QColor(settings["default_label_color"])
        if qt_color.isValid():
            self._default_label_color = qt_color
            self.uiDefaultLabelStylePlainTextEdit.setStyleSheet("color : {}".format(qt_color.name()))

    def loadPreferences(self):
        """
        Loads the general preferences.
        """

        from ..main_window import MainWindow
        self._general_settings = MainWindow.instance().settings()
        self._populateGeneralSettingWidgets(self._general_settings)

        graphics_view_settings = MainWindow.instance().uiGraphicsView.settings()
        self._populateGraphicsViewSettingWidgets(graphics_view_settings)

    def savePreferences(self):
        """
        Saves the general preferences.
        """

        new_settings = {}
        new_settings["projects_path"] = self.uiProjectsPathLineEdit.text()
        new_settings["images_path"] = self.uiImagesPathLineEdit.text()
        new_settings["temporary_files_path"] = self.uiTemporaryFilesPathLineEdit.text()
        new_settings["check_for_update"] = self.uiCheckForUpdateCheckBox.isChecked()
        new_settings["link_manual_mode"] = self.uiLinkManualModeCheckBox.isChecked()
        new_settings["slow_device_start_all"] = self.uiSlowStartAllSpinBox.value()
        new_settings["telnet_console_command"] = self.uiTelnetConsoleCommandLineEdit.text()
        new_settings["serial_console_command"] = self.uiSerialConsoleCommandLineEdit.text()
        new_settings["auto_close_console"] = self.uiCloseConsoleWindowsOnDeleteCheckBox.isChecked()
        new_settings["bring_console_to_front"] = self.uiBringConsoleWindowToFrontCheckBox.isChecked()
        new_settings["slow_console_all"] = self.uiSlowConsoleAllDoubleSpinBox.value()

        from ..main_window import MainWindow
        MainWindow.instance().setSettings(new_settings)

        new_settings = {}
        new_settings["scene_width"] = self.uiSceneWidthSpinBox.value()
        new_settings["scene_height"] = self.uiSceneHeightSpinBox.value()
        new_settings["draw_rectangle_selected_item"] = self.uiRectangleSelectedItemCheckBox.isChecked()
        new_settings["draw_link_status_points"] = self.uiDrawLinkStatusPointsCheckBox.isChecked()
        new_settings["default_label_font"] = self.uiDefaultLabelStylePlainTextEdit.font().toString()
        new_settings["default_label_color"] = self._default_label_color.name()
        MainWindow.instance().uiGraphicsView.setSettings(new_settings)
