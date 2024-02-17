nb_vies = 7

mot_mystere = 'python'

mot_public = '_' * len(mot_mystere)

while nb_vies > 0 and mot_mystere != mot_public:
    lettre = input('Entrez une lettre : ')
    if lettre in mot_mystere:
        for i in range(len(mot_mystere) ):
            if mot_mystere[i] == lettre:
                mot_public = mot_public[:i] + lettre + mot_public[i + 1:]
    else:
        nb_vies -= 1
    if mot_public == mot_mystere:
        print ("Bravo! Le mot est", mot_mystere)
    elif nb_vies == 0:
        print("Vous avez perdu")
    else:
        print ("Vous avez", nb_vies)
        print("Le mot est :",mot_public)
