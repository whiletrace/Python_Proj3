import csv
import collections
import re
import pdb
from datetime import datetime, timedelta
from entry import Entry
from utilities import Utility



class WorkLog(object):
    """WorkLog executes writing and reading entry to file 
    
    methods are: logwrite, logread, search_by_date, search_by_string
    search_by_pattern class variable self.entries which is a call 
    to logread method instance variables: entries
    """
    def __init__(self, csv_file = None):
        super(WorkLog, self).__init__()
        self.entries = self.logread(csv_file)
        

    def logwrite(self, input):
        """executes the writing of user input to csv file

            consumes instance varibles: useri, datalist from 
            which is passed to method as input argument
        """
        
        # create a write file
        with open('entries.csv', 'a', newline = '') as csvfile:
            # create an entry from user input(Menu)
            fieldnames =['date','project_name','duration','optional_notes']
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
            
            for entry in input:
                #conversion of named tuple to ordered dict
                writer.writerow(entry._asdict())
                


    def logread(self,csv_file):
        """logread reads in data from csv file creates entry objects"""
       
        # empty list
        entries = []
        # context manager pattern for 
        with open('entries.csv', newline = '') as csvfile:
            fieldnames =['date', 'project_name', 'duration', 'optional_notes']
            reader = csv.DictReader(csvfile, fieldnames = fieldnames)
            # be able to iterate over entry from filefile = open('entries.csv')
            file = open('entries.csv')
            utility = Utility()
            # converts key date and key:duration values to datetime/timedelta
            for row in reader:
                for key, value in row.items():
                    if key == 'date':
                        # convert to datetime for search and pattern matching
                        row[key] = utility.str2date(value)
                    elif key == 'duration':
                        row[key] = utility.str2time(value)
            
                # from csv file create entry objects append to list entries
                entries.append(Entry(**row))
        
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
                
        return results
                
   

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
        
        return results

    # search by exact string:
    def search_by_string(self,string):
        results =[]
        # iterate through all entries
        for entry in self.entries:
            # if string is present in the entry
            if string in entry.project_name or string in entry.optional_notes:
                results.append(entry)
                print(entry)
        for entry in results[:]:
            setattr(entry, 'date', utility.date2string(getattr(entry,'date')))
            print(entry)

        return results
        
        # return all entries that match

    # search by pattern:
    def search_by_pattern(self,user_input):
        pdb.set_trace()
        results = []
        pattern = re.compile(user_input)

        #iterate through entries
        for entry in self.entries:
            match = pattern.search(entry.project_name or entry.optional_notes)
            # if entry matches a regex pattern 
            if match:
                # return all relevant entries
                results.append(entry)
        for entry in results[:]:
            setattr(entry, 'date', utility.date2string(getattr(entry,'date')))
            print(entry)
        return results



