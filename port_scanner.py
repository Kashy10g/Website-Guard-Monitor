import socket

target = input("Enter IP to scan (e.g., 127.0.0.1): ")
ports = [21, 22, 80, 443, 3389] # Common ports

print(f"🔒 Scanning {target} for open doors...")

for port in ports:
    # Create a 'Socket' (The digital ear)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1) # Don't wait too long
    
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"✅ Port {port}: OPEN")
    else:
        print(f"❌ Port {port}: Closed")
    s.close()