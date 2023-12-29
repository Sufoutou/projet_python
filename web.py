from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'sdfsfezvzgreggrfgerg'

# Vos fonctions d'analyse de logs ici...

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        fichier = request.files['file']
        # Lire les logs à partir du fichier spécifié
        logs = fichier.readlines()
        # Sauvegarder les logs dans la session
        session['logs'] = logs
        return redirect(url_for('home'))
    return render_template('index.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    logs = session.get('logs', [])
    if request.method == 'POST':
        choix = int(request.form.get('choix'))
        if choix == 1:
            resultats = afficher_logs(logs)
        elif choix == 2:
            ip = request.form.get('ip')
            resultats = filtrer_par_ip(logs, ip)
        elif choix == 3:
            heure = request.form.get('heure')
            resultats = filtrer_par_heure(logs, heure)
        elif choix == 4:
            resultats = filtrer_par_type_requete(logs, "POST")
        elif choix == 5:
            resultats = filtrer_par_type_requete(logs, "GET")
        elif choix == 6:
            navigateur = request.form.get('navigateur')
            resultats = filtrer_par_navigateur(logs, navigateur)
        else:
            resultats = []
        return render_template('resultats.html', resultats=resultats)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
