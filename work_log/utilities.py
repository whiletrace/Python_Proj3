from datetime import datetime
from datetime import timedelta
import pdb

class Utility:
    """docstring for Utility"""
   
    def str2date(self, string):
        
        while True:
            try:
                # String to datetime:
                string_to_date = datetime.strptime(string, '%m/%d/%Y')
                return string_to_date
                break
            # except if string does not match valid date:
            except ValueError:
                print('This is not a valid date')
                string = input("please input a valid date: ")
                try:
                 # message this does not seem to be a valid date or date not
                    string_to_date = datetime.strptime(string, '%m/%d/%Y')
                    return string_to_date
                    break
                except ValueError:
                        continue

    def str2time(self, string):
        
        while True:
            try:
                # String to datetime:
                minutes_to_duration = timedelta(minutes = int(string))
                return minutes_to_duration
                break
            # except if string does not match valid date:
            except ValueError:
                print('This is not a valid duration')
                string = input("please input a numberstring ")
                try:
                 # message this does not seem to be a valid date or date not
                    minutes_to_duration = datetime.strptime(string,'%H/%M')
                    return minutes_to_duration
                    break
                except ValueError:
                        continue

    # String to datetime:
         # convert string to datetime object
         # return object 
    def date2string(self, dateobject):
        datestring = dateobject.strftime('%m/%d/%Y')
        return datestring








