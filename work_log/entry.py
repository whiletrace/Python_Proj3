

class Entry(object):
    """docstring for Entry"""
    def __init__(self, **kwargs):
        
        for key, value in kwargs.items():
            setattr(self, key, value)
    # Will be single log entry
        # will have a date
        # will have a duration
        # will have a project name
        # will have option notes
    pass