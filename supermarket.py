from datetime import datetime
name=input("Enter your name:")

lists='''
Rice   Rs 20/kg
Sugar  Rs 30/kg
salt   Rs 20/kg
oil    Rs 80/liter
paneer  Rs 110/kg
Maggi  Rs 50/kg
Boost  Rs 90/each
Soap   Rs 30/each
colgate Rs 60/each  

'''
price=0
pricelist=[]
totalprice=0
FinalAmount=0
ilist=[]
qlist=[]
plist=[]

#rates for items
items={'rice' : 20,'sugar':30,'salt':20,'paneer':110,'maggi':50,'boost':90,'soap':30,'colgate':60}
option=int(input("for list of items press 1:"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press1 or 2 for exit:"))  
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items:").lower().strip()
        quantity=int(input("Enter quantity:"))
        if item in items.keys():
            price=quantity * (items[item])
            pricelist.append((item,quantity,items[item],price)) 
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry!.You Entered item is not available") 
    else:
        print("ypu entered wrong:")   
    inp=input("Can i bill the items yes or no:")
    if inp=='yes':
        pass
        if finalamount!=0:
            print(25*"=","Mamtha supermarket",25*"=")
            print(28*" ","Nalgonda")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("sno",8*" ",'items',8*" ",'quantity',3*" ",'price')
            for i in range(len(pricelist)):
                print(i,8*"" ,8*" ",ilist[i],3*" ",qlist[i],plist[i])
            print(75*"-")
            print(50*" ",'TotalAmount:','Rs',totalprice)
            print("gst amount",50*" ",'Rs',gst)
            print(75*"-")
            print(50*" ",'finalamount:','Rs',finalamount)
            print(75*" ")
            print(50*" ","Thanks for Visiting")
            print(75*"-")
            print("THANKYOU ! VISIT AGAIN 🙏")
  


