# -*- coding: utf-8 -*-

"""
mergedapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mergedapi.api_helper import APIHelper


class StorageClassMap(object):

    """Implementation of the 'StorageClassMap' model.

    TODO: type model description here.

    Attributes:
        gluster_fs (string): TODO: type description here.
        host_path (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "gluster_fs": 'GlusterFs',
        "host_path": 'HostPath'
    }

    _optionals = [
        'gluster_fs',
        'host_path',
    ]

    def __init__(self,
                 gluster_fs=APIHelper.SKIP,
                 host_path=APIHelper.SKIP):
        """Constructor for the StorageClassMap class"""

        # Initialize members of the class
        if gluster_fs is not APIHelper.SKIP:
            self.gluster_fs = gluster_fs 
        if host_path is not APIHelper.SKIP:
            self.host_path = host_path 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary

        gluster_fs = dictionary.get("GlusterFs") if dictionary.get("GlusterFs") else APIHelper.SKIP
        host_path = dictionary.get("HostPath") if dictionary.get("HostPath") else APIHelper.SKIP
        # Return an object of this model
        return cls(gluster_fs,
                   host_path)
