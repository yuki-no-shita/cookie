import store
import entry_parser
from os.path import exists

class Driver():
    def __init__(self, store_object, parse_object):
        self.storage = store_object
        self.entry_parser = parse_object

    def __get_max_cookie(self, date):
        return self.storage.get_most_freq_cookie_on_date(date)

    def process_file(self, target_file, target_date):
        
        self.storage.reset_store()            
        for line in target_file.readlines():
            date, cookie, time = self.entry_parser.parse_entry(line)
            self.storage.store(date, cookie, time)

        return self.__get_max_cookie(target_date)


        

    