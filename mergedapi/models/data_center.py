# -*- coding: utf-8 -*-

"""
mergedapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mergedapi.api_helper import APIHelper
from mergedapi.models.params import Params


class DataCenter(object):

    """Implementation of the 'DataCenter' model.

    TODO: type model description here.

    Attributes:
        package_type (DataCenterPackageTypeEnum): Packages are optimized for
            various operating environments. Prepackaged images are available
            in OVA and QCOW formats.
        distribution (DataCenterDistributionEnum): Supported Kubernetes
            distribution for the selected cloud provider
        location (string): Indicate geo-location of cluster if you wish to use
            location based policies
        k_8_s_version (K8sVersionEnum): Version of K8s platform
        operating_system (string): Operating System for the master and worker
            nodes
        tags (list of Params): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "package_type": 'packageType',
        "distribution": 'distribution',
        "location": 'location',
        "k_8_s_version": 'k8sVersion',
        "operating_system": 'operatingSystem',
        "tags": 'tags'
    }

    _optionals = [
        'package_type',
        'distribution',
        'location',
        'k_8_s_version',
        'operating_system',
        'tags',
    ]

    def __init__(self,
                 package_type=APIHelper.SKIP,
                 distribution=APIHelper.SKIP,
                 location=APIHelper.SKIP,
                 k_8_s_version='1.18',
                 operating_system=APIHelper.SKIP,
                 tags=APIHelper.SKIP):
        """Constructor for the DataCenter class"""

        # Initialize members of the class
        if package_type is not APIHelper.SKIP:
            self.package_type = package_type 
        if distribution is not APIHelper.SKIP:
            self.distribution = distribution 
        if location is not APIHelper.SKIP:
            self.location = location 
        self.k_8_s_version = k_8_s_version 
        if operating_system is not APIHelper.SKIP:
            self.operating_system = operating_system 
        if tags is not APIHelper.SKIP:
            self.tags = tags 

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

        package_type = dictionary.get("packageType") if dictionary.get("packageType") else APIHelper.SKIP
        distribution = dictionary.get("distribution") if dictionary.get("distribution") else APIHelper.SKIP
        location = dictionary.get("location") if dictionary.get("location") else APIHelper.SKIP
        k_8_s_version = dictionary.get("k8sVersion") if dictionary.get("k8sVersion") else '1.18'
        operating_system = dictionary.get("operatingSystem") if dictionary.get("operatingSystem") else APIHelper.SKIP
        tags = None
        if dictionary.get('tags') is not None:
            tags = [Params.from_dictionary(x) for x in dictionary.get('tags')]
        else:
            tags = APIHelper.SKIP
        # Return an object of this model
        return cls(package_type,
                   distribution,
                   location,
                   k_8_s_version,
                   operating_system,
                   tags)
