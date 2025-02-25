import openai
import os
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Charger la clé API depuis la variable d'environnement
openai.api_key = os.getenv("OPENAI_API_KEY")

if openai.api_key is None:
    raise ValueError("❌ Clé API OpenAI manquante. Assurez-vous de définir la variable d'environnement OPENAI_API_KEY.")


def get_ai_recommendations(errors):
    # Formater les erreurs détectées pour l'IA
    error_list = "\n".join([f"- {error[0]} : {error[1]}" for error in errors])

    # Prompt pour l'IA
    prompt = f"""
    Tu es un expert en SEO technique. Voici une liste d'erreurs détectées :
    {error_list}

    Pour chaque erreur, fais ceci :
    - Explique pourquoi c'est un problème pour le SEO.
    - Propose une recommandation actionnable.
    - Donne un exemple de solution.
    - Adopte un ton professionnel et pédagogique.
    
    Formate ta réponse en Markdown pour un rapport professionnel.
    """

    # Appel à l'API OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Utilisation du modèle 03-mini
        messages=[
            {"role": "system", "content": "Tu es un expert en SEO technique."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=2000,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Récupérer la réponse
    ai_recommendations = response['choices'][0]['message']['content']
    return ai_recommendations
