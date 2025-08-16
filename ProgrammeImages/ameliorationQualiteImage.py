import cv2
import numpy as np
from PIL import Image, ImageEnhance

def enhance_image(input_path, output_path):
    # Charger l'image
    image = cv2.imread(input_path)

    # Étape 1 : réduction du bruit (facultatif)
    denoised = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)

    # Étape 2 : améliorer la netteté
    sharpen_kernel = np.array([[0, -1, 0],
                               [-1, 5,-1],
                               [0, -1, 0]])
    sharpened = cv2.filter2D(denoised, -1, sharpen_kernel)

    # Étape 3 : conversion en format PIL pour ajuster luminosité et contraste
    image_pil = Image.fromarray(cv2.cvtColor(sharpened, cv2.COLOR_BGR2RGB))

    # Amélioration de la luminosité
    enhancer_brightness = ImageEnhance.Brightness(image_pil)
    image_pil = enhancer_brightness.enhance(1.1)  # 1.0 = original

    # Amélioration du contraste
    enhancer_contrast = ImageEnhance.Contrast(image_pil)
    image_pil = enhancer_contrast.enhance(1.2)

    # Étape 4 : (optionnel) agrandissement avec interpolation bicubique
    width, height = image_pil.size
    upscale = image_pil.resize((width*2, height*2), Image.BICUBIC)

    # Sauvegarder l'image finale
    upscale.save(output_path)
    print(f"Image sauvegardée ici : {output_path}")

# Exemple d'utilisation
g('conversionFormat40x40.png', 'Images/ameliorer.png')
