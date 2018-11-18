class Menu(object):

    """Menu class displays menu items moethods are main and submenu"""
    
    def __init__(self):
        super(Menu, self).__init__()
    
    def main(self):
        """ create menu items main navigation"""
        print('WorkLog')
        print('\n a) Create Entry\n b) Search Entry')

    def submenu(self):
        """ create menu items for search entries"""
        print(
              '''search options:\n
                 a) search by date
                 b) search by duration of task
                 c) search by string
                 d) search by pattern
              '''
             )