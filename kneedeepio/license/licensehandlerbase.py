#!/usr/bin/env python3

### IMPORTS ###

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class LicenseHandlerBase:
    def import_license(self, license_data):
        # Used to import a license from an external transport mechanism, such as a file.
        raise NotImplementedError

    def export_license(self, identifier):
        # Used to export a license to an external transport mechanism, such as a file.
        raise NotImplementedError

    def generate_license(self):
        raise NotImplementedError

    def validate_license(self, identifier):
        # FIXME: This should check the signature (and all of the other values) for validity and return True or False
        raise NotImplementedError

    def deactivate_license(self):
        raise NotImplementedError

    def enumerate_license(self):
        raise NotImplementedError

# The validity should be checked by a handler, not internal to the license, so removing this from the license class
# def is_license_valid(self):
#     # FIXME: This should check the signature (and all of the other values) for validity and return True or False
#     raise NotImplementedError

