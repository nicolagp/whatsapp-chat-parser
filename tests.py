import wpp_parser
import unittest
import datetime


class TestDate(unittest.TestCase):
    def setUp(self):
        self.line1 = "[2/2/18, 5:32:54 PM] Juan Rodrigues: Ae queridos"
        self.line2 = "[12/20/18, 5:32:54 PM] Nicolas: 🙌🏻🙌🏻 é isso"
        self.line3 = "[2/20/18, 5:32:54 PM] Pedro Accorsi: q nem em 2017"
        self.line4 = "[12/2/18, 5:32:54 AM] Bruno Santos: eu nem tinha visto"
        self.line5 = "[2/2/18, 12:00:00 PM] Nicolas: Bora fazer isso ai"
        self.line6 = "[2/2/18, 12:00:00 AM] Lui Ferreira: Eu sou caipira demais vei"
        self.line7 = "[2/20/18, 2:00:00 AM] Felipe Silva: hahahahahaha"

    def test_date(self):
        p = wpp_parser.WppParser("")
        self.assertEqual(p.get_date(self.line1),
                         datetime.datetime(2018, 2, 2, 17, 32, 54),
                         "date 1 failed.")
        self.assertEqual(p.get_date(self.line2),
                         datetime.datetime(2018, 12, 20, 17, 32, 54),
                         "date 2 failed.")
        self.assertEqual(p.get_date(self.line3),
                         datetime.datetime(2018, 2, 20, 17, 32, 54),
                         "date 3 failed.")
        self.assertEqual(p.get_date(self.line4),
                         datetime.datetime(2018, 12, 2, 5, 32, 54),
                         "date 4 failed.")
        self.assertEqual(p.get_date(self.line5),
                         datetime.datetime(2018, 2, 2, 12, 0, 0),
                         "date 5 failed.")
        self.assertEqual(p.get_date(self.line6),
                         datetime.datetime(2018, 2, 2, 0, 0, 0),
                         "date 6 failed.")
        self.assertEqual(p.get_date(self.line7),
                         datetime.datetime(2018, 2, 20, 2, 0, 0),
                         "date 7 failed.")

    def test_user(self):
        p = wpp_parser.WppParser("")
        self.assertEqual(p.get_user(self.line1), "Juan Rodrigues", "user 1 failed.")
        self.assertEqual(p.get_user(self.line2), "Nicolas", "user 2 failed.")
        self.assertEqual(p.get_user(self.line3), "Pedro Accorsi", "tuserest 3 failed.")

    def test_content(self):
        p = wpp_parser.WppParser("")
        self.assertEqual(p.get_content(self.line1), "Ae queridos", "content 1 failed.")
        self.assertEqual(p.get_content(self.line2), "🙌🏻🙌🏻 é isso", "content 2 failed.")
        self.assertEqual(p.get_content(self.line3), "q nem em 2017", "content 3 failed.")

if __name__ == '__main__':
    unittest.main()
