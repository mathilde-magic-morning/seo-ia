from analyzer import errors
from ai_recommender import get_ai_recommendations
from reporter import generate_report

# Lancer l'analyse technique
print("🔎 Analyse technique en cours...")
print("⚙️ Détection des erreurs SEO...")

# Appel à l'IA pour les recommandations
print("🧠 Génération des recommandations avec l'IA...")
ai_recommendations = get_ai_recommendations(errors)

# Générer le rapport SEO
generate_report(errors, ai_recommendations)
