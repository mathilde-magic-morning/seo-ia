def generate_report(errors, recommendations):
    report = "# Rapport d'Audit SEO Technique\n\n"

    report += "## Erreurs détectées :\n"
    for error in errors:
        url, issue, details = error[0], error[1], error[2] if len(error) > 2 else ""
        report += f"- **{issue}** sur [{url}]({url}) {details}\n"

    report += "\n## Recommandations SEO :\n"
    report += recommendations  # Ajoute le contenu généré par l'IA

    report += "\n## Conclusion :\n"
    report += "En appliquant ces recommandations, vous améliorerez la visibilité SEO et l'expérience utilisateur."

    with open("seo_report.md", "w") as file:
        file.write(report)

    print("✅ Rapport SEO généré : seo_report.md")
