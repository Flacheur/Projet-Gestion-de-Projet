import time, datetime

#créer 10 plats avec noms, prix, allergène
#role acheteur
#role restaurateur
#menu avec choix 1 buyer / 2 resto / menu pour naviguer dans les plats, pour revenir dans les autrs menus



# Liste des plats disponibles
plats = [
    {"nom": "Pizza Margherita", "prix": 10.99, "allergenes": ["Gluten", "Lactose"]},
    {"nom": "Pâtes Carbonara", "prix": 12.50, "allergenes": ["Gluten", "Lactose"]},
    {"nom": "Salade César", "prix": 9.99, "allergenes": ["Lactose"]},
    {"nom": "Burger classique", "prix": 11.50, "allergenes": ["Gluten"]},
    {"nom": "Sushi saumon", "prix": 15.00, "allergenes": ["Poisson", "Soja"]},
    {"nom": "Ratatouille", "prix": 8.50, "allergenes": []},
    {"nom": "Tacos", "prix": 9.00, "allergenes": ["Gluten"]},
    {"nom": "Soupe à l'oignon", "prix": 7.50, "allergenes": ["Lactose"]},
    {"nom": "Crêpes sucrées", "prix": 5.50, "allergenes": ["Gluten", "Lactose"]},
    {"nom": "Tarte au citron", "prix": 6.00, "allergenes": ["Gluten", "Lactose"]}
]

# Liste pour stocker les commandes
commandes = []

# Fonction pour afficher les plats
def afficher_plats():
    for plat in plats:
        print(plat["nom"], "-", plat["prix"], "€ - Allergènes:", ", ".join(plat["allergenes"]) if plat["allergenes"] else "Aucun")






# Fonction pour effectuer un achat


def effectuer_achat():
    panier = []
    while True:
        choix = input("Entrez le nom du plat à commander (ou 'fin' pour terminer) : ")
        if choix == 'fin':
            break
        plat_trouve = False
        for plat in plats:
            if plat["nom"] == choix:
                panier.append(plat)
                plat_trouve = True
                break
        if not plat_trouve:
            print("Plat non trouvé.")
    
    total = 0
    for plat in panier:
        total += plat["prix"]
    print("Total à payer :", total, "€")
    
    if input("Valider la commande ? (o/n) : ") == 'o':
        commande = {
            "plats": panier,
            "heure": datetime.datetime.now(),
            "statut": "en préparation",
            "numero": len(commandes) + 1,
            "prix": total
        }
        commandes.append(commande)
        print("Commande validée. Numéro de commande :", commande["numero"])
    else:
        print("Commande annulée.")



# Fonction pour vérifier une commande


def verifier_commande():
    numero = int(input("Entrez le numéro de commande : "))
    commande_trouvee = False
    for commande in commandes:
        if commande["numero"] == numero:
            print("Commande n°", commande["numero"])
            print("Plats :", ", ".join([plat["nom"] for plat in commande["plats"]]))
            print("Heure :", commande["heure"])
            print("Statut :", commande["statut"])
            commande_trouvee = True
            break
    if not commande_trouvee:
        print("Commande non trouvée.")


# Fonction pour annuler une commande


def annuler_commande():
    numero = int(input("Entrez le numéro de commande : "))
    for commande in commandes:
        if commande["numero"] == numero:
            if commande["statut"] == 'en préparation':
                temps_ecoule = (datetime.datetime.now() - commande["heure"]).total_seconds()
                if temps_ecoule > 120:
                    commande["statut"] = 'annulée'
                    print("Commande annulée.")
                else:
                    print("Impossible d'annuler. Moins de 2 minutes se sont écoulées.")
            else:
                print("Impossible d'annuler. La commande n'est plus en préparation.")
            return
    print("Commande non trouvée.")


#Fonction pour afficher la commande demandé

def afficher_commandes():
    commande_a_preparer = False
    for commande in commandes:
        temps_ecoule = (datetime.datetime.now() - commande["heure"]).total_seconds()
        if commande["statut"] == 'en préparation':
            print("Commande n°", commande["numero"])
            print("Plats :", ", ".join([plat["nom"] for plat in commande["plats"]]))
            print("Heure :", commande["heure"])
            print("Temps écoulé :", temps_ecoule)
            commande_a_preparer = True
    if not commande_a_preparer:
        print("Pas de commandes à préparer.")


#Fonction pour permettre au restaurateur de valider une commande


def valider_commande():
    numero = int(input("Entrez le numéro de commande : "))
    for commande in commandes:
        if commande["numero"] == numero:
            if commande["statut"] == 'en préparation':
                commande["statut"] = "livrée"
            elif commande["statut"] == "livrée" :
                print("Cette commande à déja été livrée")
            elif commande["statut"] == "annulée" :
                print("Cette commande à été annulée")
            return
    print("Commande non trouvée.")


#Fonction permettatant au restaurateur d'avoir un bilan de ses commandes

def bilan():
    nb_commande = 0
    commandes_livree = 0
    commandes_retractee = 0
    Ca_av_retrait = 0
    Ca = 0
    pertes = 0
    for commande in commandes:
        nb_commande += 1
        Ca_av_retrait += commande["prix"]
        if commande["statut"] == "livrée" :
            commandes_livree += 1
            Ca += commande["prix"]
        if commande["statut"] == "annulée" :
            commandes_retractee += 1
            pertes += commande["prix"]
    while True:
        print("\n1. Afficher le bilan total")
        print("2. Afficher le bilan des commandes livrées")
        print("3. Afficher le bilan des commandes annulées")
        print("4. Retour")
        

        choix = input("Choisissez une option : ")

        if choix == '1':
            print(nb_commande, " commandes ont été effectué sur le site pour un total de ", Ca_av_retrait, " €.")
        elif choix == '2':
            print(commandes_livree, " commandes ont été livrées pour un total de ", Ca, " €.")
        elif choix == '3':
            print(commandes_retractee, " commandes ont été rétractées ce qui repésente un non-gain de ", pertes, " €.")
        elif choix == '4':
            return
        else:
            print("Option invalide.")



#Fonction qui contribue à ce que le restaurateur puisse ajouter des plats à son menu

def ajouter_plat():
    nom = input("Renseignez le nom du plat à ajouter : ")
    prix = float(input("Renseignez le prix du plat à ajouter : "))
    allergenes = []
    if input("Ce plat contient-il des allergenes ? (o/n) : ") == "o" :
        while True:
            allergene = input("Renseignez un des allergenes du plat (STOP pour finir de renseigner les allergenes) : ")
            if allergene == "STOP":
                break
            else :
                allergenes.append(allergene)
    plat = {
        "nom" : nom, 
        "prix" : prix,
        "allergenes" : allergenes
    }
    plats.append(plat)
    return


# Fonction qui modifie un plat, lorsque le restaurateur en a besoin


def modifier_plat():
    nom_plat = input("Renseignez le nom du plat à modifier : ")
    plat_trouve = False
    for plat in plats :
        if plat["nom"] == nom_plat :
            plat_trouve = True
            modification = input("Quelle est la modification à effectuer ? (nom/prix/allergenes)")
            if modification == "nom" :
                new_nom = input("Quel est le nouveau nom de ce plat ?")
                plat["nom"] = new_nom
            elif modification == "prix" :
                new_prix = float(input("Quel est le nouveau prix de ce plat ?"))
                plat["prix"] = new_prix
            elif modification == "allergenes" :
                new_allergenes = []
                while True:
                    new_allergene = input("Renseignez un des allergenes du plat (STOP pour finir de renseigner les allergenes) : ")
                    if new_allergene == "STOP":
                        break
                    else :
                        new_allergenes.append(new_allergene)
                plat["allergenes"] = new_allergenes
    
    if not plat_trouve:
        print("Plat non trouvé.")


#Fonction qui permet de supprimer un plat 

def supprimer_plat():
    nom_plat = input("Renseignez le nom du plat à supprimer : ")
    plat_trouve = False
    for plat in plats :
        if plat["nom"] == nom_plat :
            plat_trouve = True
            plats.remove(plat)
    
    if not plat_trouve:
        print("Plat non trouvé.")


# Menu principal


while True:
    print("\n1. Afficher les plats")
    print("2. Effectuer un achat")
    print("3. Vérifier une commande")
    print("4. Annuler une commande")
    print("5. Quitter")
    print("6. Passer en mode restaurateur")
    
    choix = input("Choisissez une option : ")
    
    if choix == '1':
        afficher_plats()
    elif choix == '2':
        effectuer_achat()
    elif choix == '3':
        verifier_commande()
    elif choix == '4':
        annuler_commande()
    elif choix == '5':
        break
    elif choix == '6':
        mdp = input("Renseignez le mot de passe : ")
        if mdp == "Admin123" :
            while True:
                print("\n1. Afficher les commandes")
                print("2. Envoyer une commande")
                print("3. Ajouter un plat à la carte")
                print("4. Modifier un plat de la carte")
                print("5. Supprimer un plat de la carte")
                print("6. Voir le bilan")
                print("7. Passer en mode client")
                choix = input("Choisissez une option : ")
    
                if choix == '1':
                    afficher_commandes()
                elif choix == '2':
                    valider_commande()
                elif choix == '3':
                    ajouter_plat()
                elif choix == '4':
                    modifier_plat()
                elif choix == '5':
                    supprimer_plat()
                elif choix == '6':
                    bilan()
                elif choix == '7':
                    break
                else:
                    print("Option invalide.")
        else:
            print("Mot de passe incorrect")
            
    else:
        print("Option invalide.")

print("Merci d'avoir utilisé notre service !")