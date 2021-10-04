import collections

class Store():
    def __init__(self):
        self.cookie_dates = {}

    def store(self, date, cookie, time):
        if date not in self.cookie_dates:
            self.cookie_dates[date] = []
        self.cookie_dates[date].append((cookie, time)) #set?

    def get_cookie_dates(self, date):
        return self.cookie_dates[date] if date in self.cookie_dates else []
    
    def get_most_freq_cookie_on_date(self, date):
        if date not in self.cookie_dates or len(self.cookie_dates[date]) == 0:
            return []
        date_list = self.cookie_dates[date]
        cookie_count = {}
        most_frequent_cookies = []
        curr_max = 0

        for cookie, time in date_list:
            if cookie not in cookie_count:
                cookie_count[cookie] = 0
            cookie_count[cookie] += 1

            if cookie_count[cookie] > curr_max:
                curr_max = cookie_count[cookie]
                most_frequent_cookies = []
                most_frequent_cookies.append(cookie)
            elif cookie_count[cookie] == curr_max:
                most_frequent_cookies.append(cookie)

        return most_frequent_cookies
    
    def reset_store(self):
        self.cookie_dates = {}

    


        