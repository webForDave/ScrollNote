from datetime import datetime
from pathlib import Path

class ScrollNote():
    def __init__(self, content):
        logs_path = Path("logs")
        logs_path.mkdir(parents=True, exist_ok=True)
        self.content = content
        self.date = (datetime.today().strftime("%Y-%m-%d"))+'.txt'
        self.filepath = Path(logs_path) / self.date

    def save(self):
        with open(self.filepath, "w", encoding="utf-8") as file:
            file.write(self.content)

    def load(self):
        try:
            with open(self.filepath, "r") as file:
                self.content = file.read()
                print(self.content)
        except FileNotFoundError:
            pass

    def __str__(self):
        return f"{self.content}, {self.date}, {self.filepath}"