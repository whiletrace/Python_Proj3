import csv
import collections


class WorkLog(object):
    """docstring for WorkLog"""
    def __init__(self, csv_file = None):
        super(WorkLog, self).__init__()
        
    # Work log will be an aggragate of indivual entries
        # work log has entries

    # work log will write entries to a csv file.
    def logwrite(self, *args):

        with open('entries.csv', 'a', newline = '') as csvfile:
            # create an entry from user input(Menu)e
            fieldnames =['date', 'project_name', 'duration', 'optional_notes']
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
            writer.writeheader()
            writer.writerow({'date': date,'project_name':project_name,
                                'duration': duration, 'optional_notes':
                                 optional_notes })
            
    
        # create an entry from user input(Menu)
        # from user input create a dict 
        # create a write file 
        # write to csv file from key falue pairs in dict 

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
date = '11/22/2018'
project_name = 'project1'
duration = '346'
optional_notes = 'these are optional notes'
a = WorkLog()
a.logwrite(date, project_name, duration, optional_notes)
a.logread('entries.csv')

