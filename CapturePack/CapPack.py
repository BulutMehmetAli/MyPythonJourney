import scapy 

"""
sniff() fonksiyonu, canlı ağ trafiğini yakalar.

Her yakalanan pakette:

IP katmanı bilgileri (src, dst, ttl)

TCP katmanı bilgileri (sport, dport, flags) yazdırılır.


"""

from scapy.all import sniff

def paket_yakala(paket):
    if paket.haslayer("IP") and paket.haslayer("TCP"):
        ip_katmani = paket["IP"]
        tcp_katmani = paket["TCP"]
        
        print("📌 IP Bilgileri:")
        print(f"  Kaynak IP: {ip_katmani.src}")
        print(f"  Hedef IP:  {ip_katmani.dst}")
        print(f"  TTL:       {ip_katmani.ttl}")
        
        print("📌 TCP Bilgileri:")
        print(f"  Kaynak Port: {tcp_katmani.sport}")
        print(f"  Hedef Port:  {tcp_katmani.dport}")
        print(f"  Bayraklar:   {tcp_katmani.flags}")
        print("-" * 40)
        

# Ağdan 10 adet TCP/IP paketi yakala
sniff(filter="tcp", prn=paket_yakala, count=10)
