import json
import os

# Charger le fichier JSON
json_file_path = 'data/screaming_frog_data.json'
if not os.path.exists(json_file_path):
    raise FileNotFoundError(f"Le fichier JSON n'existe pas : {json_file_path}")

with open(json_file_path, 'r') as file:
    data = json.load(file)

# Initialiser une liste pour stocker les erreurs
errors = []

# Parcourir les données pour trouver les erreurs
for page in data:
    url = page.get('"Address"')
    status_code = page.get('Status Code')
    indexability = page.get('Indexability')
    title = page.get('Title 1')
    meta_description = page.get('Meta Description 1')

    # Erreurs d'indexation
    if indexability in ["Non-Indexable", "Bloqué par robots.txt"]:
        errors.append((url, 'Erreur d\'indexation', indexability))

    # Balises manquantes
    if not title:
        errors.append((url, 'Titre manquant'))
    if not meta_description:
        errors.append((url, 'Meta description manquante'))

    # Statuts HTTP
    if status_code not in ['200', '301', '302']:
        errors.append((url, 'Statut HTTP', status_code))

# Afficher les erreurs détectées
print("Erreurs détectées :")
for error in errors:
    print(error)
