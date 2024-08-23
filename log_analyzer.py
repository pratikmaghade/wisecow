import re
from collections import Counter

# Regular expression for parsing Apache/Nginx log entries
LOG_PATTERN = re.compile(r'(?P<ip>\S+) \S+ \S+ \[.*?\] "(?P<method>\S+) (?P<path>\S+) \S+" (?P<status>\d{3}) \d+')

def parse_log_file(log_file_path):
    with open(log_file_path, 'r') as file:
        logs = file.readlines()

    return logs

def analyze_logs(logs):
    ip_counter = Counter()
    path_counter = Counter()
    error_404_count = 0

    for log in logs:
        match = LOG_PATTERN.match(log)
        if match:
            ip = match.group('ip')
            path = match.group('path')
            status = match.group('status')

            ip_counter[ip] += 1
            path_counter[path] += 1

            if status == '404':
                error_404_count += 1

    return {
        '404_errors': error_404_count,
        'most_requested_pages': path_counter.most_common(10),
        'most_active_ips': ip_counter.most_common(10)
    }

def print_report(report):
    print(f"404 Errors: {report['404_errors']}")
    print("\nMost Requested Pages:")
    for path, count in report['most_requested_pages']:
        print(f"{path}: {count} requests")

    print("\nMost Active IP Addresses:")
    for ip, count in report['most_active_ips']:
        print(f"{ip}: {count} requests")

if __name__ == '__main__':
    # Path to the log file
    log_file_path = 'access.log'
    
    logs = parse_log_file(log_file_path)
    report = analyze_logs(logs)
    print_report(report)
