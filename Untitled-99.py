def calculer_couts(duree_communication):
    offres = [
        {"abonnement": "Illimité", "minutes_gratuites": 200, "cout_minute": 0},
        {"abonnement": "2h", "minutes_gratuites": 120, "cout_minute": 0.5},
        {"abonnement": "1h", "minutes_gratuites": 60, "cout_minute": 1},
        {"abonnement": "30min", "minutes_gratuites": 30, "cout_minute": 1.5},
        {"abonnement": "0", "minutes_gratuites": 0, "cout_minute": 2},
    ]

    couts_mensuels = []
    for offre in offres:
        minutes_gratuites = offre["minutes_gratuites"]
        cout_minute = offre["cout_minute"]
        
        if duree_communication <= minutes_gratuites:
            cout_mensuel = 0
        else:
            cout_mensuel = (duree_communication - minutes_gratuites) * cout_minute
        
        couts_mensuels.append(cout_mensuel)
    
    return couts_mensuels

def afficher_menu():
    while True:
        print("\nMenu principal:")
        print("1- Saisir la durée de communication")
        print("2- Afficher la liste du coût mensuel par offre")
        print("3- Afficher l'offre la plus intéressante (moindre coût)")
        print("4- Quitter le programme")

        choix = input("Choisissez une option (1/2/3/4) : ")

        if choix == '1':
            duree_communication = int(input("Entrez la durée de communication du mois en minutes : "))
        elif choix == '2':
            if 'duree_communication' in locals():
                couts = calculer_couts(duree_communication)
                for i, offre in enumerate(couts, 1):
                    print(f"Offre {i}: {offre} DH")
            else:
                print("Veuillez d'abord saisir la durée de communication (option 1).")
        elif choix == '3':
            if 'duree_communication' in locals():
                couts = calculer_couts(duree_communication)
                offre_interessante = couts.index(min(couts)) + 1
                print(f"L'offre la plus intéressante est l'offre {offre_interessante}.")
            else:
                print("Veuillez d'abord saisir la durée de communication (option 1).")
        elif choix == '4':
            break
        else:
            print("Option invalide. Veuillez choisir une option valide.")

if __name__ == "__main__":
    afficher_menu()
