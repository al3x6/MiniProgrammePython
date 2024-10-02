import sys
import socket
import subprocess
from datetime import datetime

## appel commande 
# Efface l'écran du terminal (utilise 'cls' pour Windows, 'clear' pour Linux/macOS)
#subprocess.call('clear', shell=True)
subprocess.call('cls', shell=True)

# Demande à l'utilisateur d'entrer l'IP du serveur à scanner
remoteServerIP = input('Entrer l\'ip d\'un serveur à scanner : ')
print('-'*60)
print('Lancement du scan des ports de la machine '+ remoteServerIP)
print('-'*60)

# récup du temps de maintenant
t1 = datetime.now()

try:
    # Boucle pour scanner les ports de 1 à 1024
    for port in range(1, 1025):
        # Crée un socket IPv4, TCP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Tente de se connecter au port
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print('Port {}:   Ouvert'.format(port))
        sock.close()

# Gérer l'interruption manuelle (Ctrl+C)
except KeyboardInterrupt:
    print('Vous avez appuyé sur Ctrl+C')
    sys.exit()

# Gérer les erreurs de connexion
except socket.error:
    print('Impossible de se connecter au serveur')
    sys.exit()

# Récupération du temps de fin du scan
t2 = datetime.now()

# Calcul du temps total du scan
total_temps = t2 - t1
print('Scan complété en : ' + str(total_temps))
