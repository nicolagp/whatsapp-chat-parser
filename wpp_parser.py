import pandas as pd
import datetime as dt


class WppParser:
    def __init__(self, file):
        self.fileName = file

    def to_csv(self, csv_name):
        with open(self.fileName, encoding="utf8") as file:
            file_contents = file.read()
            file_lines = file_contents.split("\n")

        lines_matrix = list()
        for line in file_lines:
            time = self.get_date(line)
            user = self.get_user(line)
            content = self.get_content(line)
            # Check if any field returned None
            if time is None or user is None or content is None:
                continue

            lines_list = [time, user, content]
            lines_matrix.append(lines_list)

        df = pd.DataFrame(lines_matrix, columns=["Time", "User", "Message"])
        df.to_csv(csv_name, encoding='utf-8')

        return

    """
    line: string with a message line
    return: datetime with the time of the message, or None if the line doesn't
    contain a timestamp
    """
    def get_date(self, line):
        # Date str is of format: "[2/2/18, 5:32:54 PM]"
        end = line.find("]")
        date_string = line[1:end]
        pm_or_am = date_string[-2:]
        date_string = date_string[:-2]
        try:
            timestamp = dt.datetime.strptime(date_string, "%m/%d/%y, %H:%M:%S ")
        except ValueError:
            return None

        if pm_or_am == "PM" and timestamp.hour < 12:
            timestamp = timestamp + dt.timedelta(hours=12)
        elif pm_or_am == "AM" and timestamp.hour == 12:
            timestamp = timestamp - dt.timedelta(hours=12)

        return timestamp

    """
    line: (string) with raw message line
    return: (string) user who sent the message
    """

    def get_user(self, line):
        # match = re.search("\].*:", line)
        # if match is None:
        #     return None
        # user = match.group()[2:-1]
        # return user
        start = line.find(']')
        end = line.find(':', start)
        if start == -1 or end == -1:
            return None
        return line[start + 2:end]

    """
    line: (string) with raw message line
    return: (string) message content
    """

    def get_content(self, line):
        line = line[line.find("]"):]
        content = line[line.find(":") + 2:]
        return content


def main():
    parser = WppParser('_chat.txt')
    parser.to_csv('test.csv')

if __name__ == '__main__':
    main()
