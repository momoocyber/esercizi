from scapy.all import *
iPkt=0

def process_packet(pkt):
    
    print("Ho letto un pkt sulla tua macchina")
    global iPkt
    iPkt += 1   

sniff(iface="enp4s0", filter="tcp", prn= process_packet) 