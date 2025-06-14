#!/usr/bin/env python3
from scapy.all import *
import sys
import time

def DaffyScanNetwork(network):
    print(f"[*] Scanning network: {network}")
    
    # Create ARP request packet
    DaffyArpRequest = ARP(pdst=network)
    DaffyBroadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    DaffyArpBroadcast = DaffyBroadcast/DaffyArpRequest
    
    # Send packet and capture responses
    DaffyAnsweredList = srp(DaffyArpBroadcast, timeout=3, verbose=False)[0]
    
    # Process responses
    print("\n[+] Available devices:")
    print("IP\t\t\tMAC Address")
    print("-" * 37)
    
    for DaffySent, DaffyReceived in DaffyAnsweredList:
        print(f"{DaffyReceived.psrc}\t\t{DaffyReceived.hwsrc}")

def DaffyMain():
    if len(sys.argv) != 2:
        print("Usage: python3 DaffyArpScanner.py <network>")
        print("Example: python3 DaffyArpScanner.py 192.168.1.0/24")
        sys.exit(1)
        
    DaffyNetwork = sys.argv[1]
    DaffyScanNetwork(DaffyNetwork)

if __name__ == "__main__":
    DaffyMain() 