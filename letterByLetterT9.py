"""
    by Hokanosekai v1.0
    Ce programme affiche les mots correspondant à l'encodage T9 en fonction du numéro que vous entrez
    Tous droits réservés © 2021
"""
#
# Definition de la fonction prennant en paramètre :
#   - une liste de mots
#   - le chiffrement T9
def letterByLetterT9(dico,keys):

    # Déclaration de variables
    free_words = dico

    # chaine avec tous les inputs entrez
    chiffres = ""

    # lettre dans le mot, aussi index correspondant a l'élément dans la liste key_inputs
    # à 0 on prend la première lettre du mot ainsi de suite
    lettres = 0

    # On boucle tant que la longueur de notre liste de mots restants est superieur à 0
    while len(free_words) > 0:

        # liste temporaire de mots restants
        last_words = []

        # Input du numéro correspondant à l'encodage T9
        key_input = int(input("-> "))

        # On ajoute l'input a la chaine
        chiffres += str(key_input)

        # Pour chaque lettres correspondant au numéro de l'encodage T9 (key_input)
        for i,c in enumerate(keys.get(key_input)):

            # Pour chaque mot dans le dictionaire
            for index,mot in enumerate(free_words):

                # Si la longueur du mot est supérieur aux nombre de lettres
                # ET
                # que la lettre est égale à la lettre dans le mot
                if len(mot) > lettres and c == mot[lettres]:

                    # On ajoute ce mot dans la liste temporaire
                    last_words.append(mot)

        # On incrémente pour passer a la lettre suivante
        lettres += 1
        # On écrase notre liste de mot par la nouvelle
        free_words = last_words

        # On récupère les 10 plus petis mots des mots restants
        if len(free_words) > 0:
            mins = []
            for i in range(10):
                min = len(free_words[0])
                test = free_words[0]
                for i,val in enumerate(free_words):
                    if len(val) < min:
                        min = len(val)
                        test = val
                mins.append(test)
                free_words.remove(test)

        # On affiche certaines informations
        print(mins, "\nmots restants " + str(len(free_words)),"\n" + str(keys.get(key_input)), "\nnombres de lettres " + str(lettres), "\nchiffres " + str(chiffres))

# On crée une liste qui va contenir tous nos mots
dico=[]

# On ajoute chaque mots du fichier dico.txt a notre liste dico
with open('dico.txt','r') as f:
    for ligne in f:
        dico.append(ligne.rstrip('\n'))

# Dictionaire correspondant à notre encodage en T9
keys = {
           2 : {"a","b","c"},
           3 : {"d","e","f"},
           4 : {"g","h","i"},
           5 : {"j","k","l"},
           6 : {"m","n","o"},
           7 : {"p","q","r","s"},
           8 : {"t","u","v"},
           9 : {"w","x","y","z"}
        }

# On affiche l'encodage
for key,valeur in keys.items():
    print(key,valeur)

# On appel notre fonction en lui passant notre liste dico et notre dictionaire keys
letterByLetterT9(dico,keys)