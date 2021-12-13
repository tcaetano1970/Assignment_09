#------------------------------------------#
# Title: Data Classes
# Desc: A Module for Data Classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# TCaetano, 20211210, Modified File - Saved as a Module
#------------------------------------------#
if __name__ == '__main__':
    raise Exception('This file is not meant to ran by itself')

class CD:
        """Stores data about a CD:
            properties:
                cd_id: (int) with CD ID
                cd_title: (string) with the title of the CD
                cd_artist: (string) with the artist of the CD
                methods:
                    get_record() -> (str):
    """
# -- Constructor -- #
        def __init__(self, cd_id: int, cd_title: str, cd_artist: str) -> None:
            """Set ID, Title and Artist of a new CD Object"""
# -- Attributes -- #
            try:
                self.__cd_id = int(cd_id)
                self.__cd_title = str(cd_title)
                self.__cd_artist = str(cd_artist)
            except Exception as e:
                raise Exception('Error setting initial values:\n' + str(e))
# -- Properties -- #
# CD ID
        @property
        def cd_id(self):
            return self.__cd_id
        @cd_id.setter
        def cd_id(self, value):
            try:
                self.__cd_id = int(value)
            except Exception:
                    raise Exception('ID needs to be Integer')
# CD title
        @property
        def cd_title(self):
            return self.__cd_title
        @cd_title.setter
        def cd_title(self, value):
            try:
                self.__cd_title = str(value)
            except Exception:
                    raise Exception('Title needs to be String!')
# CD artist
        @property
        def cd_artist(self):
            return self.__cd_artist
        @cd_artist.setter
        def cd_artist(self, value):
            try:
                self.__cd_artist = str(value)
            except Exception:
                    raise Exception('Artist needs to be String!')
# TODone Add Code to the CD class
        def __str__(self):
            """Returns: CD details as formatted string"""
            return '{:>2}\t{} (by: {})'.format(self.cd_id, self.cd_title, self.cd_artist)
        def get_record(self):
            """Returns: CD record formatted for saving to file"""
            return '{},{},{}\n'.format(self.cd_id, self.cd_title, self.cd_artist)