import unittest
import entry_parser

class TestEntryParserMethods(unittest.TestCase):
    def initialize(self):
        return entry_parser.Entry_Parser()

    def test_parse(self):
        test_parser = self.initialize()
        self.assertEqual(test_parser.parse_entry("AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00"), ("2018-12-09", "AtY0laUfhglK3lC7", "14:19:00+00:00"))
        
    def test_parse_bad_input(self):
        test_parser = self.initialize()
        self.assertEqual(test_parser.parse_entry(None), None)

    def test_parse_bad_input_two(self):
        test_parser = self.initialize()
        with self.assertRaises(ValueError):
            test_parser.parse_entry("T")
        

if __name__ == '__main__':
    unittest.main()