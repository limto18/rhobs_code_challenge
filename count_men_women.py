from rhobs_code_challenge.connection import collection,get_database

def count_men_women():
    """
        *Cette fonction compte le nombre de femmes / d'hommes dans la collection.
    """
    people = collection()
    male = list(people.find({'sex':'M'}))
    female = list(people.find({'sex':'F'}))

    print(f"Nombres de femmes:{len(female)} \nNombres d'hommes:{len(male)}")

    return {'M':len(male),'F':len(female)}

if __name__ == "__main__": 
    db = get_database()
  
#Compte le nombre de femmes / d'hommes. 
    men_women = count_men_women()