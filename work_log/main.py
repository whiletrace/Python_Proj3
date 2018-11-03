import re

class Menu:
    """docstring for Menu"""
    def __init__(self):
        super(Menu, self).__init__()
        

    def mainmenu(self):
    # create menu items main navigation 2 items either to create or search 
    
        print('WorkLog')
        print('\n a) Create Entry\n b) Search Entry')
        # grab and store user input
        menu1 = input('please choose weather to create option a) or serarch option b) ')
    # if create sub navigation
        #entry date grab input
        '''pattern = re.compile("(\d{2}\/\d{2}\/\d{4})")
        match = pattern.fullmatch(string)
        if match:
            print('whoo hoo this is a match')
        else:
            print('sorry dude this needs help')
            '''
        # entry duration grab input
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