import socket
import subprocess
import sys
from datetime import datetime
import argparse

def scan_target(target, start_port, end_port):
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        sys.exit()

    print("-" * 60)
    print("Scanning remote host", target_ip)
    print("-" * 60)

    open_ports = []

    try:
        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)

            result = sock.connect_ex((target_ip, port))
            if result == 0:
                print(f"Port {port}: Open")
                open_ports.append(port)
            sock.close()

    except KeyboardInterrupt:
        print("You pressed Ctrl+C. Exiting.")
        sys.exit()

    except socket.error:
        print("Couldn't connect to server. Exiting.")
        sys.exit()

    return open_ports

def main():
    parser = argparse.ArgumentParser(description="Simple network scanner.")
    parser.add_argument("target", help="Target host to scan.")
    parser.add_argument("start_port", type=int, help="Start port for the scan.")
    parser.add_argument("end_port", type=int, help="End port for the scan.")
    args = parser.parse_args()

    target = args.target
    start_port = args.start_port
    end_port = args.end_port

    open_ports = scan_target(target, start_port, end_port)

    print("\nScan completed!")
    if open_ports:
        print("Open ports:", open_ports)
    else:
        print("No open ports found.")

if __name__ == "__main__":
    main()
