from scapy.all import sniff, IP, TCP, UDP, Raw
import datetime

def packet_summary(pkt):
    time_stamp = datetime.datetime.fromtimestamp(pkt.time).strftime("%Y-%m-%d %H:%M:%S")

    if IP in pkt:
        src = pkt[IP].src
        dst = pkt[IP].dst
        proto = ""

        if TCP in pkt:
            proto = "TCP"
        elif UDP in pkt:
            proto = "UDP"
        else:
            proto = str(pkt[IP].proto)

        length = len(pkt)

        print(f"[{time_stamp}] {src} --> {dst} | Protocol: {proto} | Length: {length}")

def main():
    print("Starting packet capture... Press CTRL + C to stop.\n")

    sniff(prn=packet_summary, store=False)

if __name__ == "__main__":
    main()
