Mot = "physique"
Phrase = "J'aime la physique."

def recherer_mot(mot, phrase):
    for i in range(len(phrase)):
        correspondance = ""
        for j in range(len(mot)):
            try:
                if phrase[i+j] == mot[j]:
                    correspondance = correspondance + mot[j]
            except:
                pass
        if correspondance == mot:
            return True
    return False

if recherer_mot(Mot, Phrase):
    print("Le mot est bien dans la phrase.")
else:
    print("Le mot n'est pas dans la phrase.")