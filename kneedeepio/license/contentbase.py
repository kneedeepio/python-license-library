#!/usr/bin/env python3

### IMPORTS ###

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class ContentBase:
    def set_content_from_license(self, config):
        # The config is supplied from the license object to this object to instantiate (aka load) the contents of the
        # license into this class.
        # NOTE: This MUST be overridden by the config class that implements this interface.
        raise NotImplementedError

    def get_content_for_license(self):
        # The config is returned from this method to the license object to be included in the license.
        # NOTE: This MUST be overridden by the config class that implements this interface.
        raise NotImplementedError
