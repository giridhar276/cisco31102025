




import os
import sys
import shutil

# Define a class
class FileManager:
    def __init__(self, source_path, destination_path):
        self.source_path = source_path  # instance variable
        self.destination_path = destination_path  # instance variable

    def display_paths(self):
        """Display source and destination paths"""
        print(f"Source Path: {self.source_path}")
        print(f"Destination Path: {self.destination_path}")

    def copy_file(self):
        """Copy file from source to destination"""
        try:
            shutil.copy(self.source_path, self.destination_path)
            print(f"File copied successfully from {self.source_path} to {self.destination_path}")
        except FileNotFoundError:
            print(f"Error: Source file not found - {self.source_path}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


# Example usage
if __name__ == "__main__":
    # Create objects (instances)
    file1 = FileManager("sample.txt", "source")
    #file2 = FileManager("sample.txt", "destination")

    # Access methods
    file1.display_paths()
    file1.copy_file()

    print()