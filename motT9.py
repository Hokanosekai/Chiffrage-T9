"""
    by Hokanosekai v1.0
    Ce programme affiche les mots correspondant à l'encodage T9 que vous entrez
    Tous droits réservés © 2021
"""
#
# Definition de la fonction prennant en paramètre :
#   - les touches encodé en T9
#   - une liste de mots
#   - le chiffrement T9
def motT9(key_inputs, dico, keys):

    # Déclaration de variables
    free_words = dico

    # liste temporaires
    last_words = []

    # lettre dans le mot, aussi index correspondant a l'élément dans la liste key_inputs
    # à 0 on prend la première lettre du mot ainsi de suite
    nb_lettres = 0

    # Pour chaque numéro entrés
    for z,key in enumerate(key_inputs):

        # Pour chaque lettres correspondant au numéro de l'encodage T9 (keys)
        for i,lettre in enumerate(keys.get(int(key))):

            # Pour chaque mot dans le dictionaire
            for x,mot in enumerate(free_words):

                # Si la longueur du mot est supérieur aux nombre de lettres
                # ET
                # que la lettre est égale à la lettre dans le mot
                if len(mot) > nb_lettres and lettre == mot[nb_lettres]:

                    # On ajoute ce mot dans la liste temporaire
                    last_words.append(mot)

        # On incrémente pour passer a la lettre suivante
        nb_lettres += 1
        # On écrase notre liste de mot par la nouvelle
        free_words = last_words
        # On remet la liste à 0
        last_words = []

    # On récupère uniquement les mots égaux à la longueur de key_inputs
    ten_words = []
    for i,mot in enumerate(free_words):
        if len(mot) == len(key_inputs):
            ten_words.append(mot)

    # On affiche / retourne les mots correspondants aux chiffres de key_inputs
    print(ten_words)

# On crée une liste qui va contenir tous nos mots
dico = []
# On ajoute chaque mots du fichier dico.txt a notre liste dico
with open('dico.txt','r') as f:
    for ligne in f:
        dico.append(ligne.rstrip('\n'))

# Dictionaire correspondant à notre encodage en T9
keys = {
           2: {"a", "b", "c"},
           3: {"d", "e", "f"},
           4: {"g", "h", "i"},
           5: {"j", "k", "l"},
           6: {"m", "n", "o"},
           7: {"p", "q", "r", "s"},
           8: {"t", "u", "v"},
           9: {"w", "x", "y", "z"}
        }
# On affiche l'encodage
for key, valeur in keys.items():
    print(key, valeur)

# On appel notre fonction en lui passant notre liste dico, notre dictionaire keys et une liste de notre numéro
motT9(list(str(input("mot encodé en T9 -> "))), dico, keys)

