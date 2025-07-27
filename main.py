
import json
import random
import string
from pathlib import Path


class Bank:
    database='data.json'
    data=[]
    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())

        else:
            print("NO Such file exists ")
    except Exception as err:
        print(f"an exception occured as {err}")


    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountgenerate(cls):
        alpha=random.choices(string.ascii_letters,k=3)
        nums=random.choices(string.digits,k=3)
        spchar=random.choices("!@#$%^&*",k=1)
        id=alpha+nums+spchar
        random.shuffle(id)
        return "".join(id)



    def createaccount(self):
        info={
            "name":input("Tell me ypur name ="),
            "age":int(input("Tell me your Age =")),
            "email":input("Tell me ypur email ID ="),
            "pin":int(input("Tell me your pin=")),
            "account number":Bank.__accountgenerate(),
            "balance":0

        }
        if info['age']<18 or len(str(info['pin'])) != 4:           
            print("Sorry you are eligible to create an account")
        else:
            print("Ypur account has been created successfully")
            for i in info:
                print(f"{i}:{info[i]}")
            print("Please note down your account number")

            Bank.data.append(info)

            Bank.__update()

    def depositmoney(self):
        accountnumber=input("please tell your acoount number: ")
        pin=int(input("please tell your pin aswell:"))
        userdata=[i for i in Bank.data if i['account number']==accountnumber and i['pin']==pin]

        if userdata==False:
            print("NO data found ")
        else:
            amount=int(input("how much amount you want to deposit"))
            if amount>10000 or amount<0:
                print("sorry the amount you are trying to deposit should be below 10000 and above 0.")
            else:
                userdata[0]['balance']+=amount
                Bank.__update()
                print("your amount deposited successfully.")

    def withdrawmoney(self):
        accountnumber=input("please tell your acoount number: ")
        pin=int(input("please tell your pin aswell:"))
        userdata=[i for i in Bank.data if i['account number']==accountnumber and i['pin']==pin]

        if userdata==False:
            print("NO data found ")
        else:
            amount=int(input("how much amount you want to withdraw"))
            if userdata[0]['balance']<amount:
                print("sorry you don't have that much money.")

            
            else:
                userdata[0]['balance']-=amount
                Bank.__update()
                print("your amount withdrew  successfully.")

    def showdetails(self):
        accountnumber=input("please tell your acoount number: ")
        pin=int(input("please tell your pin aswell:"))
        
        userdata=[i for i in Bank.data if i['account number']==accountnumber and i['pin']==pin]
        print("your information are \n")
        for i in userdata[0]:
            print(f"{i}:{userdata[0][i]}")

    def updatedetails(self):
        accountnumber=input("please tell your acoount number: ")
        pin=int(input("please tell your pin aswell:"))
        userdata=[i for i in Bank.data if i['account number']==accountnumber and i['pin']==pin]
        
        if userdata==False:
            print("There no such user found.")
        else:
            print("you can't change your age, account number, balance.")

            print("Fill the details for change or leave it empty if no changes.")

            newdata={
                "name":input("please enter your new name or press enter to skip:="),
                "email":input("Please enter your new email or press enter to skip:="),
                "pin":input("Please enter your new pin or press enter to skip:=")                
            }
            if newdata["name"]=="":
                newdata["name"]=userdata[0]['name']
            
            if newdata["email"]=="":
                newdata["email"]=userdata[0]['email']

            if newdata["pin"]=="":
                newdata["pin"]=userdata[0]['pin']

            newdata['age']=userdata[0]['age']
            newdata['account number']=userdata[0]['account number']
            newdata['balance']=userdata[0]['balance']

            if type(newdata['pin'])==str:
                newdata['pin']=int(newdata['pin'])

            for  i in newdata:
                  if newdata[i]==userdata[0][i]:
                      continue
                  else:
                      userdata[0][i]=newdata[i]

            Bank.__update()
            print("Your Bank details has been updated successfully:")

    def delete(self):
        accountnumber=input("please tell your acoount number: ")
        pin=int(input("please tell your pin aswell:"))
        userdata=[i for i in Bank.data if i['account number']==accountnumber and i['pin']==pin]

        if userdata==False:
            print("sorry no such data found.")
        else:
            Check=input("press 'y' if you want to to delete the file or else press 'n' .")
            if Check=='n' or Check=='N':
                print("bypassed")
            else:
                index=Bank.data.index(userdata[0])
                Bank.dat.pop(index)
                print("Account deleted succussfully.")
            



user=Bank()

print("press 1 for creating an account")
print("press 2 for Depositing the money in the bank")
print("press 3 for withdrawing the money")
print("press 4 for details")
print("press 5 for updating the details")
print("press 6 for deleting your account")

Check=int(input("Enter your response:"))

if Check==1:
    user.createaccount()

if Check==2:
    user.depositmoney()

if Check==3:
    user.withdrawmoney()

if Check==4:
    user.showdetails()

if Check==5:
    user.updatedetails()

if Check==6:
    user.delete()

