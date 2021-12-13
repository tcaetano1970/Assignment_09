#------------------------------------------#
# Title: IO Classes
# Desc: A Module for IO Classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# TCaetano, 20211210, Modified File - Saved as a Module
#------------------------------------------#
if __name__ == '__main__':
    raise Exception('This file is not meant to ran by itself')

import DataClasses as DC

class FileIO:
    """Processes data to and from file:
properties:
methods:
save_inventory(file_name, lst_Inventory): -> None
load_inventory(file_name): -> (a list of CD objects)
"""
    @staticmethod
    def save_inventory(file_name: str, lst_Inventory: list) -> None:
        """
Args:
file_name (str): name of file that holds the data.
lst_Inventory (list): list of CD objects.
Returns:
None.
"""
        try:
            with open(file_name, 'w') as file:
                for disc in lst_Inventory:
                    file.write(disc.get_record())
        except Exception as e:
            print('There was a general error!', e, e.__doc__, type(e), sep='\n')
    @staticmethod
    def load_inventory(file_name: str) -> list:
        """
Args:
file_name (str): name of file that holds the data.
Returns:
list: list of CD objects.
"""
        lst_Inventory = []
        try:
            with open(file_name, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    row = DC.CD(data[0], data[1], data[2])
                    lst_Inventory.append(row)
        except Exception as e:
            print('There was a general error!', e, e.__doc__, type(e), sep='\n')
            return lst_Inventory

class ScreenIO:
    """Handling Input / Output"""
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user
Args:
None.
Returns:
None.
"""
        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')
    @staticmethod
    def menu_choice():
        """Gets user input for menu selection
Args:
None.
Returns:
choice (string): a lower case sting of the users input out of the choices l, a, i, d, s o
r x
"""
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print() # Add extra space for layout
        return choice
    @staticmethod
    def show_inventory(table):
        """Displays current inventory table
Args:
table (list of dict): 2D data structure (list of dicts) that holds the data during
runtime.
Returns:
None.
    """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print(row)
        print('======================================')
    @staticmethod
    def get_CD_info():
        """function to request CD information from User to add CD to inventory
Returns:
cdId (string): Holds the ID of the CD dataset.
cdTitle (string): Holds the title of the CD.
cdArtist (string): Holds the artist of the CD.
"""
        cdId = input('Enter ID: ').strip()
        cdTitle = input('What is the CD\'s title? ').strip()
        cdArtist = input('What is the Artist\'s name? ').strip()
        return cdId, cdTitle, cdArtist