class Menu(object):
    """docstring for Menu"""
    def __init__(self):
        super(Menu, self).__init__()
    # create menu items main navigation 
    # items either to create or search
    
    def main(self):
        print('WorkLog')
        print('\n a) Create Entry\n b) Search Entry')

    def submenu(self):
        print(
              '''search options:\n
                 a) search by date
                 b) search by duration of task
                 c) search by string
                 d) search by pattern
              '''
             )