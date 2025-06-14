#!/usr/bin/env python3
from scapy.all import *
import sys
import time

def DaffyCraftTcpPacket(target, port, payload=None):
    # Create IP and TCP layers
    DaffyIP = IP(dst=target)
    DaffyTCP = TCP(dport=port, flags="S")
    
    # Add payload if provided
    if payload:
        DaffyPacket = DaffyIP/DaffyTCP/Raw(load=payload)
    else:
        DaffyPacket = DaffyIP/DaffyTCP
    
    return DaffyPacket

def DaffyCraftUdpPacket(target, port, payload=None):
    # Create IP and UDP layers
    DaffyIP = IP(dst=target)
    DaffyUDP = UDP(dport=port)
    
    # Add payload if provided
    if payload:
        DaffyPacket = DaffyIP/DaffyUDP/Raw(load=payload)
    else:
        DaffyPacket = DaffyIP/DaffyUDP
    
    return DaffyPacket

def DaffyCraftIcmpPacket(target, payload=None):
    # Create IP and ICMP layers
    DaffyIP = IP(dst=target)
    DaffyICMP = ICMP()
    
    # Add payload if provided
    if payload:
        DaffyPacket = DaffyIP/DaffyICMP/Raw(load=payload)
    else:
        DaffyPacket = DaffyIP/DaffyICMP
    
    return DaffyPacket

def DaffySendPacket(packet, count=1, interval=1):
    print(f"[*] Sending packet to {packet[IP].dst}")
    print(f"[*] Protocol: {packet[IP].proto}")
    
    for i in range(count):
        print(f"\n[+] Sending packet {i+1}/{count}")
        DaffyResponse = sr1(packet, timeout=2, verbose=False)
        
        if DaffyResponse:
            print(f"[+] Received response from {DaffyResponse.src}")
            print(f"[+] Response type: {DaffyResponse.type}")
        else:
            print("[-] No response received")
        
        if i < count - 1:
            time.sleep(interval)

def DaffyMain():
    if len(sys.argv) < 3:
        print("Usage: python3 DaffyPacketCrafter.py <target> <protocol> [port] [payload]")
        print("Example: python3 DaffyPacketCrafter.py 192.168.1.1 tcp 80 'Hello World'")
        sys.exit(1)
    
    DaffyTarget = sys.argv[1]
    DaffyProtocol = sys.argv[2].lower()
    
    # Get optional parameters
    DaffyPort = int(sys.argv[3]) if len(sys.argv) > 3 else None
    DaffyPayload = sys.argv[4] if len(sys.argv) > 4 else None
    
    # Create and send packet based on protocol
    if DaffyProtocol == "tcp":
        if not DaffyPort:
            print("Error: Port required for TCP packet")
            sys.exit(1)
        DaffyPacket = DaffyCraftTcpPacket(DaffyTarget, DaffyPort, DaffyPayload)
    elif DaffyProtocol == "udp":
        if not DaffyPort:
            print("Error: Port required for UDP packet")
            sys.exit(1)
        DaffyPacket = DaffyCraftUdpPacket(DaffyTarget, DaffyPort, DaffyPayload)
    elif DaffyProtocol == "icmp":
        DaffyPacket = DaffyCraftIcmpPacket(DaffyTarget, DaffyPayload)
    else:
        print(f"Error: Unsupported protocol {DaffyProtocol}")
        sys.exit(1)
    
    DaffySendPacket(DaffyPacket)

if __name__ == "__main__":
    DaffyMain() 