from ping3 import ping
import socket


def scan_local_network():
    """Simple network scanner for demo purposes"""
    # For demo, we'll use some common hosts or your local network
    hosts_to_ping = [
        'google.com',
        '8.8.8.8',  # Google DNS
        '1.1.1.1',  # Cloudflare DNS
        'localhost'
    ]

    latency_results = {}

    for host in hosts_to_ping:
        try:
            response_time = ping(host, timeout=2)
            if response_time:
                latency_results[host] = round(
                    response_time * 1000, 2)  # Convert to ms
                print(f"✅ {host}: {latency_results[host]} ms")
            else:
                latency_results[host] = float('inf')
                print(f"❌ {host}: Unreachable")
        except Exception as e:
            print(f"❌ {host}: Error - {e}")
            latency_results[host] = float('inf')

    return latency_results


if __name__ == "__main__":
    print("🔍 Scanning network...")
    results = scan_local_network()
    print("\n📊 Results:", results)
