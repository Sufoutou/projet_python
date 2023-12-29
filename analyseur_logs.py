#afficher les logs et lister les resultats
def afficher_logs(logs_list):
  for i, log in enumerate(logs_list, start=1):
      print(f"{i}. {log}")

#Filtrer les logs par adresse IP
def filtrer_par_ip(logs_list, adresse_ip):
  filtered_logs = [log for log in logs_list if adresse_ip in log]
  return filtered_logs

#Filtrer les logs par heure
def filtrer_par_heure(logs_list, heure):
  filtered_logs = [log for log in logs_list if heure in log]
  return filtered_logs

#Filtrer les logs par requete
def filtrer_par_type_requete(logs_list, type_requete):
  filtered_logs = [log for log in logs_list if type_requete.upper() in log.split('"')[1].split()[0]]
  return filtered_logs

#Filtrer les logs par navigateur
def filtrer_par_navigateur(logs_list, navigateur):
  filtered_logs = [log for log in logs_list if navigateur in log]
  return filtered_logs

# Menu pour l'utilisateur
print("Bienvenue ! Veuillez spécifier le chemin du fichier de logs :")
chemin_fichier = input("Chemin du fichier de logs : ")

# Lire les logs à partir du fichier spécifié
with open(chemin_fichier, 'r') as file:
  logs = file.readlines()

#Sélection pour l'utilisateur
import inquirer

if __name__ == "__main__":

    questions = [
        inquirer.Checkbox("logs", 
                          message="Please define your type of request?", 
                          choices=["@ip", "Hours", "browser", "request GET", "request Post",],
                        ),
                ]
    
        

    answers = inquirer.prompt(questions)

    print(answers)
#si une certaine case est cochée et effectuez l'action qui lui correspond
if '@ip' in answers['logs']:
    ip = input("Entrez l'adresse IP : ")
    filtered_logs = filtrer_par_ip(logs, ip)
    afficher_logs(filtered_logs)
elif 'Hours' in answers['logs']:
    heure = input("Entrez l'heure au format [DD/MMM/YYYY:HH:MM:SS +0000] : ")
    filtered_logs = filtrer_par_heure(logs, heure)
    afficher_logs(filtered_logs)
elif 'browser' in answers['logs']:
    navigateur = input("Entrez le type de navigateur : ")
    filtered_logs = filtrer_par_navigateur(logs, navigateur)
    afficher_logs(filtered_logs)
elif 'request GET' in answers['logs']:
    filtered_logs = filtrer_par_type_requete(logs, "GET")
    afficher_logs(filtered_logs)
elif 'request POST' in answers['logs']:
    filtered_logs = filtrer_par_type_requete(logs, "POST")
    afficher_logs(filtered_logs)
  
else:
  print("Choix invalide.")


# -----------------------------Ancien Menu-----------------------------#

# Menu pour l'utilisateur


# print("1. Afficher tous les logs")
# print("2. Afficher les logs pour une adresse IP précise")
# print("3. Afficher les logs pour une heure précise")
# print("4. Afficher les logs avec des requêtes POST")
# print("5. Afficher les logs avec des requêtes GET")
# print("6. Afficher les logs pour un type de navigateur précis")

# choix = input("Entrez votre choix : ")

# if choix == "1":
#   afficher_logs(logs)
# elif choix == "2":
#   ip = input("Entrez l'adresse IP : ")
#   filtered_logs = filtrer_par_ip(logs, ip)
#   afficher_logs(filtered_logs)
# elif choix == "3":
#   heure = input("Entrez l'heure au format [DD/MMM/YYYY:HH:MM:SS +0000] : ")
#   filtered_logs = filtrer_par_heure(logs, heure)
#   afficher_logs(filtered_logs)
# elif choix == "4":
#   filtered_logs = filtrer_par_type_requete(logs, "POST")
#   afficher_logs(filtered_logs)
# elif choix == "5":
#   filtered_logs = filtrer_par_type_requete(logs, "GET")
#   afficher_logs(filtered_logs)
# elif choix == "6":
#   navigateur = input("Entrez le type de navigateur : ")
#   filtered_logs = filtrer_par_navigateur(logs, navigateur)
#   afficher_logs(filtered_logs)
# else:
#   print("Choix invalide.")

# -----------------------------Ancien Menu-----------------------------#