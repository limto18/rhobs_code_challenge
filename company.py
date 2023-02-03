from rhobs_code_challenge.connection import collection,get_database

def get_company_with_more_than_n_people(n):
    """
        *Cette fonction renvoie les entreprises de plus de N personnes.
    """
    people = collection()
    company= people.aggregate(
    [{
    "$group" : 
        {"_id" : "$company",  
         "total_worker" : {"$sum" : 1}
         }},
        {
        "$match":{
            "total_worker":{"$gte":n}
        }  
        },
        {
      "$sort": { "total_worker": -1 }
   }
    ])
    print(f"Company with more than {n} workers")
    for i in company:
        print(i)

    return company

if __name__ == "__main__": 
    db = get_database()
#Fonction qui renvoie les entreprises de plus de N personnes.
    company = get_company_with_more_than_n_people(80)

