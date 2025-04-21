import os
from PIL import Image

input_folder = "ImagesSortie40x40/"
output_folder = "ImagesSortieWebp/"

#os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(".png"):
        path = os.path.join(input_folder, filename)
        image = Image.open(path).convert("RGBA")

        # Nom sans extension
        base_name = os.path.splitext(filename)[0]
        output_path = os.path.join(output_folder, base_name + ".webp")

        # Sauvegarde WebP (sans perte)
        image.save(output_path, "WEBP", lossless=True)

        print(f"✅ Converti : {filename} → {base_name}.webp")
