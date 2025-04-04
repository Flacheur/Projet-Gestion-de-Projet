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