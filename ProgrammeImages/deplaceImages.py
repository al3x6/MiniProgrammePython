import os
import shutil
from dotenv import load_dotenv

# Charger les variables d’environnement
load_dotenv()

# Dossiers
#source_folder = "ImagesSortieWebp/"
source_folder = "ImagesSortie40x40/"
destination_folder = os.getenv("DEST_FOLDER")

# Créer le dossier de destination s'il n'existe pas
#os.makedirs(destination_folder, exist_ok=True)

# Extensions des images à déplacer
image_extensions = (".png",".webp")

# Parcours et déplacement
for filename in os.listdir(source_folder):
    if filename.lower().endswith(image_extensions):
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)

        shutil.move(source_path, destination_path)
        print(f"✅ Déplacé : {filename}")
