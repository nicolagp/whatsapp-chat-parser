import pandas as pd
import datetime as dt
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
        end = line.find("]")
        date_string = line[1:end]      
        PM_or_AM = date_string[-2:]
        date_string = date_string[:-2]
        timestamp = dt.datetime.strptime(date_string, "%m/%d/%y, %H:%M:%S ")
        if PM_or_AM == "PM":
            timestamp = timestamp + dt.timedelta(hours = 12)

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
