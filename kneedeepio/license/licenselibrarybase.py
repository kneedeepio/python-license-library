#!/usr/bin/env python3

### IMPORTS ###

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class LicenseLibraryBase:
    def import_license(self, license_data):
        # Used to import a license from an external transport mechanism, such as a file.
        raise NotImplementedError

    def export_license(self, license_identifier):
        # Used to export a license to an external transport mechanism, such as a file.
        raise NotImplementedError

    def insert_license(self, license_instance):
        # FIXME: Should this check to make sure any updates are newer than the existing?
        raise NotImplementedError

    def retrieve_license(self, license_identifier):
        raise NotImplementedError

    def remove_license(self, license_identifier):
        # FIXME: Should removal be allowed here?  It can always be blocked in wrapping implementation.
        raise NotImplementedError

    # FIXME: Should there be a "revoke" option, to deactivate but not remove a license?

    def retrieve_licenses_for_assignee(self, license_assignee):
        raise NotImplementedError
