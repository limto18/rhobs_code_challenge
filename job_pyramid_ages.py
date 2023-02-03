from rhobs_code_challenge.connection import collection,get_database
from pandas import DataFrame
import matplotlib.pyplot as plt

def get_age_pyramid_for_a_job(job="psychanalyste"):
    """
        *Fonction qui prend en paramètre un métier et qui renvoie la pyramide des âges pour ce métier    
    """
    people = collection()
    sex = "F","M"
    women = people.aggregate(
    [{
        "$addFields":{"birth_date":{"$toDate":"$birthdate"}}
    },
    {
    "$match":{
        "job":job,
        "sex":sex[0]
    }  
    },
    {
    "$project" : 
        {"_id" : "$sex",
        "age": { "$dateDiff": { "startDate": "$birth_date", "endDate": "$$NOW", "unit": "year" }}
        
        }
    },
    {
    "$group" : 
        {"_id" : "$age",
            "total_worker" : {"$sum" : 1},
        }
    },
    {
    "$addFields":
        {
            "sex":sex[0],
        }
    },
    {
        "$sort": { "_id": -1 },
    },
    # {
    #     "$limit": 10
    # }
    ])

    men = people.aggregate(
    [{
        "$addFields":{"birth_date":{"$toDate":"$birthdate"}}
    },
    {
    "$match":{
        "job":job,
        "sex":sex[1]
    }  
    },
    {
    "$project" : 
        {"_id" : "$sex",
        "age": { "$dateDiff": { "startDate": "$birth_date", "endDate": "$$NOW", "unit": "year" }}
        
        }
    },
    {
    "$group" : 
        {"_id" : "$age",
            "total_worker" : {"$sum" : 1},
        }
    },
    {
    "$addFields":
        {
            "sex":sex[1],
        }
    },
    {
        "$sort": { "_id": -1 },
    },
    # {
    #     "$limit": 10
    # }
    ])

    print(f"pyramid ages of {job} job")
    # for i in men:
    #     print(i)
    # for i in women:
    #     print(i)
    return women,men

def plot_pyramid(men_df,women_df):
    men_age,men_number = men_df['_id'],men_df['total_worker']
    women_age,women_number = women_df['_id'],women_df['total_worker']

    fig, ax = plt.subplots(figsize=(8,8))
    ValH = ax.barh(men_age, men_number, 1, label="Hommes",
                color='b', linewidth=0, align='center')
    ValF = ax.barh(women_age, -women_number, 1, label="Femmes",
                color='r', linewidth=0, align='center')
    #diff, = ax.plot(somme, arange(len(femmes)), 'y', linewidth=2)
    ax.set_title("Pyramide des âges")
    ax.set_ylabel("Ages")
    ax.set_xlabel("Employés")
    ax.set_ylim([0, 110])
    ax.legend((ValH[0], ValF[0]), ('Hommes', 'Femmes'))
    plt.show()

if __name__ == "__main__": 
    db = get_database()
#Fonction qui prend en paramètre un métier et qui renvoie la pyramide des âges pour ce métier
    F,M = get_age_pyramid_for_a_job()

    #convert output to pandas dataframe for better visualisation
    men_df = DataFrame(F)
    women_df = DataFrame(M)
    print(men_df)
    print(women_df)
    plot_pyramid(men_df,women_df)

