
from utilities import Utility

def datestring(obj):
    utility = Utility()
    utility.date2string(obj)

class Entry(object):
    """docstring for Entry"""
    def __init__(self, **kwargs):
        # Will be single log entry
        # will have a date
        # will have a duration
        # will have a project name
        # will have option notes
        
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def __str__(self):
        return "date: {}\nproject: {}\nduration: {}\nnotes: {}".format(
                                     self.date, self.project_name, self.duration, 
                                     self.optional_notes
                                    )
