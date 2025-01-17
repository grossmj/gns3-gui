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
Default general settings.
"""

import os
import sys
import tempfile
import platform

# Projects directory location
DEFAULT_PROJECTS_PATH = os.path.normpath(os.path.expanduser("~/GNS3/projects"))

# Images directory location
DEFAULT_IMAGES_PATH = os.path.normpath(os.path.expanduser("~/GNS3/images"))

# Temporary files location
DEFAULT_TEMPORARY_FILES_PATH = tempfile.gettempdir()

# Default path to the local GNS3 server executable
if sys.platform.startswith("win"):
    DEFAULT_LOCAL_SERVER_PATH = "gns3server.exe"
elif sys.platform.startswith("darwin") and hasattr(sys, "frozen"):
    DEFAULT_LOCAL_SERVER_PATH = "server/Contents/MacOS/gns3server"
else:
    paths = [os.getcwd()] + os.environ["PATH"].split(os.pathsep)
    # look for gns3server in the current working directory and $PATH
    DEFAULT_LOCAL_SERVER_PATH = "gns3server"
    for path in paths:
        try:
            if "gns3server" in os.listdir(path) and os.access(os.path.join(path, "gns3server"), os.X_OK):
                DEFAULT_LOCAL_SERVER_PATH = os.path.join(path, "gns3server")
                break
        except OSError:
            continue

DEFAULT_LOCAL_SERVER_HOST = "127.0.0.1"
DEFAULT_LOCAL_SERVER_PORT = 8000

# Pre-configured Telnet console commands on various OSes
if sys.platform.startswith("win") and "PROGRAMFILES(X86)" in os.environ and os.path.exists(os.environ["PROGRAMFILES(X86)"]):
    # windows 64-bit
    PRECONFIGURED_TELNET_CONSOLE_COMMANDS = {'Putty (included with GNS3)': 'putty.exe -telnet %h %p -wt "%d" -gns3 5 -skin 4',
                                             'SuperPutty': 'SuperPutty.exe -telnet "%h -P %p -wt \"%d\" -gns3 5 -skin 4"',
                                             'SecureCRT': '"C:\Program Files\\VanDyke Software\\SecureCRT\\SecureCRT.EXE" /SCRIPT securecrt.vbs /ARG %d /T /TELNET %h %p',
                                             'TeraTerm Pro (64-bit)': r'"C:\Program Files (x86)\teraterm\ttermpro.exe" /W="%d" /M="C:\Program Files\GNS3\ttstart.macro" /T=1 %h %p',
                                             'TeraTerm Pro (32-bit)': r'"C:\Program Files\teraterm\ttermpro.exe" /W="%d" /M="C:\Program Files\GNS3\ttstart.macro" /T=1 %h %p"',
                                             'Telnet': 'telnet %h %p',
                                             'Xshell 4': 'C:\Program Files (x86)\\NetSarang\\Xshell 4\\xshell.exe -url telnet://%h:%p'}

    # default Windows 64-bit Telnet console command
    if os.path.exists(os.getcwd() + os.sep + "SuperPutty.exe"):
        DEFAULT_TELNET_CONSOLE_COMMAND = PRECONFIGURED_TELNET_CONSOLE_COMMANDS["SuperPutty"]
    else:
        DEFAULT_TELNET_CONSOLE_COMMAND = PRECONFIGURED_TELNET_CONSOLE_COMMANDS["Putty (included with GNS3)"]

elif sys.platform.startswith("win"):
    # windows 32-bit
    PRECONFIGURED_TELNET_CONSOLE_COMMANDS = {'Putty (included with GNS3)': 'putty.exe -telnet %h %p -wt "%d" -gns3 5 -skin 4',
                                             'SuperPutty': 'SuperPutty.exe -telnet "%h -P %p -wt \"%d\" -gns3 5 -skin 4"',
                                             'SecureCRT': '"C:\Program Files\\VanDyke Software\\SecureCRT\\SecureCRT.EXE" /SCRIPT securecrt.vbs /ARG %d /T /TELNET %h %p',
                                             'TeraTerm Pro': r'"C:\Program Files\teraterm\ttermpro.exe" /W="%d" /M="C:\Program Files\GNS3\ttstart.macro" /T=1 %h %p"',
                                             'Telnet': 'telnet %h %p',
                                             'Xshell 4': 'C:\Program Files\\NetSarang\\Xshell 4\\xshell.exe -url telnet://%h:%p'}

    # default Windows 32-bit Telnet console command
    if os.path.exists(os.getcwd() + os.sep + "SuperPutty.exe"):
        DEFAULT_TELNET_CONSOLE_COMMAND = PRECONFIGURED_TELNET_CONSOLE_COMMANDS["SuperPutty"]
    else:
        DEFAULT_TELNET_CONSOLE_COMMAND = PRECONFIGURED_TELNET_CONSOLE_COMMANDS["Putty (included with GNS3)"]

elif sys.platform.startswith("darwin"):
    # Mac OS X
    PRECONFIGURED_TELNET_CONSOLE_COMMANDS = {'Terminal': "/usr/bin/osascript -e 'tell application \"terminal\" to do script with command \"telnet %h %p ; exit\"'",
                                             'iTerm': "/usr/bin/osascript -e 'tell app \"iTerm\"' -e 'activate' -e 'set myterm to the first terminal' -e 'tell myterm' -e 'set mysession to (make new session at the end of sessions)' -e 'tell mysession' -e 'exec command \"telnet %h %p\"' -e 'set name to \"%d\"' -e 'end tell' -e 'end tell' -e 'end tell'",
                                             'SecureCRT': '/Applications/SecureCRT.app/Contents/MacOS/SecureCRT /ARG %d /T /TELNET %h %p'}

    # default Mac OS X Telnet console command
    DEFAULT_TELNET_CONSOLE_COMMAND = PRECONFIGURED_TELNET_CONSOLE_COMMANDS["Terminal"]

else:
    PRECONFIGURED_TELNET_CONSOLE_COMMANDS = {'Xterm': 'xterm -T %d -e \'telnet %h %p\'',
                                             'Putty': 'putty -telnet %h %p -title %d -sl 2500 -fg SALMON1 -bg BLACK',
                                             'Gnome Terminal': 'gnome-terminal -t %d -e \'telnet %h %p\'',
                                             'ROXTerm': 'roxterm -n %d --tab -e telnet %h %p',
                                             'KDE Konsole': 'konsole --new-tab -p tabtitle=%d -e telnet %h %p',
                                             'SecureCRT': 'SecureCRT /T /N "%d"  /TELNET %h %p',
                                             'Mate Terminal': 'mate-terminal --tab -e \'telnet %h %p\'  -t %d'}

    # default Telnet console command on other systems
    DEFAULT_TELNET_CONSOLE_COMMAND = PRECONFIGURED_TELNET_CONSOLE_COMMANDS["Xterm"]

    if sys.platform.startswith("linux"):
        distro = platform.linux_distribution()[0]
        if distro == "Debian" or distro == "Ubuntu" or distro == "LinuxMint":
            DEFAULT_TELNET_CONSOLE_COMMAND = PRECONFIGURED_TELNET_CONSOLE_COMMANDS["Gnome Terminal"]

# Pre-configured serial console commands on various OSes
if sys.platform.startswith("win"):
    # Windows
    PRECONFIGURED_SERIAL_CONSOLE_COMMANDS = {'Putty (included with GNS3)': 'putty.exe -serial %s -wt "%d [Local Console]" -gns3 5',
                                             'SuperPutty': 'SuperPutty.exe -serial "%s -wt \"%d\" -gns3 5 -skin 4"'}

    # default Windows serial console command
    if os.path.exists(os.getcwd() + os.sep + "SuperPutty.exe"):
        DEFAULT_SERIAL_CONSOLE_COMMAND = PRECONFIGURED_SERIAL_CONSOLE_COMMANDS["SuperPutty"]
    else:
        DEFAULT_SERIAL_CONSOLE_COMMAND = PRECONFIGURED_SERIAL_CONSOLE_COMMANDS["Putty (included with GNS3)"]

elif sys.platform.startswith("darwin"):
    # Mac OS X
    PRECONFIGURED_SERIAL_CONSOLE_COMMANDS = {'Terminal + socat': "/usr/bin/osascript -e 'tell application \"terminal\" to do script with command \"socat UNIX-CONNECT:\\\"%s\\\" stdio,raw,echo=0 ; exit\"'"}

    # default Mac OS X serial console command
    DEFAULT_SERIAL_CONSOLE_COMMAND = PRECONFIGURED_SERIAL_CONSOLE_COMMANDS["Terminal + socat"]

else:
    PRECONFIGURED_SERIAL_CONSOLE_COMMANDS = {'Xterm + socat': 'xterm -T %d -e \'socat UNIX-CONNECT:"%s" stdio,raw,echo=0\'',
                                             'Gnome Terminal + socat': 'gnome-terminal -t %d -e \'socat UNIX-CONNECT:"%s" stdio,raw,echo=0\'',
                                             'Konsole + socat': 'konsole --new-tab -p tabtitle=%d -e \'socat UNIX-CONNECT:"%s" stdio,raw,echo=0\''}

    # default serial console command on other systems
    DEFAULT_SERIAL_CONSOLE_COMMAND = PRECONFIGURED_SERIAL_CONSOLE_COMMANDS["Xterm + socat"]

    if sys.platform.startswith("linux"):
        distro = platform.linux_distribution()[0]
        if distro == "Debian" or distro == "Ubuntu" or distro == "LinuxMint":
            DEFAULT_SERIAL_CONSOLE_COMMAND = PRECONFIGURED_SERIAL_CONSOLE_COMMANDS["Gnome Terminal + socat"]

# Pre-configured packet capture reader commands on various OSes
WIRESHARK_NORMAL_CAPTURE = "Wireshark Traditional Capture"
WIRESHARK_LIVE_TRAFFIC_CAPTURE = "Wireshark Live Traffic Capture"

if sys.platform.startswith("win"):
    PRECONFIGURED_PACKET_CAPTURE_READER_COMMANDS = {WIRESHARK_NORMAL_CAPTURE: "C:\Program Files\Wireshark\wireshark.exe %c",
                                                    WIRESHARK_LIVE_TRAFFIC_CAPTURE: 'tail.exe -f -c +0b %c | "C:\Program Files\Wireshark\wireshark.exe" -k -i -'}

elif sys.platform.startswith("darwin"):
    # Mac OS X
    PRECONFIGURED_PACKET_CAPTURE_READER_COMMANDS = {WIRESHARK_NORMAL_CAPTURE: "/usr/bin/open -a /Applications/Wireshark.app %c",
                                                    WIRESHARK_LIVE_TRAFFIC_CAPTURE: "tail -f -c +0 %c | /Applications/Wireshark.app/Contents/Resources/bin/wireshark -k -i -"}

elif sys.platform.startswith("freebsd"):
    # FreeBSD
    PRECONFIGURED_PACKET_CAPTURE_READER_COMMANDS = {WIRESHARK_NORMAL_CAPTURE: "wireshark %c",
                                                    WIRESHARK_LIVE_TRAFFIC_CAPTURE: "gtail -f -c +0b %c | wireshark -k -i -"}
else:
    PRECONFIGURED_PACKET_CAPTURE_READER_COMMANDS = {WIRESHARK_NORMAL_CAPTURE: "wireshark %c",
                                                    WIRESHARK_LIVE_TRAFFIC_CAPTURE: "tail -f -c +0b %c | wireshark -k -i -"}

DEFAULT_PACKET_CAPTURE_READER_COMMAND = PRECONFIGURED_PACKET_CAPTURE_READER_COMMANDS[WIRESHARK_LIVE_TRAFFIC_CAPTURE]

DEFAULT_PACKET_CAPTURE_ANALYZER_COMMAND = ""
if sys.platform.startswith("win") and "PROGRAMFILES(X86)" in os.environ and os.path.exists(os.environ["PROGRAMFILES(X86)"]):
    # Windows 64-bit
    DEFAULT_PACKET_CAPTURE_ANALYZER_COMMAND = r'"C:\Program Files (x86)\SolarWinds\ResponseTimeViewer\ResponseTimeViewer.exe" %c'

GENERAL_SETTINGS = {
    "projects_path": DEFAULT_PROJECTS_PATH,
    "images_path": DEFAULT_IMAGES_PATH,
    "temporary_files_path": DEFAULT_TEMPORARY_FILES_PATH,
    "check_for_update": True,
    "slow_device_start_all": 0,
    "link_manual_mode": True,
    "telnet_console_command": DEFAULT_TELNET_CONSOLE_COMMAND,
    "serial_console_command": DEFAULT_SERIAL_CONSOLE_COMMAND,
    "auto_close_console": True,
    "bring_console_to_front": True,
    "slow_console_all": 0.5,
}

GENERAL_SETTING_TYPES = {
    "projects_path": str,
    "images_path": str,
    "temporary_files_path": str,
    "check_for_update": bool,
    "slow_device_start_all": int,
    "link_manual_mode": bool,
    "telnet_console_command": str,
    "serial_console_command": str,
    "auto_close_console": bool,
    "bring_console_to_front": bool,
    "slow_console_all": float,
}

GRAPHICS_VIEW_SETTINGS = {
    "scene_width": 2000,
    "scene_height": 1000,
    "draw_rectangle_selected_item": False,
    "draw_link_status_points": True,
    "default_label_font": "TypeWriter,10,-1,5,75,0,0,0,0,0",
    "default_label_color": "#000000",
}

GRAPHICS_VIEW_SETTING_TYPES = {
    "scene_width": int,
    "scene_height": int,
    "draw_rectangle_selected_item": bool,
    "draw_link_status_points": bool,
    "default_label_font": str,
    "default_label_color": str,
}

PACKET_CAPTURE_SETTINGS = {
    "packet_capture_reader_command": DEFAULT_PACKET_CAPTURE_READER_COMMAND,
    "command_auto_start": True,
    "packet_capture_analyzer_command": DEFAULT_PACKET_CAPTURE_ANALYZER_COMMAND,
}

PACKET_CAPTURE_SETTING_TYPES = {
    "packet_capture_reader_command": str,
    "command_auto_start": bool,
    "packet_capture_analyzer_command": str,
}

CLOUD_SETTINGS = {
    "cloud_user_name": "",
    "cloud_api_key": "",
    "cloud_store_api_key": False,
    # no default value at startup, users must choose and we need to know if they've already done it
    "cloud_store_api_key_chosen": False,
    "cloud_provider": "rackspace",
    "cloud_region": "",
    "instances_per_project": 0,
    "default_flavor": "",
    "new_instance_flavor": "",
    "memory_per_new_instance": 1,  # TODO remove
    "accepted_terms": False,
    "instance_timeout": 30,
    "default_image": "",
}

CLOUD_SETTINGS_TYPES = {
    "cloud_user_name": str,
    "cloud_api_key": str,
    "cloud_store_api_key": bool,
    "cloud_store_api_key_chosen": bool,
    "cloud_provider": str,
    "cloud_region": str,
    "instances_per_project": int,
    "default_flavor": str,
    "new_instance_flavor": str,
    "memory_per_new_instance": int,  # TODO remove
    "accepted_terms": bool,
    "instance_timeout": int,
    "default_image": str,
}

# TODO proof of concept, needs review
CLOUD_PROVIDERS = {
    "rackspace": ("Rackspace", 'gns3.cloud.rackspace_ctrl.RackspaceCtrl'),
}
