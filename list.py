drink = ["coca", "coffee" , "tea", "mile"]
print(drink)  #show iteam in list

drink.append("sting") #added iteam in the list
print(drink)

drink.sort() #set title from A->Z
print(drink)

drink.pop() #delete item the end
print(drink)

drink.insert(2,"sting") #add item can set index
print(drink)

drink1=drink.copy() #make new variable wanna copy
print(drink1)

drink2= drink.index("coca") #show location index
print(drink2)

drink.remove("coca") #rempove item
print(drink)

drink.clear() #clear all item in the list
print(drink)