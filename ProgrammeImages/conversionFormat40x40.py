import os
from PIL import Image

input_folder = "Images/"
output_folder = "ImagesSortie40x40/"

#os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg")):
        path = os.path.join(input_folder, filename)
        image = Image.open(path).convert("RGBA")

        # Calcul de la nouvelle taille proportionnelle
        new_width = 40
        new_height = 40

        # Si la largeur est plus grande que la hauteur, redimensionner la hauteur
        if image.width > image.height:
            aspect_ratio = image.width / image.height
            new_height = int(new_width / aspect_ratio)
        else:
            aspect_ratio = image.height / image.width
            new_width = int(new_height / aspect_ratio)

        resized = image.resize((new_width, new_height), Image.LANCZOS)

        # Centrer avec padding transparent
        final_image = Image.new("RGBA", (40, 40), (0, 0, 0, 0))
        final_image.paste(resized, ((40 - new_width) // 2, (40 - new_height) // 2))

        # Enregistrer en PNG
        output_name = os.path.splitext(filename)[0] + ".png"
        output_path = os.path.join(output_folder, output_name)
        final_image.save(output_path, "PNG")

        print(f"✅ Redimensionné : {filename} → {output_name}")