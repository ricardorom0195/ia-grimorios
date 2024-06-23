"""CUSTOM ERROrS."""

class SQLException(Exception):
    """SQL EXCEPTION"""
    def __init__(self, message = "An error ocurred with sql conecction"):
        self.message = message
        Exception.__init__(self, message)
