import nmap
import socket
import requests
import time

# Fonction pour scanner les machines du réseau
def scan_network():
    nm = nmap.PortScanner
    nm.scan(hosts='192.168.1.0/24', arguments='-sn')
    hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
    return hosts_list

# Fonction pour tester la latence de la connexion Internet
def test_latency():
    try:
        latency = round(requests.get('http://google.com').elapsed.total_seconds(), 2)
        return latency
    except:
        return None

# Fonction pour récupérer l'IP publique et l'associer à un nom de domaine
def get_public_ip():
    try:
        public_ip = requests.get('https://api.ipify.org').text
        domain_name = 'mydomain.com'
        # Mettre en place le lien entre l'IP publique et le nom de domaine ici
        return (public_ip, domain_name)
    except:
        return (None, None)

# Fonction pour tester le débit de la connexion Internet

# Fonction pour mettre à jour le tableau de bord
def update_dashboard():
    # Récupération des informations sur le réseau
    ip_address = socket.gethostbyname(socket.gethostname())
    hostname = socket.gethostname()
    public_ip, domain_name = get_public_ip()
    # Récupération des informations sur la connexion Internet
    connection_status = 'Connecté' if test_latency() else 'Non connecté'
    latency = test_latency()

    # Mise à jour du tableau de bord avec les informations récupérées
    dashboard_data = {
        'Adresse IP de la Semabox': ip_address,
        'Nom de la Semabox': hostname,
        'IP publique de l\'accès Internet': public_ip,
        'Nom DNS dynamique': domain_name,
        'Etat de la connexion Internet': connection_status,

    }

    # Afficher le tableau de bord ici
    print(dashboard_data)

# Mise à jour du tableau de bord toutes les 10 minutes
while True:
    update_dashboard()
    time.sleep(600)
