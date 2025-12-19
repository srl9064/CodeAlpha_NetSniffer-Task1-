# CodeAlpha – Basic Network Sniffer (Cybersecurity Internship)

This project is developed as **Task 1** of the **CodeAlpha Cybersecurity Internship**.  
It is a Python-based network packet sniffer built using the **Scapy** library to capture and analyze live network traffic.

---

##  Project Overview

The Network Sniffer captures real-time packets flowing through the system and displays essential information such as:

- Source IP address  
- Destination IP address  
- Network protocol (TCP / UDP / ICMP)  
- Packet size  
- Timestamp  

Captured packets can also be saved in **PCAP format**, allowing further analysis using tools like **Wireshark**.

---

##  Features

- Captures live network traffic  
- Displays protocol-level packet information  
- Saves packets to a `.pcap` file  
- Works on Ubuntu / WSL  
- Useful for learning basic network monitoring and cybersecurity concepts  

---

##  Technologies Used

- Python 3  
- Scapy  
- Ubuntu (WSL)  
- Wireshark  
- Git & GitHub  

---

##  Installation

1. Clone the repository:
- git clone https://github.com/srl9064/CodeAlpha_NetSniffer
- cd CodeAlpha_NetSniffer

2. Create and activate a virtual environment:
- python3 -m venv venv
- source venv/bin/activate

3. Install dependencies:
-pip install -r requirements.txt

---

##  How to Run

Run the sniffer with root privileges:
- sudo ./venv/bin/python3 sniffer.py -c 5 -o capture.pcap

### Command Explanation:
- `-c 5` → Captures 5 packets  
- `-o capture.pcap` → Saves packets to a PCAP file  

---

##  Sample Output

- [2025-12-09 10:12:01] 172.31.208.114 --> 8.8.8.8 | Protocol: ICMP | Length: 98
- [2025-12-09 10:12:02] 8.8.8.8 --> 172.31.208.114 | Protocol: ICMP | Length: 98
