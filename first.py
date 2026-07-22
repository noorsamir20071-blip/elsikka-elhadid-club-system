"""
this is the same use of hashtag (#)
for study 
i will be great at this insha'allah
print("iam nour")
int = 10-2
print(int)
string1 = "my name is nour "
string2 = "my last name is samir "
print (string1) 
print (string2) 
age =10
has_license = True

if age >=18 and has_license :
    print ("you can drive" )
else:
    print ("you cannot drive" )
    for i in range(5):
    print(i)
else:
  for  z in range (9):
    print (z)

print (i*z)


person = {
"name" : "nour",
"age"  :   19  ,
"study": "cs " ,
"city" : "cairo"
}
print(person)





def nour():
    print ("hi there  ")

person = {
"name" : "nour",
"age"  :   19  ,
"study": "cs " ,
"city" : "cairo"
}
print(person)




nour()



def calc (tax_price  , price , discount ):
    tax = price * tax_price 
    final_price = price + tax - discount
    print (f"total {final_price}")

calc (.5, 1000, 700)

import random 
number = random.randint (1 , 20)
print(number)
choice = random.choice(["apple", "banana", "choclate", "burger"])
print(choice)
name = random.choice(["ahmed" ,"nour" ,"zeyad" ,"adam" ,"mai" ,"yassin" ,"body"])
print(name)
import requests


url = "https://open.er-api.com/v6/latest/USD"
respond = requests.get(url)
price = respond.json()

live_usa_rate = price["rates"]["USD"]
live_egp_rate = price["rates"]["EGP"]

print(f"dollar Price: {live_usa_rate} USD")
print(f"egp Price: {live_egp_rate} EGP")

amount = float(input("Enter dollar amount: "))

total_egp = amount * live_egp_rate
print(f"Total Value: {total_egp} EGP")
"""
