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
Base cloud controller class.

Base class for interacting with Cloud APIs to create and manage cloud
instances.

"""
import logging
log = logging.getLogger(__name__)

from libcloud.compute.base import NodeAuthSSHKey
from .exceptions import ItemNotFound, KeyPairExists, MethodNotAllowed
from .exceptions import OverLimit, BadRequest, ServiceUnavailable
from .exceptions import Unauthorized, ApiError


def parse_exception(exception):
    """
    Parse the exception to separate the HTTP status code from the text.

    Libcloud raises many exceptions of the form:
        Exception("<http status code> <http error> <reponse body>")

    in lieu of raising specific incident-based exceptions.

    """

    e_str = str(exception)

    try:
        status = int(e_str[0:3])
        error_text = e_str[3:]

    except ValueError:
        status = None
        error_text = e_str

    return status, error_text


class BaseCloudCtrl(object):

    """ Base class for interacting with a cloud provider API. """

    http_status_to_exception = {
        400: BadRequest,
        401: Unauthorized,
        404: ItemNotFound,
        405: MethodNotAllowed,
        413: OverLimit,
        500: ApiError,
        503: ServiceUnavailable
    }

    def __init__(self, username, api_key):
        self.username = username
        self.api_key = api_key

    def _handle_exception(self, status, error_text, response_overrides=None):
        """ Raise an exception based on the HTTP status. """

        if response_overrides:
            if status in response_overrides:
                raise response_overrides[status](error_text)

        raise self.http_status_to_exception[status](error_text)

    def authenticate(self):
        """ Validate cloud account credentials.  Return boolean. """
        raise NotImplementedError

    def list_sizes(self):
        """ Return a list of NodeSize objects. """

        return self.driver.list_sizes()

    def list_flavors(self):
        """ Return an iterable of flavors """

        raise NotImplementedError

    def create_instance(self, name, size_id, image_id, keypair=None):
        """
        Create a new instance with the supplied attributes.

        Return a Node object.

        """
        try:
            image = self.get_image(image_id)
            if image is None:
                raise ItemNotFound("Image not found")

            size = self.driver.ex_get_size(size_id)

            args = {
                "name": name,
                "size": size,
                "image": image,
            }

            if keypair is not None:
                auth_key = NodeAuthSSHKey(keypair.public_key)
                args["auth"] = auth_key

            return self.driver.create_node(**args)

        except Exception as e:
            status, error_text = parse_exception(e)

            if status:
                self._handle_exception(status, error_text)
            else:
                log.error("create_instance method raised an exception: {}".format(e))

    def delete_instance(self, instance):
        """ Delete the specified instance.  Returns True or False. """

        try:
            return self.driver.destroy_node(instance)

        except Exception as e:

            status, error_text = parse_exception(e)

            if status:
                self._handle_exception(status, error_text)
            else:
                raise e

    def get_instance(self, instance):
        """ Return a Node object representing the requested instance. """

        for i in self.driver.list_nodes():
            if i.id == instance.id:
                return i

        raise ItemNotFound("Instance not found")

    def list_instances(self):
        """ Return a list of instances in the current region. """

        try:
            return self.driver.list_nodes()
        except Exception as e:
            log.error("list_instances returned an error: {}".format(e))


    def create_key_pair(self, name):
        """ Create and return a new Key Pair. """

        response_overrides = {
            409: KeyPairExists
        }
        try:
            return self.driver.create_key_pair(name)

        except Exception as e:
            status, error_text = parse_exception(e)
            if status:
                self._handle_exception(status, error_text, response_overrides)
            else:
                raise e

    def delete_key_pair(self, keypair):
        """ Delete the keypair. Returns True or False. """

        try:
            return self.driver.delete_key_pair(keypair)

        except Exception as e:
            status, error_text = parse_exception(e)
            if status:
                self._handle_exception(status, error_text)
            else:
                raise e

    def list_key_pairs(self):
        """ Return a list of Key Pairs. """

        return self.driver.list_key_pairs()
