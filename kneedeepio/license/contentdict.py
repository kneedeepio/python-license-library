#!/usr/bin/env python3

### IMPORTS ###
from kneedeepio.license.contentbase import ContentBase

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class ContentDict(ContentBase):
    _content: dict

    def __init__(self):
        self._content = {}

    @property
    def content(self):
        # FIXME: Should this raise an empty (No Content) exception?
        return self._content

    @content.setter
    def content(self, value):
        if not isinstance(value, dict):
            raise TypeError
        self._content = value

    def set_content_from_license(self, value):
        self.content = value

    def get_content_for_license(self):
        return self.content
