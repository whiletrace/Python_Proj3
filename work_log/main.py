import re
import pdb
import collections

class Menu:
    """docstring for Menu"""
    def __init__(self):
        super(Menu, self).__init__()
        
        

    def mainmenu(self):
    # create menu items main navigation 2 items either to create or search 
    
        print('WorkLog')
        print('\n a) Create Entry\n b) Search Entry')
        # grab and store user input
        while True:
            menu1 = input("please choose weather to create option a),or serarch option b)" )
            if menu1.lower() not in ('a', 'b'):
                print("Not an appropriate choice.")
            else:
                break
        if menu1 == 'a':
            self.submenu1()
                
                
        print(menu1)
    # if create sub 
    def submenu1(self):
        pdb.set_trace()
        datalist =[]
        useri = collections.namedtuple('useri', ['date','project_name','duration','optional_notes'])
        a = True
        
        while a:
         #entry date grab input
            while True:
                date =input("please input a date for the entry in the format mm/dd/yyyy: ")
                pattern = re.compile("(\d{2}\/\d{2}\/\d{4})")
                match = pattern.fullmatch(date)
                if not match:
                        print('this is not an appropriate format')
                else:
                     break
            # entry duration grab input
            while True:
                duration = input("please input the duration of the task is minutes: ")
                durpattern = re.compile("(\d+)")
                durmatch = durpattern.fullmatch(duration)
                
                if not durmatch:
                    print('this is not an appropriate format')
                else:
                    break
                   

            project_name = input("please give your project a name: ")
            optional_notes = input("please add notes(optional):" )
            print('\n Thankyou your entry has been created')
            user_data = useri(date, project_name, duration, optional_notes)
            datalist.append(user_data)
            print('\na) create a new entry\nb) return to main menu')
            choice = input('please type your choice')
            if choice == 'a':
                continue
            else:
                return datalist
        
    def return_to_main(self):
         self.mainmenu()

           


        
        

    
    
        

        

        






            
        
        # project name grab input
        # optional notes grab input
        # confirmation of entry creation

    #if search sub navigation(display)
        # menu item search date
        # menu item search duration
        # menu item search by string
        # menu item search by pattern

        #prompt choose search method 
            # get user input
                # if date prompt for date get input
                #if duration prompt for duration get input
                # if string  prompt for string get input
                # if pattern prompt for pattern get input
       
a = Menu()
a.mainmenu()

a.return_to_main()