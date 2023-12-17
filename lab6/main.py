import os
import time


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time of {func.__name__}: {execution_time:.6f} seconds")
        return result

    return wrapper


class CommandPrompt:
    def __init__(self, current_directory='.'):
        self.current_directory = os.path.abspath(current_directory)

    @timing_decorator
    def pwd(self):
        print(f"Current directory: {self.current_directory}")

    @timing_decorator
    def ls(self):
        try:
            files = os.listdir(self.current_directory)
            print("Files in the current directory:")
            for file in files:
                print(file)
        except Exception as e:
            print(f"Exception: {e}")

    @timing_decorator
    def cd(self, new_directory):
        try:
            os.chdir(new_directory)
            self.current_directory = os.getcwd()
        except FileNotFoundError:
            print("Exception: Directory not found.")
        except Exception as e:
            print(f"Exception: {e}")

    @timing_decorator
    def mkdir(self, directory_name):
        try:
            os.mkdir(directory_name)
            print(f"Created directory: {directory_name}")
        except FileExistsError:
            print(f"Exception: Directory {directory_name} already exists.")
        except Exception as e:
            print(f"Exception: {e}")

    @timing_decorator
    def rmdir(self, directory_name):
        try:
            os.rmdir(directory_name)
            print(f"Removed directory: {directory_name}")
        except FileNotFoundError:
            print(f"Exception: Directory {directory_name} not found.")
        except Exception as e:
            print(f"Exception: {e}")

    @timing_decorator
    def mv(self, old_name, new_name):
        try:
            os.rename(old_name, new_name)
            print(f"Renamed: {old_name} -> {new_name}")
        except FileNotFoundError:
            print(f"Exception: File/directory {old_name} not found.")
        except Exception as e:
            print(f"Exception: {e}")

    @timing_decorator
    def touch(self, file_name):
        try:
            with open(file_name, 'w') as file:
                file.write("Sample text")
            print(f"Created file: {file_name}")
        except Exception as e:
            print(f"Exception: {e}")

    @timing_decorator
    def rm(self, file_name):
        try:
            os.remove(file_name)
            print(f"Removed file: {file_name}")
        except FileNotFoundError:
            print(f"Exception: File {file_name} not found.")
        except Exception as e:
            print(f"Exception: {e}")

    @timing_decorator
    def view_files(self, extension):
        try:
            matching_files = [file for file in os.listdir(self.current_directory) if file.endswith(extension)]
            print(f"Files with extension .{extension}:")
            for file in matching_files:
                with open(file, 'r') as f:
                    content = f.read()
                    print(f"\nContents of {file}:\n{content}")
        except Exception as e:
            print(f"Exception: {e}")

    def exit(self):
        print("Exiting Command Prompt")
        exit()


def interactive_unix_shell(cmd):
    while True:
        user_input = input(f"{cmd.current_directory}$ ")
        try:
            command, *args = user_input.split()
            if hasattr(cmd, command):
                getattr(cmd, command)(*args)
            else:
                print("Invalid input. Please enter a valid choice.")
        except Exception as e:
            print(f"Exception: {e}")


if __name__ == "__main__":
    cmd = CommandPrompt()
    interactive_unix_shell(cmd)
