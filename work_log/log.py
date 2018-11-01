import csv
import collections
import re
import pdb
from datetime import datetime


class WorkLog(object):
    """docstring for WorkLog"""
    def __init__(self, csv_file = None):
        super(WorkLog, self).__init__()
        
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
        #if string matches mm/dd/yyyy
        pattern = re.compile("(\d{2}\/\d{2}\/\d{4})")
        match = pattern.fullmatch(string)
        pdb.set_trace()
        if match:
            #try string
            try:
                # String to datetime:
                
                d = datetime.strptime(string, '%m/%d/%Y')

                print(d)

            except ValueError:
                print('This is not a valid date')
                
        else:
            print('sorry dude this needs help')
        
            
                # yield object
        # except if string does not match valid date:
            # value error
                # message this does not seem to be a valid date or date not
                # formatted properly please type a date
        
        
    # Date time to string:
    # convert datetime object to string
    # return string

    # work log will read files from csv file
    def logread(self,csv_file):
        with open('entries.csv', newline = '') as csvfile:
            fieldnames =['date', 'project_name', 'duration', 'optional_notes']
            reader = csv.DictReader(csvfile, fieldnames = fieldnames)
            for row in reader:
                print(row['date'], row['project_name'])
        # context manager design pattern
        # from csv file create entry objects
        # convert to datetime for search and pattern matching operations
        # be able to iterate over entry from file
        # output entries 

   

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
date = '11/22/2018'
project_name = 'project1'
duration = '346'
optional_notes = 'these are optional notes'
a = WorkLog()
a.logwrite(date, project_name, duration, optional_notes)
# a.logread('entries.csv')
a.str2date('15/12/1999')

a.str2date('12/boogabooga/1990')

