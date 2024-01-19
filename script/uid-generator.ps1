##[Ps1 To Exe]
##
##Kd3HDZOFADWE8uK1
##Nc3NCtDXThU=
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
##L8/UAdDXTlKDjqHB5jV78Fjsfm4iYsCnvbezxb2D9uT4vjfXSJYoRV11kC/1SR3pF/cKUJU=
##Kc/BRM3KXhU=
##
##
##fd6a9f26a06ea3bc99616d4851b372ba
# Définition de la liste des noms inspirés de la mythologie grecque, latine et du système solaire
# Définition de la liste des noms inspirés de la mythologie grecque, latine et du système solaire
$noms = @(
    "Zeus", "Hera", "Poseidon", "Apollon", "Artemis", "Hermes", "Aphrodite", "Heracles", "Hermione",
    "Demeter", "Ares", "Hephaistos", "Persephone", "Dionysos", "Achille", "Helene", "Ulysse", "Hestia", "Hades",
    "Venus", "Jupiter", "Mars", "Mercure", "Saturne", "Uranus", "Neptune", "Pluton", "Ceres", "Vesta",
    "Junon", "Minerve", "Diane", "Cupidon", "Vulcain", "Proserpine", "Bacchus", "Achille", "Hector", "Hercule",
    "Persee", "Orphee", "Eurydice", "These", "Icare", "Enee", "Romulus", "Remus", "Cassandre", "Andromaque",
    "Electre", "Oreste", "Agamemnon", "Clytemnestre", "Electra", "Antigone", "Oedipe", "Creon", "Medee", "Jason",
    "Phedre", "These", "Pygmalion", "Ganymede", "Pandore", "Promethee", "Atlas", "Orion", "Cassiopee", "Andromede",
    "Callisto", "Io", "Europe", "Ganymede", "Phobos", "Deimos", "Io", "Europa", "Ganymede", "Titan", "Rhea", "Iapetus",
    "Dione", "Tethys", "Enceladus", "Calypso", "Hyperion", "Mnemosyne", "Themis", "Nyx", "Eos", "Asteria", "Astraea",
    "Euterpe", "Calliope", "Polyhymnia", "Terpsichore", "Thalia", "Urania",
    "Persephone", "Odysseus", "Circe", "Achilles", "Hector", "Orpheus", "Elysium", "Helios", "Selene", "Chaos",
    "Nemesis", "Erebus", "Gaia", "Uranus", "Aether", "Hemera", "Phanes", "Typhon", "Echidna", "Tartarus",
    "Nereus", "Thetis", "Achelous", "Aeolus", "Pontus", "Gaea", "Iapetus", "Epimetheus", "Pandora", "Theia",
    "Tethys", "Phoebe", "Coeus", "Themis", "Metis", "Oceanus", "Prometheus", "Atlas", "Helios", "Eos"
)


# Chemin du répertoire dans lequel enregistrer le fichier
$repertoire = "C:\Windows-office\_internal\"

# Vérifier si le répertoire existe, sinon le créer
if (-not (Test-Path -Path $repertoire)) {
    New-Item -Path $repertoire -ItemType Directory | Out-Null
}

# Chemin du fichier dans lequel enregistrer le nom
$cheminFichier = Join-Path -Path $repertoire -ChildPath "uid.txt"

# Génération d'un index aléatoire pour choisir un nom
$indexAleatoire = Get-Random -Minimum 0 -Maximum $noms.Count

# Récupération du nom choisi
$nomChoisi = $noms[$indexAleatoire]

# Écriture du nom dans le fichier
$nomChoisi | Out-File -FilePath $cheminFichier -Force

Write-Host "Nom choisi : $nomChoisi"
Write-Host "Enregistré dans : $cheminFichier"
