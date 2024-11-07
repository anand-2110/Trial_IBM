import pyshark

def run_nids(interface='eth0'):
    """
    Monitors network traffic using Pyshark to capture packets.
    Here, we simulate network monitoring with a simple check for suspicious traffic.
    """
    cap = pyshark.LiveCapture(interface=interface, bpf_filter='ip')
    suspicious_traffic = False
    
    for packet in cap.sniff_continuously(packet_count=10):  # Capture 10 packets for simplicity
        if packet.ip.src == '192.168.0.1':  # Example: Check for specific IP traffic (suspicious pattern)
            suspicious_traffic = True
            break
    
    return {'flagged': suspicious_traffic}
