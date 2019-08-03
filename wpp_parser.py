import pandas as pd
from datetime import datetime
import datetime
import re

class Parser:
    def __init__(self, file):
        self.fileName = file

    def toCSV(self):
        with open(self.fileName, encoding="utf8") as file:
            file_contents = file.read()
            file_lines = file_contents.split("\n")
        
        for line in file_lines:
            time = self._getDate(self, line)
            # Check if time is None

    """
    line: string with a message line
    return: datetime with the time of the message, or None if the line doesn't contain a timestamp
    """ 
    def getDate(self, line):
        # Date str is of format: "[2/2/18, 5:32:54 PM]"
        match = re.search("\[.*/.*/.*,.*:.*:*\]", line)
        if match != None:
            date_string = match.group()
        else:
            return None

        # get month
        if (date_string[2] == "/"):
            month = int(date_string[1])
            date_string = date_string[3:]
        else:
            month = int(date_string[1:3])
            date_string = date_string[4:]
        # get day
        if (date_string[1] == "/"):
            day = int(date_string[0])
            date_string = date_string[2:]
        else:
            day = int(date_string[0:2])
            date_string = date_string[3:]
        # get year
        year = int("20"+date_string[0:2])
        date_string = date_string[4:]
        # get hour
        if (date_string[1] == ":"):
            hour = int(date_string[0])
            date_string = date_string[2:]
        else:
            hour = int(date_string[0:2])
            date_string = date_string[3:]
        # get minute, second and period
        minute = int(date_string[0:2])
        second = int(date_string[3:5])
        period = date_string[6:8]
        # convert hour
        if period == "PM" and hour < 12:
            hour += 12
        elif period == "AM" and hour == 12:
            hour = 0

        timestamp = datetime.datetime(year, month, day, hour, minute, second)
        return timestamp


# line = "[2/2/18, 5:32:54 PM] Nicolas Perez: Bora jogar um fut amn"
# print(getDate(line))


# if __name__ == "__main__":
#     main()