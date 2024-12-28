import sys
from pathlib import Path
from collections import Counter

def file_error(func):
    def inner(*args, **kwargs):
        try:
            logs = func(*args, **kwargs)
            return logs
        except FileNotFoundError: 
            print("Файл не знайдено.")
        except Exception as e:
            print(f"Сталася помилка: {e}")

    return inner

def parse_log_line(line: str) -> dict:
    date, time, level, *args = line.split()
    message = " ".join(args)
    return {"date": date, "time": time, "level": level, "message": message} 

@file_error
def load_logs(file_path: str) -> list:
    with open(file_path) as f:
        lines = []
        while True:
            line = f.readline()
            if not line:
                break
            lines.append(parse_log_line(line))
                
        return lines
            

def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda log: log["level"] == level ,logs))

def count_logs_by_level(logs: list) -> dict:
    return Counter([log["level"] for log in logs])

def display_log_counts(counts: dict): 
    print(f"{'Level':<10} | {'Count':<10}")
    print("-" * 23)

    for level, count in counts.items():
        print(f"{level:<10} | {count:<10}")


def main():
    if len(sys.argv) > 1: 
        file_path = Path(sys.argv[1])
        logs = load_logs(file_path)
        display_log_counts(count_logs_by_level(logs))
        if len(sys.argv) > 2:
            log_level = sys.argv[2].upper()
            print("")
            print(f"Деталі логів для рівня '{log_level}':")
            logs_filtered = filter_logs_by_level(logs, log_level)
            for log in logs_filtered:
                print(f"{log["date"]} {log["time"]} {log["level"]} {log["message"]}")
    else:
        print("Please input path for logs file.")

if __name__ == "__main__":
    main()
