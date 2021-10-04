import unittest
from unittest.mock import Mock, MagicMock, patch, mock_open
import driver
import store
import entry_parser

class TestDriverMethods(unittest.TestCase):
    def initialize(self):
        return driver.Driver(self.storage_mock, self.parser_mock)

    def setUp(self):
        self.storage_mock = Mock()
        self.parser_mock = Mock()

        def mock_parse(entry):
            return entry_parser.Entry_Parser.parse_entry(None, entry)
        self.parser_mock.parse_entry = mock_parse

    def test_storage_calls(self):
        test_driver = self.initialize()
        def test():
            return l
        l = []
        l.append("AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00")
        l.append("AtY0laUfhglK3lC7,2018-12-09T14:20:00+00:00")
        mock_file = MagicMock(readlines = test)
        s = test_driver.process_file(mock_file, "2018-12-09")
        self.assertEqual(self.storage_mock.store.call_count, 2)

    '''
    defined parse_entry in line 15 so cannot 
    test number of times parse_entry was called
    '''

if __name__ == '__main__':
    unittest.main()