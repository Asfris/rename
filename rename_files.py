# Rename all files in specific folder
import sys
import os
import shutil


class Arg:
    # Creates Arg object
    def __init__(self) -> None:
        self.args = sys.argv

    def args_length_check(self, min_len: int) -> bool:
        if len(self.args) <= min_len:
            return False

        return True


class Main (Arg):
    # Creates Main object
    # Has limit length for args
    def __init__(self) -> None:
        Arg.__init__(self)

        if self.args_length_check(3) == False:
            print("Recived args lenght is not correct!")
            exit()

    def get_first_arg(self) -> str:
        return self.args[1]

    def get_second_arg(self) -> str:
        return self.args[2]

    def get_new_files_name(self) -> str:
        return self.args[3]
    
    def get_files_sorted(self, folder: str) -> list[str]:
        files = os.listdir(folder)
        files.sort()

        return files

    def copy_folder_files(self, target_folder: str, new_folder: str) -> None:
        files = self.get_files_sorted(target_folder)
        index: int = 1

        # Check if new_folder is exist
        if not os.path.exists(new_folder):
            print("Target older is not exist. Creating.")
            #Create folder
            try:
                os.makedirs(new_folder)
            except:
                print("Cant create target folder!")


        new_files_name = self.get_new_files_name()
        for file in files:
            extention = os.path.splitext(file)[1]
            newName = new_folder+"/" + \
                new_files_name+str(index)+extention
            shutil.copy(target_folder+"/"+file, newName)

            index += 1

    # RUNS app
    def run(self) -> None:
        # start copy folder files to a new folder (with rename)
        first_folder = os.path.abspath(self.get_first_arg())
        second_folder = os.path.abspath(self.get_second_arg())

        self.copy_folder_files(first_folder, second_folder)


if __name__ == "__main__":
    main = Main()
    main.run()
