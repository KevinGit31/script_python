def bienvenue_dans_le_jeu_du_pendu():
    nb_try = 7  # on va initialiser un nombre de tentatives
    word_to_found = "calibrer"  # on initialise le mot à trouver
    while nb_try >= 1:
        print("Vous avez {} tentatives ".format(nb_try))
        mot = input("Saisissez un mot: ")
        if word_to_found == mot:
            print("Trouvé")
            break
        nb_try -=1


bienvenue_dans_le_jeu_du_pendu()
