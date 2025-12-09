from scapy.all import sniff, IP, TCP, UDP, Raw, wrpcap
import datetime
import argparse

packet_list = []

def packet_summary(pkt):
    time_stamp = datetime.datetime.fromtimestamp(pkt.time).strftime("%Y-%m-%d %H:%M:%S")

    if IP in pkt:
        src = pkt[IP].src
        dst = pkt[IP].dst

        if TCP in pkt:
            proto = "TCP"
        elif UDP in pkt:
            proto = "UDP"
        else:
            proto = str(pkt[IP].proto)

        length = len(pkt)
        print(f"[{time_stamp}] {src} --> {dst} | Protocol: {proto} | Length: {length}")

    # store packet for saving
    packet_list.append(pkt)

def main():
    parser = argparse.ArgumentParser(description="Simple Network Packet Sniffer")
    parser.add_argument("-c", "--count", type=int, default=0, help="Number of packets to capture")
    parser.add_argument("-o", "--output", type=str, help="Output PCAP file")
    args = parser.parse_args()

    print("Starting packet capture...\n")

    sniff(prn=packet_summary, count=args.count if args.count > 0 else 0)

    if args.output:
        wrpcap(args.output, packet_list)
        print(f"\nSaved captured packets to {args.output}")

if __name__ == "__main__":
    main()

