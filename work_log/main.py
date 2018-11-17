import re
import pdb
import collections
from log import WorkLog
from utilities import Utility
from menu import Menu


class Main:

    """
Main class gathers and procecsses user input

methods of Main: userchoice1, user_entry_data, user_search.
instance vaiables: datalist

"""

    def __init__(self):
        super(Main, self).__init__()

    def userchoice1(self):
        """ 
        grabs and validates user choice

        Initialize menu object to display menu items menu1 stores
        user input while loop runs until user provides a valid input 
        based upon input the method calls: either self.user_entry_data method
        or will call an instance of menu.submenu() which is a method of 
        Menu class

        """
         # grab and store user input
        menu = Menu()
        menu.main()
        while True:
            menu1 = input(
                            'please choose weather'
                            'to create option a),or'
                            'search option b) '
                          
                        )
            # tests for a valid resonse
            # if user provides valid response loop will break
            if menu1.lower() not in ('a', 'b'):
                print("Not an appropriate choice.")
            else:
                break
        # based upon user input call method
        if menu1 == 'a':
            self.user_entry_data()
        elif menu1 =='b':
            menu.submenu()
            self.user_search()

    # if create sub 
    def user_entry_data(self):
        """
        user_entry_data collects and processes user data

        user data is collected and stored in date, duration,
        project_name, and 
        """
        datalist = []
        useri = collections.namedtuple(
                                       'useri', ['date','project_name',
                                       'duration','optional_notes'
                                       ])
        a = True
        
        while a:
         #entry date grab input
            while True:
                date =input(
                             'please input a date for' 
                              'the entry in the format mm/dd/yyyy: ' 
                             )
                pattern = re.compile("(\d{2}\/\d{2}\/\d{4})")
                match = pattern.fullmatch(date)
                if not match:
                        print('this is not an appropriate format')
                else:
                    test_date = Utility()
                    date = test_date.date2string(test_date.str2date(date))
                    
                    break
            # entry duration grab input
            while True:
                duration = input(
                                 'please input the duration '
                                 'of the task is minutes: '
                                 
                                )
                durpattern = re.compile("(\d+)")
                durmatch = durpattern.fullmatch(duration)
                
                if not durmatch:
                    print('this is not an appropriate format')
                else:
                    break
                   
            # project name grab input
            project_name = input("please give your project a name: ")
            # optional notes grab input
            optional_notes = input("please add notes(optional):" )


            user_data = useri(date, project_name, duration, optional_notes)
            print(user_data)
            datalist.append(user_data)

            print('\na) create a new entry\nb) return to main menu')
            choice = input('please type your choice')
            if choice == 'a':
                continue
            else:
                try:
                    worklog_initiate = WorkLog()
                    worklog_initiate.logwrite(datalist)
                    # confirmation of entry creation
                    print('\n Thankyou your entry has been created')
                    break
                except ValueError:
                    print('looks like a value couldnt beebs written to file')
                finally:
                    self.mainmenu()
    
    #if search sub navigation(display)
    
    def user_search(self):
        while True:
            #prompt choose search method 
            search_option = input('please choose a search option: ')
            if search_option not in ('a', 'b','c','d'):
                print('this is not an available option')
            else:
                break
        # if date prompt for date get input
        if search_option == 'a':
            
            while True:
                date =input(
                               'please input a date to search '
                               'in the format mm/dd/yyyy: '
                            )
                pattern = re.compile("(\d{2}\/\d{2}\/\d{4})")
                match = pattern.fullmatch(date)
                if not match:
                        print('this is not an appropriate format')
                elif match:
                    utility = Utility()
                    str2date = utility.str2date(date)
                    worklog_initiate = WorkLog()
                    search_results = worklog_initiate.search_by_date(str2date)
                if len(search_results) == 0:
                    print('could not find a matching entry')
                    continue
                else:
                    break
        #if duration prompt for duration get input
        elif search_option =='b':
            while True:
                duration = input(
                                   'please input the duration of the task '
                                   'that you want to search: '
                                )
                durpattern = re.compile("(\d+)")
                durmatch = durpattern.fullmatch(duration)
                
                if not durmatch:
                    print('this is not an appropriate format')
                elif durmatch:
                    utility = Utility()
                    str2time = utility.str2time(duration)
                    worklog_initiate = WorkLog()
                    search_results = worklog_initiate.search_by_duration(str2time)

                if len(search_results) == 0:
                    print('could not find a matching entry')
                    continue
                else:
                    break

        # if string  prompt for string get input
        elif search_option =='c':
            while True:
                string = input(
                                'please types string to we'
                                'will search that against: '
                                )
                worklog_initiate = WorkLog()
                search_results = worklog_initiate.search_by_string(string)
                if len(search_results) == 0:
                    print('could not find a matching entry')
                    continue
                else:
                    break
        # if pattern prompt for pattern get input
        elif search_option == 'd':
            pdb.set_trace()
            while True:
                pattern = input(
                                   'please input your regex'
                                   'pattern here and we will '
                                   'look for matching entries: '
                                )
               
                worklog_initiate = WorkLog()
                search_results = worklog_initiate.search_by_pattern(pattern)
                if len(search_results) == 0:
                    print('could not find a matching entry')
                    continue
                else:
                    break
                    
                

if __name__ == '__main__':
   a = Main()
   a.userchoice1()  
   
