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
        end = line.find("]")
        date_string = line[1:end]      
        PM_or_AM = date_string[-2:]
        date_string = date_string[:-2]
        timestamp = dt.datetime.strptime(date_string, "%m/%d/%y, %H:%M:%S ")
        if PM_or_AM == "PM":
            timestamp = timestamp + dt.timedelta(hours = 12)
        return timestamp


# line = "[2/2/18, 5:32:54 PM] Nicolas Perez: Bora jogar um fut amn"
# print(getDate(line))


# if __name__ == "__main__":
#     main()