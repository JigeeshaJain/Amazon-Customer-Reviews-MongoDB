import pymongo
import matplotlib.pyplot as plt
import numpy as np
myclient=pymongo.MongoClient("mongodb://localhost:27017/")
database=myclient["Project3"]
collection=database["ConsumerReview"]


def black_friday_check(review):
    review_list = []

    for char in review.split(" "):
        review_list.append(char)
  
    for key, value in enumerate(review_list):
        try:
            if value.lower() == "black" and review_list[key +1][0:6].lower() == "friday":
                return True
        except:
            continue
    return False


def enter_value(choice):
    
    if choice == 1:
        Q1=[1,2,3,4]
        Q2=[5,6,7,8]
        Q3=[9,10,11,12]

        countQ1=0
        countQ2=0
        countQ3=0
        addcounterQ1=0
        addcounterQ2=0
        addcounterQ3=0

        input_year = str(input("Enter the year:")) 

        for row in collection.find():  # all the data in row 
            Month=(row["ReviewDate"][5:7]) # fetching only the dtaa belonging to column review date
            if int(Month) in Q1 and row["ReviewDate"][0:4] == input_year:
                countQ1+=row["Ratings"]
                addcounterQ1+=1
                
            elif int(Month) in Q2 and row["ReviewDate"][0:4] == input_year:
                countQ2+=row["Ratings"]
                addcounterQ2+=1
                
        
            elif int(Month) in Q3 and row["ReviewDate"][0:4] == input_year:
                countQ3+=row["Ratings"]
                addcounterQ3+=1
                
        
        avgQ1=(countQ1/addcounterQ1) if addcounterQ1 else "No Data" 
        avgQ2=(countQ2/addcounterQ2) if addcounterQ2 else "No Data"
        avgQ3=(countQ3/addcounterQ3) if addcounterQ3 else "No Data"
        
            #print(type(row["RecommendReview"]))
        print("The average of Quarter 1 for the given year is: ",avgQ1)
        print("The average of Quarter 2 for the given year is: ",avgQ2)
        print("The average of Quarter 3 for the given year is: ",avgQ3)
        
        return
        
    if choice == 2:
        input_product = str(input("Enter the product:"))
        input_year = str(input("Enter the year:")) 
        avg_rating=0
        sum_rating = 0 
        addCounter = 0
        
        for row in collection.find():  # all the data in row 
            if row["ProductName"] == input_product and row["ReviewDate"][0:4] == input_year:
                sum_rating+=row["Ratings"]
                addCounter+=1
                avg_rating = (sum_rating/addCounter)
        print(avg_rating)
        
        return
    if choice == 3:
        first_year = str(input("Enter the year:")) 
        second_year = str(input("Enter the year:")) 

        first_counter = 0
        second_counter = 0 

        for row in collection.find():
            if row["ReviewDate"][0:4] == first_year:
                if black_friday_check(row["ReviewText"]):
                    first_counter +=1
    
            if row["ReviewDate"][0:4] == second_year:
                if black_friday_check(row["ReviewText"]):
                    second_counter +=1

        print(first_counter)
        print(second_counter)
        
        x=np.array([first_year,second_year])
        y=np.array([first_counter,second_counter])
                
        plt.bar(x,y,width=0.5)
        plt.show()
        
        return
    
    if choice == 4:
        dict_kindle = {
    "2010" : 0,
    "2011" : 0,
    "2012" : 0,
    "2013" : 0,
    "2014" : 0,
    "2015" : 0,
    "2016" : 0,
    "2017" : 0,    
 } 
 
        for row in collection.find():
            kindle_list = []
            counter = 0 
    
            for char in row["ProductName"].split(" "):
                kindle_list.append(char)
        
            for key, value in enumerate(kindle_list):
                if value[0:6].lower() == "kindle" and row["Ratings"] > 3:
                    dict_kindle[row["ReviewDate"][0:4]] = dict_kindle[row["ReviewDate"][0:4]] + 1
            
            
        print(dict_kindle)
        
        return
    
    if choice == 5:
        Q1=[1,2,3,4]
        Q2=[5,6,7,8]
        Q3=[9,10,11,12]

        countQ1=0
        countQ2=0
        countQ3=0
        addcounterQ1=0
        addcounterQ2=0
        addcounterQ3=0


        input_year = str(input("Enter the year:")) 
        
        for row in collection.find():  # all the data in row 
            Month=(row["ReviewDate"][6:7]) # fetching only the dtaa belonging to column review date
            if int(Month) in Q1 and row["ReviewDate"][0:4] == input_year:
                countQ1+=row["Ratings"]
                addcounterQ1+=1
                avgQ1=(countQ1/addcounterQ1)
                
            elif int(Month) in Q2 and row["ReviewDate"][0:4] == input_year:
                countQ2+=row["Ratings"]
                addcounterQ2+=1
                avgQ2=(countQ2/addcounterQ2)
        
            elif int(Month) in Q3 and row["ReviewDate"][0:4] == input_year:
                countQ3+=row["Ratings"]
                addcounterQ3+=1
                avgQ3=(countQ3/addcounterQ3)
                
    
        
        print("The average of Quarter 1 for the given year is: ",avgQ1)
        print("The average of Quarter 2 for the given year is: ",avgQ2)
        print("The average of Quarter 3 for the given year is: ",avgQ3)
        
        x=np.array(["Q1","Q2","Q3"])
        y=np.array([avgQ1,avgQ2,avgQ3])
                
        plt.bar(x,y, width=0.5)
        plt.show()
        
        
        
    return    

while True:
    
    choice = int(input("Enter the number between 1 and 5 as a choice and choice 6 for exit:"))
    
    if choice == 6:
        break
    else:
        enter_value(choice)
  