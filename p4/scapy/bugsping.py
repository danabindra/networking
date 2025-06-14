#!/usr/bin/env python3
from scapy.all import *
import sys
import time

def BugsPingHost(target, count=4):
    print(f"[*] Pinging {target}")
    
    # Create ICMP echo request packet
    BugsPingPacket = IP(dst=target)/ICMP()
    
    # Send packets and capture responses
    BugsResponses = []
    for i in range(count):
        BugsStartTime = time.time()
        BugsResponse = sr1(BugsPingPacket, timeout=2, verbose=False)
        
        if BugsResponse is None:
            print(f"Request timed out.")
        else:
            BugsEndTime = time.time()
            BugsRtt = (BugsEndTime - BugsStartTime) * 1000  # Convert to milliseconds
            BugsResponses.append(BugsRtt)
            print(f"Reply from {BugsResponse.src}: time={BugsRtt:.2f}ms")
        
        time.sleep(1)  # Wait 1 second between pings
    
    if BugsResponses:
        BugsAvgRtt = sum(BugsResponses) / len(BugsResponses)
        print(f"\nPing statistics for {target}:")
        print(f"    Packets: Sent = {count}, Received = {len(BugsResponses)}, Lost = {count - len(BugsResponses)}")
        print(f"    Average RTT: {BugsAvgRtt:.2f}ms")

def BugsMain():
    if len(sys.argv) != 2:
        print("Usage: python3 BugsPing.py <target>")
        print("Example: python3 BugsPing.py 8.8.8.8")
        sys.exit(1)
    
    BugsTarget = sys.argv[1]
    BugsPingHost(BugsTarget)

if __name__ == "__main__":
    BugsMain() 