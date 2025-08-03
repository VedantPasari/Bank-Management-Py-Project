#Features : Bank Account, Deposit Money, Withdraw Money, Details, Update Details and Delete Account
#We have to create a JSON file to save the datas of the users when we create it.
#then we have to create dummy data file of JSON file to access through this file itself.  
#Changes will be done in Dummy file which exists in main file itself. 
import json
import random
import string
from pathlib import Path


class Bank:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print(f"No such file exists.")
    except Exception as err:
        print(f"An exception occured as {err}")

                                                                                                                                                                                                                                                  
    @staticmethod
    def __update():
        with open(Bank.database,'w') as fs:
            fs.write(json.dumps(Bank.data))

    
    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters,k=3)
        num = random.choices(string.digits,k=3)
        spchar = random.choices("!@#$%^&*",k=1)
        id = alpha + num + spchar
        random.shuffle(id) #it is in the form of list
        return "".join(id)  #list to string



    def createaccount(self):   
        info = {
            "name" : input("Tell your Name:-"),
            "Age" : int(input("Tell your Age:-")),
            "email": input("Tell your email:-"),
            "pin": int(input("Tell your Pin:-")),
            "AccountNo." : Bank.__accountgenerate(),   #account no. should be system generated
            "Balance": 0
        }
        if info['Age'] < 18 or len(str(info["pin"])) != 4:
            print("Sorry you cannot create your account.")
        else:
            print("Account has been created successfully.")
            for i  in info :
                print(f"{i} : {info[i]}")
            print("Please note down your account number.")


            Bank.data.append(info)  #appending all the info in the dummy file i.e. data file so list ke andar dictionary append ho jayegii

            Bank.__update()


    
    def depositmoney(self):
        accnumber = input("Please tell your account no.:- ")
        pin = int(input("Please tell your pin as well:- "))

        #Extracting the data
        userdata = [i for i in Bank.data if i['AccountNo.']==accnumber and i['pin']==pin]   #this will be dictionary inside a list
         
        if userdata == False:  #if empty tuple,list,dictionary,string then result is false
            print("Sorry No data found") 
        else:
            amount = int(input("How much you want to deposit :- "))
            if amount>10000 or amount<0:
                print("The amount is too much to deposit.You can deposit below 10K and above 0")
            else:
                userdata[0]['Balance'] += amount  #this will update the dummy data Bank.data also using deepcopy method
                Bank.__update()   #Now we have to update it in the Data.Json file 
                print("Amount deposited successfully!")



    def withdrawmoney(self):
        accnumber = input("Please tell your account no.:- ")
        pin = int(input("Please tell your pin as well:- "))

        userdata = [i for i in Bank.data if i['AccountNo.']==accnumber and i['pin']==pin]

        if userdata == False:
            print("Sorry No data found") 
        else:
            amount = int(input("How much you want to withdraw :- "))
            if amount > userdata[0]['Balance']:
                print("Sorry you don't have that much money.")
            else:
                userdata[0]['Balance'] -= amount  
                Bank.__update()
                print("Amount withdrawn successfully!")


    
    def showdetails(self):
        accnumber = input("Please tell your account no.:- ")
        pin = int(input("Please tell your pin as well:- "))

        userdata = [i for i in Bank.data if i['AccountNo.']==accnumber and i['pin']==pin]
        
        if userdata == False:
            print("Data not found.")
        else:
            print("\n\nYour information are :\n\n")
            for i in userdata[0]:
                print(f"{i} : {userdata[0][i]}")



    def updatedetails(self):
        accnumber = input("Please tell your account no.:- ")
        pin = int(input("Please tell your pin as well:- "))

        userdata = [i for i in Bank.data if i['AccountNo.']==accnumber and i['pin']==pin]

        if userdata == False:
            print("Data not found.")
        else:
            print("You cannot change the age , Account number and the balance.")
            print("Fill the details for the change or leave it empty for no change...")

            #We will make a new dummy file then save this info to the Bank.data dummy file.

            newdata = {
                "name" : input("Please tell new name or press enter to skip :- "),
                "email" : input("Please tell new email or press enter to skip :- "),
                "pin": input("Pease tell new Pin or press enter to skip :- ")  #Pin is an int value but enter will not work in int so taking it first as a string 
            }
            
            if newdata["name"] == "":
                newdata["name"] = userdata[0]['name']
            if newdata["email"] == "":
                newdata["email"] = userdata[0]['email']
            if newdata["pin"] == "":
                newdata["pin"] = userdata[0]['pin']
            
            newdata['Age'] = userdata[0]['Age']
            newdata['AccountNo.'] = userdata[0]['AccountNo.']
            newdata['Balance'] = userdata[0]['Balance']

            if type(newdata['pin']) == str:
                newdata['pin'] = int(newdata['pin'])

            for i in newdata:
                if newdata[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = newdata[i]

            Bank.__update()
            print("Details updated successfully.")



    def deleteaccount(self):
        accnumber = input("Please tell your account no.:- ")
        pin = int(input("Please tell your pin as well:- "))

        userdata = [i for i in Bank.data if i['AccountNo.']==accnumber and i['pin']==pin]

        if userdata == False:
            print("Sorry no such data exists.")
        else:
            check = input("Press y if you actually want to delete the account or press n :- ")
            if check == 'n' or check == 'N':
                print("Bypassed")
            else:
                index = Bank.data.index(userdata[0])  #finds index of the userdata.data dictionary in the Bank.data
                Bank.data.pop(index) #deleted from dummy data file 
                print("Account deleted successfully")
                Bank.__update()





user = Bank()  #user is the object we have created 

print("Press 1 for creating an account")
print("Press 2 to deposit money in the bank")
print("Press 3 for withdrawing the money")
print("Press 4 for Details")
print("Press 5 for updating the details")
print("Press 6 for deleting your account")

check = int(input("Tell your Response : "))

if check == 1:
    user.createaccount()

if check == 2:
    user.depositmoney()

if check == 3:
    user.withdrawmoney()

if check == 4:
    user.showdetails()

if check == 5:
    user.updatedetails()

if check == 6:
    user.deleteaccount()