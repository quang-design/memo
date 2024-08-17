import datetime
import sys
import os

class Memo:
    def __init__(self, thoughts):
        self.thoughts = thoughts

    def save(self):
        current_datetime = datetime.datetime.now()
        year = current_datetime.strftime("%Y")
        month = current_datetime.strftime("%m")
        day = current_datetime.strftime("%d")
        time = current_datetime.strftime("%H:%M:%S")

        # Create folder structure year/month/day
        folder_path = os.path.join(year, month, day)
        os.makedirs(folder_path, exist_ok=True)

        # Create or open the file for the current day
        filename = os.path.join(folder_path, f"{year}-{month}-{day}.txt")
        with open(filename, "a") as file:
            file.write(f"{time} - Thoughts: {self.thoughts}\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        thoughts = " ".join(sys.argv[1:])
    else:
        thoughts = input("What's on your mind, right now? ")

    memo = Memo(thoughts)
    memo.save()
