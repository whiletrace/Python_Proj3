import csv
import collections
import re
import pdb
from datetime import datetime, timedelta
from entry import Entry
from utilities import Utility



class WorkLog(object):
    """docstring for WorkLog"""
    def __init__(self, csv_file = None):
        super(WorkLog, self).__init__()
        self.entries = self.logread(csv_file)
        
        
    # Work log will be an aggragate of indivual entries
        # work log has entries

    # work log will write entries to a csv file.
    def logwrite(self, input):
        # create a write file 
        print(input)
        
        with open('entries.csv', 'a', newline = '') as csvfile:
            # create an entry from user input(Menu)
            fieldnames =['date','project_name','duration','optional_notes']
            
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
            
            for entry in input:
                writer.writerow(entry._asdict())
                
                
            




            
                
    
    # convert string to datetime object
    
        
    # Date time to string: 
    # convert datetime object to string
    # return string

    # work log will read files from csv file
    # context manager design pattern
    def logread(self,csv_file):
        
        entries = []
        with open('entries.csv', newline = '') as csvfile:
            fieldnames =['date', 'project_name', 'duration', 'optional_notes']
            reader = csv.DictReader(csvfile, fieldnames = fieldnames)
            # be able to iterate over entry from filefile = open('entries.csv')
            file = open('entries.csv')
            utility = Utility()
            
            for row in reader:
                for key, value in row.items():
                    if key == 'date':
                        # convert to datetime for search and pattern matching
                        row[key] = utility.str2date(value)
                    elif key == 'duration':
                        row[key] = utility.str2time(value)
            
                # from csv file create entry objects
                #print(row)
                entries.append(Entry(**row))
                # tests to see if string -> datetime and timedelta has 
                # occured and is stored within objects attr
                
               
            # output entries 
        print(entries)
        return entries

    
        
    def search_by_date(self, obj):
        results = []
        utility = Utility()
        # iterate through all entries
        
        for entry in self.entries:
        # if entries match user given date
            if obj == getattr(entry,'date'):
                results.append(entry)
        # return all entries that match the date
        for entry in results[:]:
            setattr(entry, 'date', utility.date2string(getattr(entry,'date')))
            print(entry)
                
            
                
        # return all entries that match the date

    # search by duration:
    def search_by_duration(self, obj):
        results = []
        utility = Utility()
        
        # iterate through all entries
        for entry in self.entries:
        # if entries match user given date
            if obj == getattr(entry,'duration'):
                results.append(entry)
        # return all entries that match the date
        for entry in results[:]:
            setattr(entry, 'date', utility.date2string(getattr(entry,'date')))
            print(entry)
        
        # if entries match user given duration of time 
        # return all entries that match

    # search by exact string:
    def search_by_string(self,string):
        results =[]
        # iterate through all entries
        for entry in self.entries:
            # if string is present in the entry
            if string in entry.project_name or string in entry.optional_notes:
                results.append(entry)
                print(entry)
        
        # return all entries that match

    # search by pattern:
        #iterate through entries
        # if entry matches a regex pattern 
        # return all relevant entries
        



