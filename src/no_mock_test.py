from app import rm
import os


def delete_check(filename):
    
    if os.path.isfile(filename):
        os.remove(filename)
        return f"{filename} has been successfully removed."
    else:
        raise FileNotFoundError(f"'{filename}' doesn't exist")
    


