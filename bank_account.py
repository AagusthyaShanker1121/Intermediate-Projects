
# bank_account_holders = {}

import random


class BankAccount() :

    #For any new bank account , Register User_name , and amount. Default Name = NULL and amount = 10000 
    def __init__(self , name = 'NULL' , balance = 0 ) :
        self.name = name 
        if balance.isnumeric() != True :
            balance = 0
        self.balance = balance
        self.age = 18
        self.address = ''
        self.phone_number = ''
        self.pin = random.randint(1000 , 9999) # random 4-digit pin assigned to each new account holder
        self.account_number = random.randint(1000000000 , 10000000000)
        print("Bank account created successfully ! ")
        print("Your Account number :\t" , self.account_number , '\n' ) 


    def modify_name(self) :
        new_name = input("Enter your new name :\t")
        self.name = new_name
        print("Name modified successfully ! ")
    
    def modify_address(self) :
        new_address = input("Enter your modified address :\t")
        self.address = new_address
        print("Address modified successfully ! ")
    
    def modify_age(self) :
        new_age = input("Enter your new age :\t")
        self.age = new_age 
        print("Age modified successfully ! ")
    
    def modify_phone_number(self) :
        new_phone_number = input("Enter your new phone Number :\t") 
        self.phone_number = new_phone_number
        print("Phone number modified successfully ! ")

    def modify_pin(self) :
        new_pin = int(input("Enter your desired pin"))
        self.pin = new_pin
        print("Your pin is resetted successfully !")


    def modify_details(self) :
        print("Some user guidelines ....\n")
        print("Type name/addres/age/phone number/pin to modify any of the details\n")
        print("Type no/nothing/no modification/quit/quit() to quit the modification process\n")
        while(True) :
            what_modification = input("Enter what do you want to modify :\t") 

            if what_modification.lower() == 'name' :
                BankAccount.modify_name(self)
            elif what_modification.lower() == 'address' :
                BankAccount.modify_address(self)
            elif what_modification.lower() == 'age' :
                BankAccount.modify_age(self)
            elif what_modification.lower() == 'phone number' :
                BankAccount.modify_phone_number(self)
            elif what_modification.lower() == 'pin' :
                BankAccount.modify_pin(self)
            elif what_modification.lower() in ['no' , 'nothing' , 'no modification' , 'quit' , 'quit()' ]:
                break
            else :
                print("Enter correct data (name/phone number/address/age/pin) to proceed further ! ")
                # print("Enter correct data (name/phone number/address/age) to proceed further ! ")
                continue

    def amount_deposit(self) :
        deposit_amount = float(input("How much you want to deposit into your account :\t"))
        self.balance += deposit_amount
        print("Amount deposited successfully ! ") 
    
    def withdraw_amount(self) :
        withdrawal = int(input("Enter amount to be withdrawn :\t")) 

        if withdrawal > self.balance :
            print("Error ! Withdrawal amount should be within your balance ")
            quit()
        else :
            self.balance -= withdrawal
            print("Rs {} withdrawn successfully !".format(withdrawal))
        
    def show_details(self) :
        print("Account holders Details are as follows :\n")
        print("Name :\t" , self.name) 
        print("Age :\t" , self.age)
        print("Address :\t" , self.address)
        print("Account Number :\t" , self.account_number)
        print("Phone Number :\t" , self.phone_number)
        print("Current Balance :\t" , self.balance)

    def show_balance(self) :
        print("Your current balance :\t" , self.balance) 


# count_creations = 0 
# while True :
#     user_input = input("Do you wish create a new bank account ? Type \"y\" for yes and \"n\" for no\n")
#     if user_input.lower() == 'n' :
#         break

#     elif user_input.lower() == 'y' :
#         # ask about name and balance to be initialized 
#         user_name = input("Enter new account holder's name :\t")
#         user_balance = input("Enter initialial balance :\t")
#         count_creations += 1
#         # instantiating a new bank account 
#         user_account = BankAccount(user_name , user_balance)
#         # storing data 
#         bank_account_holders[user_account.pin] = user_account

#     else :
#         continue 



# print("\n\n{} account(s) created successfully !.".format(count_creations))

# for key in bank_account_holders.keys() :
#     print(key , bank_account_holders[key].name)
