# file operations
class FileIO:

    file_location = ' '

    def __init__(self, file_location):
        self.file_location = file_location

    def open(self, write_mode):
        if write_mode == True:
            with open(self.file_location, 'w') as file_object:
                return file_object
        else:
            with open(self.file_location) as file_object:
                return file_object


print('loaded the program ')
hello = FileIO('/Users/srividhya/Downloads/firstTimePass')
hello.open(True)