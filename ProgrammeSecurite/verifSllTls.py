### Vérification de force de version sécurisée du protocole SLL/TLS

import ssl
import socket

def get_tls_version(hostname, port=443):
    context = ssl.create_default_context()
    
    # Désactiver les options de sécurité pour permettre le test de versions spécifiques
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    tls_versions = {
        ssl.TLSVersion.SSLv23: "SSL v2/v3 (Insecure)",
        ssl.TLSVersion.TLSv1: "TLS v1.0 (Insecure)",
        ssl.TLSVersion.TLSv1_1: "TLS v1.1 (Insecure)",
        ssl.TLSVersion.TLSv1_2: "TLS v1.2 (Secure)",
        ssl.TLSVersion.TLSv1_3: "TLS v1.3 (Most Secure)"
    }

    for tls_version, version_name in tls_versions.items():
        context.maximum_version = tls_version
        context.minimum_version = tls_version
        try:
            with socket.create_connection((hostname, port)) as sock:
                with context.wrap_socket(sock, server_hostname=hostname) as ssl_sock:
                    print(f"{version_name} est pris en charge par {hostname}")
        except ssl.SSLError:
            print(f"{version_name} n'est pas pris en charge.")
        except Exception as e:
            print(f"Erreur de connexion : {e}")
            break

if __name__ == "__main__":
    target_host = input("Entrez l'URL ou l'IP du serveur : ")
    get_tls_version(target_host)
