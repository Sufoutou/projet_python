from datetime import datetime, timedelta
import random

# Fonction pour générer une ligne de log Apache factice
def generate_apache_log_line(timestamp):
    # Liste d'adresses IP fictives
    ip_addresses = ["123.45.67.89", "98.76.54.32", "192.168.1.1", "10.0.0.2", "172.16.0.3"]
    
    # Liste d'identifiants d'utilisateurs (généralement vide pour les accès publics)
    user_ident = "-"
    
    # Liste d'identifiants d'utilisateurs authentifiés (généralement vide pour les accès publics)
    user_auth = "-"
    
    # Liste des méthodes HTTP et des ressources demandées
    methods_resources = [
        "GET /index.html HTTP/1.1",
        "POST /login.php HTTP/1.1",
        "GET /images/logo.png HTTP/1.1",
        "GET /css/style.css HTTP/1.1",
        "HEAD / HTTP/1.1"
    ]
    
    # Codes de statut HTTP
    status_codes = [200, 404, 500, 302, 401]
    
    # Tailles de réponse (en octets)
    response_sizes = [1024, 2048, 0, 512, 256]
    
    # URLs référentes
    referrers = ["-", "http://example.com", "https://google.com/search", "http://mysite.com/about", "https://news.com/article"]

    # Identifiants des agents utilisateur
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        "Mozilla/5.0 (Linux; Android 9; Pixel 3)",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 13_6 like Mac OS X)",
        "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
    ]

    # Création de la ligne de log
    log_line = f'{random.choice(ip_addresses)} {user_ident} {user_auth} [{timestamp.strftime("%d/%b/%Y:%H:%M:%S +0000")}] "{random.choice(methods_resources)}" {random.choice(status_codes)} {random.choice(response_sizes)} "{random.choice(referrers)}" "{random.choice(user_agents)}"'
    
    return log_line

# Génération de 50 lignes de logs
start_time = datetime.now()
apache_logs = []

for i in range(50):
    # Générer un timestamp aléatoire dans les dernières 24 heures
    timestamp = start_time - timedelta(minutes=random.randint(0, 1440))
    apache_logs.append(generate_apache_log_line(timestamp))

apache_logs_text = "\n".join(apache_logs)
print(apache_logs_text)

with open("apache_logs.txt", "w", encoding="utf-8") as file:
    file.write(apache_logs_text)