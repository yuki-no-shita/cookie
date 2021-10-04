import driver
import store
import entry_parser
import sys
from os.path import exists

if __name__ == "__main__":
    cookie_finder = driver.Driver(store.Store(), entry_parser.Entry_Parser())
    target_file_path = sys.argv[1]
    target_date = sys.argv[3]

    if not exists(target_file_path):
        raise FileNotFoundError

    target_file = open(target_file_path)
    
    print(*cookie_finder.process_file(target_file, target_date), sep = "\n")