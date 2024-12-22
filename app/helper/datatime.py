from datetime import datetime

def parser_datetime(date: str, format: str = "%Y-%m-%d %H:%M:%S"):
  return datetime.strptime(date, format)