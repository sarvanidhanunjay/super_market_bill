#Date_time module
from datetime import datetime
#to enter name
name=input("enter your name:")
#specify groceries list.
list='''
Rice    -50/- per Kg
sugar   -40/- per Kg
salt    -25/- per Kg
oil     -120/- per Li
maggi   -5/- per unit
boost   -90/- per unit
shampoo -80/- per unit
'''
#declaration of variables
price=0
pricelist=[]
totalprice=0
finalamount=0
i_list=[]
q_list=[]
p_list=[]
gst=0

#rates for items
items={'rice':50,'sugar':40,'salt':25,
       'oil':120,'maggi':5,'boost':90,'shampoo':80}
#option to find details about list
option=int(input("for list of items press 1:"))
if option==1:
    print(list)
    for i in range(len(items)):
        inp1=int(input("if u want to buy press 1 or press 2 for exit:"))
        if inp1==2:
         break
        if inp1==1:
         item=input("enter your item you want:")
         quantity=int(input("enter your required quantity:"))
         if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,price))
            totalprice+=price
            i_list.append(item)
            q_list.append(quantity)
            p_list.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
    else:  
            print("your requested item is not available.") 
else:
 print("you entered wrong number")  
 
 
                      
inp=input("can i bill now:if yes press 1 else press 0:") 
if inp==1:  
   pass
if finalamount!=0: 
   print(32*"_","D.S. SUPER MARKET",32*"_")
   print(37*" ","KADIRI")
   print("NAME:",name,30*" ","DATE:",datetime.now())
   print(80*"_")
   print("Sno",8*" ","ITEMS",8*" ","QUANTITY",5*" ","PRICE")
   print(80*"_")
   for i in range(len(pricelist)):                 
         print(i,8*" ",i_list[i],15*" ",q_list[i],10*" ",p_list[i])

   print(80*"_")                   
   print(50*" ","TOTAL AMOUNT:","Rs.",totalprice)
   print(50*" ","gst amounnt:  ","Rs.",gst)
   print(80*"_")
   print(50*" ","FINAL AMOUNT:","Rs.",finalamount)
   print(80*"_")
   print(30*" ","THANK YOU * VIST AGAIN")
   print(80*"-")
 
   print(80*"*")
   print(80*"_")
 




'''print(i_list)
print(q_list)
print(p_list)                
print(pricelist)''' 
   

                     
        
           
