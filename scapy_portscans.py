from scapy.all import *
from scapy.layers.inet import IP, TCP, UDP, ICMP

# ip = sys.argv[1]
dst_ip = "192.168.88.243"

# dst_port = sys.argv[2]
dst_port = 22

dst_timeout = 10

src_port = RandShort()


def tcp_connect_scan():
    tcp_connect_scan_resp = sr1(IP(dst=dst_ip) / TCP(sport=src_port, dport=dst_port, flags="S"), timeout=10)

    print(repr(tcp_connect_scan_resp))

    if str(type(tcp_connect_scan_resp)) == "<type 'NoneType'>":
        print("Closed")

    elif tcp_connect_scan_resp.haslayer(TCP):

        if tcp_connect_scan_resp.getlayer(TCP).flags == 0x12:
            send_rst = sr(IP(dst=dst_ip) / TCP(sport=src_port, dport=dst_port, flags="AR"), timeout=10)
            print("Open")

        elif tcp_connect_scan_resp.getlayer(TCP).flags == 0x14:
            print("Closed")


def tcp_stealth_scan():
    tcp_stealth_scan_resp = sr1(IP(dst=dst_ip) / TCP(sport=src_port, dport=dst_port, flags="S"), timeout=10)

    print(repr(tcp_stealth_scan_resp))

    if str(type(tcp_stealth_scan_resp)) == "<type 'NoneType'>":
        print("Filtered")

    elif tcp_stealth_scan_resp.haslayer(TCP):

        if tcp_stealth_scan_resp.getlayer(TCP).flags == 0x12:
            send_rst = sr(IP(dst=dst_ip) / TCP(sport=src_port, dport=dst_port, flags="R"), timeout=10)
            print("Open")

        elif tcp_stealth_scan_resp.getlayer(TCP).flags == 0x14:
            print("Closed")

    elif tcp_stealth_scan_resp.haslayer(ICMP):
        if int(tcp_stealth_scan_resp.getlayer(ICMP).type) == 3 and \
                        int(tcp_stealth_scan_resp.getlayer(ICMP).code) in [1, 2, 3, 9, 10, 13]:
            print("Filtered")


def xmas_scan():
    xmas_scan_resp = sr1(IP(dst=dst_ip) / TCP(dport=dst_port, flags="FPU"), timeout=10)

    print(repr(xmas_scan_resp))

    if str(type(xmas_scan_resp)) == "<type 'NoneType'>":
        print("Open|Filtered")

    elif xmas_scan_resp.haslayer(TCP):
        if xmas_scan_resp.getlayer(TCP).flags == 0x14:
            print("Closed")

        elif xmas_scan_resp.haslayer(ICMP):
            if int(xmas_scan_resp.getlayer(ICMP).type) == 3 and \
                            int(xmas_scan_resp.getlayer(ICMP).code) in [1, 2, 3, 9, 10, 13]:
                print("Filtered")


def fin_scan():
    fin_scan_resp = sr1(IP(dst=dst_ip) / TCP(dport=dst_port, flags="F"), timeout=10)

    print(repr(fin_scan_resp))

    if str(type(fin_scan_resp)) == "<type 'NoneType'>":
        print("Open|Filtered")

    elif fin_scan_resp.haslayer(TCP):
        if fin_scan_resp.getlayer(TCP).flags == 0x14:
            print("Closed")

    elif fin_scan_resp.haslayer(ICMP):
        if int(fin_scan_resp.getlayer(ICMP).type) == 3 and \
                        int(fin_scan_resp.getlayer(ICMP).code) in [1, 2, 3, 9, 10, 13]:
            print("Filtered")


def null_scan():
    null_scan_resp = sr1(IP(dst=dst_ip) / TCP(dport=dst_port, flags=""), timeout=10)

    print(repr(null_scan_resp))

    if str(type(null_scan_resp)) == "<type 'NoneType'>":
        print("Open|Filtered")

    elif null_scan_resp.haslayer(TCP):
        if null_scan_resp.getlayer(TCP).flags == 0x14:
            print("Closed")

        elif null_scan_resp.haslayer(ICMP):
            if int(null_scan_resp.getlayer(ICMP).type) == 3 and \
                            int(null_scan_resp.getlayer(ICMP).code) in [1, 2, 3, 9, 10, 13]:
                print("Filtered")


def tcp_ack_scan():
    tcp_ack_flag_scan_resp = sr1(IP(dst=dst_ip) / TCP(dport=dst_port, flags="A"), timeout=10)

    print(repr(tcp_ack_flag_scan_resp))

    if str(type(tcp_ack_flag_scan_resp)) == "<type 'NoneType'>":
        print("Stateful firewall present (Filtered)")

    elif tcp_ack_flag_scan_resp.haslayer(TCP):
        if tcp_ack_flag_scan_resp.getlayer(TCP).flags == 0x4:
            print("No firewall (Unfiltered)")

        elif tcp_ack_flag_scan_resp.haslayer(ICMP):
            if int(tcp_ack_flag_scan_resp.getlayer(ICMP).type) == 3 and \
                            int(tcp_ack_flag_scan_resp.getlayer(ICMP).code) in [1, 2, 3, 9, 10, 13]:
                print("Stateful firewall present (Filtered)")


def tcp_window_scan():
    tcp_window_scan_resp = sr1(IP(dst=dst_ip) / TCP(dport=dst_port, flags="A"), timeout=10)

    print(repr(tcp_window_scan_resp))

    if str(type(tcp_window_scan_resp)) == "<type 'NoneType'>":
        print("No response")

    elif tcp_window_scan_resp.haslayer(TCP):
        if tcp_window_scan_resp.getlayer(TCP).window == 0:
            print("Closed")

        elif tcp_window_scan_resp.getlayer(TCP).window > 0:
            print("Open")


def udp_scan():
    # not sure it works as intended
    udp_scan_resp = sr1(IP(dst=dst_ip) / UDP(dport=dst_port), timeout=dst_timeout)

    print(repr(udp_scan_resp))

    if str(type(udp_scan_resp)) == "<type 'NoneType'>":
        retrans = []
        for count in range(0, 3):
            retrans.append(sr1(IP(dst=dst_ip) / UDP(dport=dst_port), timeout=dst_timeout))

        for item in retrans:
            if str(type(item)) != "<type 'NoneType'>":
                udp_scan()
                return "Open|Filtered"

            elif udp_scan_resp.haslayer(UDP):
                return "Open"

            elif udp_scan_resp.haslayer(ICMP):
                if int(udp_scan_resp.getlayer(ICMP).type) == 3 and int(udp_scan_resp.getlayer(ICMP).code) == 3:
                    return "Closed"

                elif int(udp_scan_resp.getlayer(ICMP).type) == 3 and \
                                int(udp_scan_resp.getlayer(ICMP).code) in [1, 2, 9, 10, 13]:
                    return "Filtered"
