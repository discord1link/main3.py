import socket

scan_host = input("URL/IP to scan: ")
scan_ip = socket.gethostbyname(scan_host)

print(f"Scanning {scan_ip}")

socket.setdefaulttimeout(0.05)
for port in range(1, 65535):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((scan_ip, port))
        if result == 0:
            print(f"Port {port}")
            sock.close()
    except Exception:
        pass