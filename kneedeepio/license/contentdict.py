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

    def __eq__(self, other):
        if not isinstance(other, ContentDict):
            return NotImplemented
        return self.content == other.content

    @property
    def content(self):
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
