# coding : utf-8

# Un script de Jessica Potsou

# Dans ce script, je vais faire une recherche dans les archives de La Presse
# Je vais sortir les urls des articles de février 2010 qui parlent des Jeux Olympiques de vancouver

# Je dois en premiers lieux importer les extensions requests, csv et beautifulSoup
import requests
import csv
from bs4 import BeautifulSoup

# Je donne tout de suite le nom au fichier que je veux généré
fichier = "article_jo.csv"

# Voici la constante de l'url qui me mène à la page d'une journée dans les archives (lorsque je la modifie, ce que je ferai plus tard)
# Cette variable ne sera pas réutilisée mais me servira de rappel
urldebut = "https://www.lapresse.ca/archives/2010/2/.php"

# Voici l'entête qui accompagnera ma requête
entetes = {
    "User-Agent": "Jessica Potsou - requête envoyée dans le cadre d'un cours de journalisme de données",
    "From":"potsou.jessica@courrier.uqam.ca"
}

# Je fais une liste qui contient mon range de date (en 2010, le mois de février comptait 28 jours) 
date = list(range(1,29))

# Je fais une liste de vide dans laquelle je vais ajouter plus tard mes urls d'articles
liste = []

# Je fais une boucle pour générer les urls qui mènent à la page d'une journée d'archive
for jour in date:
    # Comme mes urls seront des dates du mois de février, je modifie mon url de la façon suivante: 
    # J'utilise la fonction .format, car je dois inséré mon jour à l'intérieur de mon url et non à la fin
    urljours = "https://www.lapresse.ca/archives/2010/2/{}.php".format(jour)
    # J'ai fait un print pour voir que j'arrive bien à générer mes urls de journée... j'ai mis le print en commentaire
    # print (urljours)
    # Je fais une requête pour pouvoir moissonner mes donnés dans toutes les pages de journée
    contenu = requests.get(urljours, headers=entetes)

    # Je vais analyser mes donner avec l'aide de BeautifulSoup et sa fonction « parse »
    page = BeautifulSoup(contenu.text, "html.parser")

    # Je forme une seconde boucle pour trouver mes urls d'article pour chaque journée du mois de février 2010
    # J'ai trouver la formule suivante (les deux prochaines lignes) sur internet... elle me permet de sortir l'url de chaque article du mois
    for article in page.find("ul", class_="square square-spread").find_all("a") :
        urlarticle = article.get('href')
        # J'ai fait un print pour vérifier que ma formule fonctionne... J'ai mis le print en commentaire
        # print (urlarticle)

        # J'ai fait une condition pour trouver les urls de tous les articles qui parlent des JO de Vancouver
        # Il y a une constance dans tous ces urls... ils contiennent tous la chaine de caractères « vancouver-2010 »
        if "vancouver-2010" in urlarticle:
            jo = urlarticle
            # J'ai fait un print pour m'assurer que ma condition fonctionne, je l'ai mis en commentaire
            # print (jo)
            # J'ai utilisé la fonction .split pour séparer chaque url
            jeux = jo.split(',')
            # J'ai ajouté mes urls séparés à ma liste de vide en utilisant la fonction .append
            liste.append(jeux)

# J'ai créé mon fichier csv à partir de ma liste contenant mes urls d'articles sur les Jeux Olympiques de Vancouver 2010
c1 = open(fichier, "a")
c2 = csv.writer(c1)
c2.writerow (liste)
