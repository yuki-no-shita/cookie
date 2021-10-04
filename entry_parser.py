class Entry_Parser():
    def parse_entry(self, entry):
        if not entry:
            return None
        try:
            cookie, date_time = entry.split(",")
            date, time = date_time.split("T")
            return (date, cookie, time)
        except:
            raise ValueError("Improperly formatted input: " + entry)
        
    