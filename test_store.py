import unittest
import store

class TestStoreMethods(unittest.TestCase):
    def initialize(self):
        return store.Store()

    def test_test(self):
        test_store = self.initialize()

    def test_store_one_item(self):
        test_store = self.initialize()
        test_store.store("2018-12-09", "AtY0laUfhglK3lC7", "14:19:00+00:00")
        self.assertEqual(test_store.get_cookie_dates("2018-12-09"), [("AtY0laUfhglK3lC7", "14:19:00+00:00")])
    
    def test_store_dne(self):
        test_store = self.initialize()
        test_store.store("2018-12-09", "AtY0laUfhglK3lC7", "14:19:00+00:00")
        self.assertEqual(test_store.get_cookie_dates("2018-12-10"), [])
   
    def test_store_most_frequent_one(self):
        test_store = self.initialize()
        test_store.store("2018-12-09", "a", "14:19:00+00:00")
        test_store.store("2018-12-09", "a", "14:20:00+00:00")
        test_store.store("2018-12-09", "b", "14:19:00+00:00")
        self.assertEqual(test_store.get_most_freq_cookie_on_date("2018-12-09"), ["a"])

    def test_store_most_frequent_multiple(self):
        test_store = self.initialize()
        test_store.store("2018-12-09", "a", "14:19:00+00:00")
        test_store.store("2018-12-09", "a", "14:20:00+00:00")
        test_store.store("2018-12-09", "b", "14:19:00+00:00")
        test_store.store("2018-12-09", "b", "14:20:00+00:00")
        self.assertEqual(test_store.get_most_freq_cookie_on_date("2018-12-09"), ["a", "b"])

    def test_store_most_frequent_b(self):
        test_store = self.initialize()
        test_store.store("2018-12-09", "a", "14:19:00+00:00")
        test_store.store("2018-12-09", "a", "14:20:00+00:00")
        test_store.store("2018-12-09", "b", "14:19:00+00:00")
        test_store.store("2018-12-09", "b", "14:20:00+00:00")
        test_store.store("2018-12-09", "b", "14:21:00+00:00")
        self.assertEqual(test_store.get_most_freq_cookie_on_date("2018-12-09"), ["b"])

    def test_store_most_frequent_dne_date(self):
        test_store = self.initialize()
        test_store.store("2018-12-09", "a", "14:19:00+00:00")
        test_store.store("2018-12-09", "a", "14:20:00+00:00")
        test_store.store("2018-12-09", "b", "14:19:00+00:00")
        test_store.store("2018-12-09", "b", "14:20:00+00:00")
        test_store.store("2018-12-09", "b", "14:21:00+00:00")
        self.assertEqual(test_store.get_most_freq_cookie_on_date("2018-12-10"), [])

    def test_reset(self):
        test_store = self.initialize()
        test_store.store("2018-12-09", "a", "14:19:00+00:00")
        test_store.store("2018-12-09", "a", "14:20:00+00:00")  
        test_store.reset_store()
        self.assertEqual(test_store.cookie_dates, {})
        
    def test_large(self):
        test_store = self.initialize()
        test_store.store("2018-12-09", "AtY0laUfhglK3lC7", "14:19:00+00:00")
        test_store.store("2018-12-09", "SAZuXPGUrfbcn5UA", "10:13:00+00:00")
        test_store.store("2018-12-09", "5UAVanZf6UtGyKVS", "07:25:00+00:00")
        test_store.store("2018-12-09", "AtY0laUfhglK3lC7", "06:19:00+00:00")
        test_store.store("2018-12-08", "SAZuXPGUrfbcn5UA", "22:03:00+00:00")
        test_store.store("2018-12-08", "4sMM2LxV07bPJzwf", "21:30:00+00:00")
        test_store.store("2018-12-08", "fbcn5UAVanZf6UtG", "09:30:00+00:00")
        test_store.store("2018-12-07", "4sMM2LxV07bPJzwf", "23:30:00+00:00")
        self.assertEqual(test_store.get_most_freq_cookie_on_date("2018-12-09"), ["AtY0laUfhglK3lC7"])

if __name__ == '__main__':
    unittest.main()