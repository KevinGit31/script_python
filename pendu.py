def bienvenue_dans_le_jeu_du_pendu():
    word_to_find = "Calibrer"  # on initialise le mot à trouver
    nb_try = len(word_to_find)  # on va initialiser un nombre de tentatives
    word_to_find_final = [word_to_find[0]]
    word_user = init_word_to_find_user(nb_try, word_to_find_final)
    while nb_try >= 1 and word_to_find != "".join(word_user):
        print("Vous avez {} tentatives ".format(nb_try))
        print(word_user)
        letter_by_user = input("Saisissez une lettre : ")
        if verif_saisie_user(letter_by_user):
            if letter_by_user in word_to_find:
                word_user = build_word_user(letter_by_user, word_to_find, word_user)
                print("Trouvé")
            else:
                print("Perdu")
                nb_try -=1
        else:
            print("Veuillez saisir une seule lêtre: ")
            nb_try -= 1
    print("Félicitation le mot à trouver était: " + word_to_find)


# on va verifier si l'utilisateur a bien saisi un seul caratère
def verif_saisie_user(letter):
    """
    This method verify if user input one letter and not a word or many letter
    :param letter:
    :return: boolean
    """
    if len(letter) > 1:
        return False
    return True


def init_word_to_find_user(nb_try, word_to_find_final):
    """
    TODO
    :param nb_try:
    :param word_to_find_final:
    :return:
    """
    for i in range(nb_try-1):
        word_to_find_final.append("_")
    return word_to_find_final


def build_word_user(letter_by_user, word_to_find_list, word_user):
    """
    Count how many time a word in word to find & building new word
    :param word_to_find_list:
    :param letter_by_user:
    :param word_user:
    :return:
    """
    for index, value in enumerate(word_to_find_list):
        if value == letter_by_user:
            word_user[index] = letter_by_user
    return word_user


bienvenue_dans_le_jeu_du_pendu()
