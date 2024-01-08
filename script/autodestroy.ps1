# Chemin du fichier contenant la date
$cheminFichierDate = "date.txt"

# Chemin du dossier à supprimer
$dossierASupprimer = "C:\Windows-office"

# Lire la date depuis le fichier
$dateTexte = Get-Content -Path $cheminFichierDate

# Convertir la date texte en objet DateTime
$date = Get-Date $dateTexte -Format "MM/dd/yyyy"

# Obtenir la date actuelle
$dateActuelle = Get-Date

# Comparer les dates
if ($date -le $dateActuelle) {
    # Supprimer le dossier s'il existe
    if (Test-Path $dossierASupprimer -PathType Container) {
        Remove-Item -Path $dossierASupprimer -Recurse -Force
        Write-Host "Le dossier $dossierASupprimer a été supprimé."
    } else {
        Write-Host "Le dossier $dossierASupprimer n'existe pas."
    }
} else {
    Write-Host "La date dans le fichier est postérieure à la date actuelle."
}
