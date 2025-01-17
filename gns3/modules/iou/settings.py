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

import sys
import os

"""
Default IOU settings.
"""

if sys.platform.startswith("linux"):
    paths = [os.getcwd()] + os.environ["PATH"].split(os.pathsep)
    # look for iouyap in the current working directory and $PATH
    DEFAULT_IOUYAP_PATH = "iouyap"
    for path in paths:
        try:
            if "iouyap" in os.listdir(path) and os.access(os.path.join(path, "iouyap"), os.X_OK):
                DEFAULT_IOUYAP_PATH = os.path.join(path, "iouyap")
                break
        except OSError:
            continue
else:
    DEFAULT_IOUYAP_PATH = ""

IOU_SETTINGS = {
    "iourc": "",
    "iouyap": DEFAULT_IOUYAP_PATH,
    "console_start_port_range": 4001,
    "console_end_port_range": 4500,
    "udp_start_port_range": 30001,
    "udp_end_port_range": 35000,
    "use_local_server": True,
}

# IOU is only available on Linux
if not sys.platform.startswith("linux"):
    IOU_SETTINGS["use_local_server"] = False

IOU_SETTING_TYPES = {
    "iourc": str,
    "iouyap": str,
    "console_start_port_range": int,
    "console_end_port_range": int,
    "udp_start_port_range": int,
    "udp_end_port_range": int,
    "use_local_server": bool,
}
