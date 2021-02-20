"""
    by Hokanosekai v1.0
    Ce programme encode le mot entrez en T9
    Tous droits réservés © 2021
"""
#
# Definition de la fonction prennant en paramètre :
#   - le mot à encoder
#   - le chiffrement T9
def chiffrageT9(mot,keys):

    # Déclaration de variables
    mot_encode = ""

    # Notre mot sous forme de liste
    list_mot = list(mot)

    # Pour toutes les lettres dans notre liste
    for k,letter_mot in enumerate(list_mot):

        # Pour toutes les correspondance de l'encodage T9
        for i,keys_letters in enumerate(keys.items()):

            # Pour toutes les lettres de chaque éléments de l'encodage T9
            for z,letter in enumerate(keys_letters[1]):

                # Si la lettre du mot est égale à une lettre dans l'élément de l'encodage T9
                if letter_mot == letter:

                    # On ajoute le numéro correspondant de l'encodage T9 à la lettre
                    mot_encode += str(keys_letters[0])

    # On affiche le résultat
    print(mot + " -> " + mot_encode)


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
chiffrageT9(str(input("mot à encodé en T9 -> ")).lower(), keys)