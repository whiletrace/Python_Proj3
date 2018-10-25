
class WorkLog(object):
    """docstring for WorkLog"""
    def __init__(self, arg):
        super(WorkLog, self).__init__()
        self.arg = arg

    # Work log will be an aggragate of indivual entries
        # work log has entries

    # work log will write entries to a csv file.
        # create an entry from user input(Menu)
        # from user input create a dict 
        # create a write file 
        # write to csv file from key falue pairs in dict 

    # work log will read files from csv file 
        # context manager design pattern
        # from csv file create entry objects
        # convert to datetime for search and pattern matching operations
        # be able to iterate over entry from file
        # output entries 

    # Date time to string:
        # convert datetime object to string
        # return string

    # String to datetime:
         # convert string to datetime object
         # return object 
        
    # search by date:
        # iterate through all entries
        # if entries match user given date
        # return all entries that match the date

    # search by duration:
        # iterate through all entries
        # if entries match user given duration of time 
        # return all entries that match

    # search by exact string:
        # iterate through all entries
        # if string is present in the entry
        # return all entries that match

    # search by pattern:
        #iterate through entries
        # if entry matches a regex pattern 
        # return all relevant entries
        pass