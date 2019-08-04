import pandas as pd
from datetime import datetime
import datetime
import re


class WppParser:
    def __init__(self, file):
        self.fileName = file

    def toCSV(self, csvName):
        with open(self.fileName, encoding="utf8") as file:
            file_contents = file.read()
            file_lines = file_contents.split("\n")

        linesMatrix = list()
        for line in file_lines:
            time = self.getDate(self, line)
            user = self.getUser(self, line)
            content = self.getContent(self, line)
            # Check if any field returned None
            if time is None or user is None or content is None:
                continue

            linesList = [time, user, content]
            linesMatrix.append(linesList)

        df = pd.DataFrame(linesMatrix, columns=["Time", "User", "Message"])
        df.to_csv(csvName, encoding='utf-8')

        return

    """
    line: string with a message line
    return: datetime with the time of the message, or None if the line doesn't
    contain a timestamp
    """
    def getDate(self, line):
        # Date str is of format: "[2/2/18, 5:32:54 PM]"
        match = re.search("\[.*/.*/.*,.*:.*:*\]", line)
        if match is not None:
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

    """
    line: (string) with raw message line
    return: (string) user who sent the message
    """
    def getUser(self, line):
        # TODO
        return

    """
    line: (string) with raw message line
    return: (string) message content
    """
    def getContent(self, line):
        # TODO
        return


# if __name__ == "__main__":
#     main()
