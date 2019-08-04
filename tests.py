import wpp_parser
import unittest
import datetime


class TestDate(unittest.TestCase):
    date1 = "[2/2/18, 5:32:54 PM]"
    date2 = "[12/20/18, 5:32:54 PM]"
    date3 = "[2/20/18, 5:32:54 PM]"
    date4 = "[12/2/18, 5:32:54 AM]"
    date5 = "[2/2/18, 12:00:00 PM]"
    date6 = "[2/2/18, 12:00:00 AM]"
    date7 = "[2/20/18, 2:00:00 AM]"

    def test_date(self):
        p = wpp_parser.WppParser("")
        self.assertEqual(p.getDate("[2/2/18, 5:32:54 PM]"),
                         datetime.datetime(2018, 2, 2, 17, 32, 54),
                         "test 1 failed.")
        self.assertEqual(p.getDate("[12/20/18, 5:32:54 PM]"),
                         datetime.datetime(2018, 12, 20, 17, 32, 54),
                         "test 2 failed.")
        self.assertEqual(p.getDate("[2/20/18, 5:32:54 PM]"),
                         datetime.datetime(2018, 2, 20, 17, 32, 54),
                         "test 3 failed.")
        self.assertEqual(p.getDate("[12/2/18, 5:32:54 AM]"),
                         datetime.datetime(2018, 12, 2, 5, 32, 54),
                         "test 4 failed.")
        self.assertEqual(p.getDate("[2/2/18, 12:00:00 PM]"),
                         datetime.datetime(2018, 2, 2, 12, 0, 0),
                         "test 5 failed.")
        self.assertEqual(p.getDate("[2/2/18, 12:00:00 AM]"),
                         datetime.datetime(2018, 2, 2, 0, 0, 0),
                         "test 6 failed.")
        self.assertEqual(p.getDate("[2/20/18, 2:00:00 AM]"),
                         datetime.datetime(2018, 2, 20, 2, 0, 0),
                         "test 7 failed.")

if __name__ == '__main__':
    unittest.main()
