from datetime import datetime
from pathlib import Path

class ScrollNote():
    def __init__(self, content):
        logs_path = Path("logs")
        logs_path.mkdir(parents=True, exist_ok=True)
        self.content = content
        self.date = (datetime.today().strftime("%Y-%m-%d"))+'.txt'
        self.filepath = Path(logs_path) / self.date

    def __str__(self):
        return f"{self.content}, {self.date}, {self.filepath}"

print(ScrollNote("Hello"))