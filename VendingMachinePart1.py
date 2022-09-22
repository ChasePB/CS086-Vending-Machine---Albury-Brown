from ctypes import sizeof

import inspect
from ntpath import join
from operator import contains
import gc
import re
from turtle import done

## price input is assumed to just be entered as a float. ex 2.75 0.5 not $0.50
class Products:
    def __init__(self,name, qty, price):
        self.name=name
        self.qty=qty
        self.price=price
userInput=''
hist=[]
count=0
inv=[]
balance=0
while userInput!="exit":
    
    userInput=input("Please make a selection or type help for more options\n")
    hist.append(userInput)
    inputs=userInput.split()
    
    if len(inputs)>1:
        temp=inputs[0]
        temp2=inputs[1]
        temp3=temp+" "+temp2
        inputs[0]=temp3
        
        inputs.pop(1)

    if userInput == "help":
        print("Here is how you enter the commands")
        print("balance shows the balance")
        print("history prints list of transactions")
        print("inventory prints available items with name and ID")
        print("add item <str> <int> <float>	 for ex. add item chips 2 $1.00	add an item name qty price")
        print("buy item <str> 5 <int>	for ex. buy item chips 1 2 2 4 3	buys an item with # dollars, quarters, dimes, nickles")
        print("pennies. It also shows change given and the remaining")
        print("balance with currency distribution. For change, the machine")
        print("uses the largest denominator of curenncy that is available.")
        print("help displays help menu with these commands")
        print("exit	exit the vending machine")
    elif userInput == "balance":
        print("${:,.2f}". format(balance/100))

    elif userInput == "history":
        for i in range(len(hist)):
            print(hist[i])
    elif userInput == "inventory":
        print("ID    QTY    Name ")
        i=0
        for product in inv:
            print (str(i)+"      "+str(product.qty)+"     "+product.name)
            i+=1
    elif inputs[0]== "add item":
        try:
            name=""
            count=0
            inputs.pop(0)
            for word in inputs:
                if word.isalpha():
                    name= name+word+" "
                    count+=1
            for i in range(0,count):
                inputs.pop(0)
            if count>=2:
                name=name.strip()
            qty=int(inputs[0])
            inputs.pop(0)
            price=float(inputs[0])
            inputs.pop(0)
            if len(inv)!=0:
                for prod in inv:
                    if prod.name==name:
                        prod.qty+=qty
                    else:
                        inv.append(Products(name,qty,price))  
                        break
            else:
                inv.append(Products(name,qty,price))
        except :
            print("Unexpected input format")
    elif inputs[0]== "buy item":
        name=""
        count=0
        try:
            inputs.pop(0)
            for word in inputs:
                if word.isalpha():
                    name= name+word+" "
                    count+=1
            for i in range(0,count):
                inputs.pop(0)
            if count>=2:
                name=name.strip()
            dollars=int(inputs[0])
            inputs.pop(0)
            quarters=int(inputs[0])
            inputs.pop(0)
            dimes=int(inputs[0])
            inputs.pop(0)
            nickels=int(inputs[0])
            inputs.pop(0)
            pennies=int(inputs[0])
            totPay= float(dollars * 100 +quarters*25+dimes*10+nickels*5+pennies)
        
            for prod in inv:
                if prod.name==name:
                    totPrice=prod.price
                    totPrice=totPrice*100
                    if(totPay-totPrice<0):
                        print("error you do not have enough money")
            
                    else:
                        change=totPay-totPrice
                        if prod.qty==0:
                            print("Sorry the vending machine is out of"+prod.name)
                            break
                        balance+=totPrice
                        print("Congrats transaction complete")
                        if change>100:
                            print("Your change is "+"${:,.2f}". format(change))
                        elif change<100 and change>0:
                            print("Your change is "+"$0."+str(change))
                        else:
                            print("Your change is "+str(change))
                        prod.qty-=1

                    break
            
        except :
            print("Unexpected input format.")
    elif userInput=="exit":
        print("Okay Goodbye!")
        exit(0) 
    else:
        print("Unknown command, type help to see a list of commands")
             

    
    userInput=''
   
    
    
print ("all done")
#elif userInput.contains("buy item"):
#elif userInput is "exit":
    #exit(1)


    