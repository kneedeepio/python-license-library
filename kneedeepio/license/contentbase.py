#!/usr/bin/env python3

### IMPORTS ###

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class ContentBase:
    def set_content_from_license(self, value):
        # The value is supplied as a dict from the license object to this object to instantiate (aka load) the contents
        # of the license into this class.
        # NOTE: This MUST be overridden by the content class that implements this interface.
        raise NotImplementedError

    def get_content_for_license(self):
        # The config is returned as a dict from this method to the license object to be included in the license.
        # NOTE: This MUST be overridden by the content class that implements this interface.
        raise NotImplementedError
