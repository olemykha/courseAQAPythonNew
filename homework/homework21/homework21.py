import os
from datetime import datetime


def analyze_heartbeat(input_path: str, output_path: str):

    key = "Key TSTFEED0300|7E3E|0400"
    timestamps = []

    with open(input_path, 'r', encoding='utf-8') as f:
        for line in f:
            if key in line:
                idx = line.find("Timestamp ")
                if idx >= 0:
                    ts_str = line[idx + len("Timestamp "): idx + len("Timestamp ") + 8]
                    try:
                        ts = datetime.strptime(ts_str, "%H:%M:%S")
                        timestamps.append(ts)
                    except ValueError:
                        continue

    with open(output_path, 'w', encoding='utf-8') as log_file:
        for prev, curr in zip(timestamps, timestamps[1:]):
            interval = abs((curr - prev).total_seconds())
            time_of_event = curr.strftime("%H:%M:%S")
            if 31 < interval < 33:
                log_file.write(f'{time_of_event} WARNING heartbeat interval {int(interval)}s\n')
            elif interval >= 33:
                log_file.write(f'{time_of_event} ERROR heartbeat interval {int(interval)}s\n')


if __name__ == "__main__":

    base_dir = os.path.dirname(__file__)
    input_log = os.path.join(base_dir, "hblog.txt")
    output_log = os.path.join(base_dir, "hb_test.log")

    analyze_heartbeat(input_log, output_log)
    print(f'Analysis complete.\nSee {output_log}')
