# -*- coding: utf-8 -*-

"""
mergedapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class TerraformGitBranch1(object):

    """Implementation of the 'terraformGitBranch1' model.

    TODO: type model description here.

    Attributes:
        branch_name (string): TODO: type description here.
        terraform_path (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "branch_name": 'branchName',
        "terraform_path": 'terraformPath'
    }

    def __init__(self,
                 branch_name=None,
                 terraform_path=None):
        """Constructor for the TerraformGitBranch1 class"""

        # Initialize members of the class
        self.branch_name = branch_name 
        self.terraform_path = terraform_path 

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

        branch_name = dictionary.get("branchName") if dictionary.get("branchName") else None
        terraform_path = dictionary.get("terraformPath") if dictionary.get("terraformPath") else None
        # Return an object of this model
        return cls(branch_name,
                   terraform_path)
