### 

import re
import subprocess
import optparse

##### MON ADRESSE MAC
def search_mac_address(mac_address):
    '''
    Fonction de recherche d'adresse MAC
    '''
    return re.search(r'([0-9A-F]{2}[:-]){5}([0-9A-F]{2})', str(mac_address)).group(0)

def get_mac_address_from_interface(interface):
    '''
    Récupérer l'adresse MAC de l'interface
    '''
    ifconfig_result = subprocess.check_output(["ifconfig ", interface])
    mac_address_search_result = search_mac_address(ifconfig_result)

    if mac_address_search_result:
        return mac_address_search_result
    else:
        print("[-] Ce n'est pas une adresse MAC")

#### INPUT ADRESSE MAC ET INTERFACE
def  get_arguments():
    '''
    Permet de récupérer les arguments de l'utilisateur pour le changement de l'adresse MAC à l'adresse spécifiée
    sudo python3 macChanger.py -i ens33 -m 00:11:22:33:44:55
    '''
    parser = optparse.OptionParser()     #Permet de lire les options d'une commande
    
    # met dans une variable interface
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    # met dans une variable new_mac_address
    parser.add_option("-m", "--mac", dest="new_mac_address", help="New MAC address")
    
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Entrer une interface")
    elif not options.new_mac_address:
        parser.error("[-] Entrer une nouvelle adresse MAC")
    return options

#### NOUVELLE ADRESSE MAC
def set_new_mac_address(interface, new_mac_address):
    '''
    Changement de l'adresse MAC
    '''
    print("[+] Changement de l'adresse Mac > " + new_mac_address + " à l'interface > "+ interface)
    subprocess.call("ifconfig " + interface + " down", shell=True)
    subprocess.call("ifconfig " + interface + " hw ether " + new_mac_address, shell=True)
    subprocess.call("ifconfig " + interface + " up", shell=True)



#interface = input("interface > ")
#new_mac_address = input("new_mac_address > ")
#set_new_mac_address(interface, new_mac_address)
options = get_arguments()
current_mac_address = get_mac_address_from_interface(options.interface)

print("Adresse Mac courante de l'interface "+ options.interface +" est " + current_mac_address)

if current_mac_address == options.new_mac_address:
    print("[-] MAC Adresse " + current_mac_address + " est déjà utilisée.")
else:
    set_new_mac_address(options.interface, options.new_mac_address)
    
    new_mac_address = get_mac_address_from_interface(options.interface)
    if new_mac_address == options.new_mac_address:
        print("[+] MAC adresse a été changé avec succès à " + new_mac_address)
    else :
        print("[-] MAC adresse n'a pas pu être changé.")
    
### sudo python3 macChanger.py -i ens33 -m 00:11:22:33:44:55