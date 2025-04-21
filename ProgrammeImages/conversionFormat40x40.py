import os
from PIL import Image

input_folder = "Images/"
output_folder = "ImagesSortie40x40/"

#os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg")):
        path = os.path.join(input_folder, filename)
        image = Image.open(path).convert("RGBA")

        # Redimension proportionnelle
        new_width = 40
        aspect_ratio = image.height / image.width
        new_height = int(new_width * aspect_ratio)

        resized = image.resize((new_width, new_height), Image.LANCZOS)

        # Centrer avec padding transparent
        final_image = Image.new("RGBA", (40, 40), (0, 0, 0, 0))
        final_image.paste(resized, (0, (40 - new_height) // 2))

        # Enregistrer en PNG
        output_name = os.path.splitext(filename)[0] + ".png"
        output_path = os.path.join(output_folder, output_name)
        final_image.save(output_path, "PNG")

        print(f"✅ Redimensionné : {filename} → {output_name}")
