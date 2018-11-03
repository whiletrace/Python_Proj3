import csv
import collections
import re
import pdb
from datetime import datetime, timedelta
from entry import Entry


class WorkLog(object):
    """docstring for WorkLog"""
    def __init__(self, csv_file = None):
        super(WorkLog, self).__init__()
        # self.logwriter = self.logwrite()
        self.logreader = self.logread(csv_file)
    # Work log will be an aggragate of indivual entries
        # work log has entries

    # work log will write entries to a csv file.
    def logwrite(self, *args):
        # create a write file 
        with open('entries.csv', 'a', newline = '') as csvfile:
            # create an entry from user input(Menu)
            fieldnames =['date', 'project_name', 'duration', 'optional_notes']
            # from user input create a dict
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
            writer.writeheader()
            # write to csv file from key falue pairs in dict
            # from user input create a dict
            writer.writerow({'date': date,'project_name':project_name,
                                'duration': duration, 'optional_notes':
                                 optional_notes })
    
    # convert string to datetime object
    def str2date(self, string):
        #test strint against pattern
        dpattern = re.compile("(\d{2}\/\d{2}\/\d{4})")
        durpattern = re.compile("(\d+)")
        dmatch = dpattern.fullmatch(string)
        durmatch = durpattern.fullmatch(string)
        
        #if string matches mm/dd/yyyy
        if dmatch:
            #try string
            try:
                # String to datetime:
                d = datetime.strptime(string, '%m/%d/%Y')
                return d
            # except if string does not match valid date:
            except ValueError:
                # message this does not seem to be a valid date or date not
                print('This is not a valid date')
        # if string not match dpattern will try to match durpattern
        elif durmatch:
            # if match will convert string to datetime.timedelta
            try:
                dur = timedelta(minutes= int(string))
                return dur
            except ValueError:
                print('this is not the requested whatever')
        
    # Date time to string: 
    # convert datetime object to string
    # return string

    # work log will read files from csv file
    # context manager design pattern
    def logread(self,csv_file):
        with open('entries.csv', newline = '') as csvfile:
            fieldnames =['date', 'project_name', 'duration', 'optional_notes']
            reader = csv.DictReader(csvfile, fieldnames = fieldnames)
            # be able to iterate over entry from file
            for row in reader:
                for key, value in row.items():
                    if key == 'date' or key == 'duration':
                        # convert to datetime for search and pattern matching
                        row[key] = self.str2date(value)
            
            # from csv file create entry objects
            entries = [Entry(**row)]
            # tests to see if string -> datetime and timedelta has 
            # occured and is stored within objects attr
            for entry in entries:
                print(getattr(entry,'duration'))
            # output entries 
            return entries

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
        

