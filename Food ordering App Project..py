#!/usr/bin/env python
# coding: utf-8

# In[16]:


#importing json:
import json
import re

#Creating the Restaurant class:
class Restaurant:
    def __init__(self):
        self.foods={}
        self.food_id=len(self.foods)
        
        
#Admin functionalities:

    def food_items(self):
        self.name=input("Enter the food name :")
        self.quantity=int(input("Enter the food Quantity :"))
        self.price=int(input("Enter the food price :Rs"))
        self.discount=int(input("Enter the food discount :INR"))
        self.stock=int(input("Enter the food stock :pieces"))
        self.item={"Name":self.name,"Quantity":self.quantity,"Price":self.price,"Discount":self.discount,"Stock":self.stock}
        self.food_id=len(self.foods)+1
        self.foods[self.food_id]=self.item
        print(" ")
        print("Food items Added Successfully  :")
        print(self.foods)
        print(" ")
    
#Creating the json file to store the data of foods_item:
        with open("Food_items.json","w") as f:
            json.dump(self.foods,f)
        
        
#Creating the functionality for the Remove a food items from the menu using FoodID:       
    def remove_food_items(self):
        del self.foods[int(input("Enter the food_id which you want to the Remove :"))]
        print(" ")
        print("Remaining food items are",self.foods)
        print(" ")
        
        
       #Creating the json file to store the data of foods_item: 
        with open("Food_items.json","w") as f:
            json.dump(self.foods,f)
        
        
        
#Creating the functionality for the Edit food items usning the FoodID:def Edit_food_items(self):        
    def Edit_food_items(self):
        f_id=int(input("Enter the food_id which you want to the update :"))
        print(" ")
        for i in self.foods[f_id]:
            self.foods[f_id][i]=input(f"Enter the {i} that you want to update :")
        print(" ")
        print("Updated food items : ")
        print(self.foods)
        
      #Creating the json file to store the data of foods_item:  
        with open("Food_items.json","w") as f:
            json.dump(self.foods,f)
            
#Creating the functionality for the View the list of all food items:
    def view_food_items(self):
        print(" ")
        print("list of all food items : ")
        for i in self.foods:
            print(" ")
            print("food_id : ",i)
            for j in self.foods[i]:
                print(j,":",self.foods[i][j])
                
                
                

## USER  functionality:               
                
#Create the class of user name:
class user:
    def __init__(self):
        self.details={}
        self.food_id=len(self.details)
        self.order=[]
        
    
    
    #Create the function of register name to performe all functionality of user:
    def register(self):
        
        #Take input as Full Name from  User :
        print("Please register yourself  :")
        self.name=input("Enter the Full Name :")
        matcher = re.finditer("\s",self.name)
        
        #Take input as Phone Number from user :
        self.phone_number=input("Enter the Phone Number :")
        m = re.fullmatch("[6-9][0-9]{9}",self.phone_number)
        if m!=None:
            pass
        else:
            print("Please enter Valid Phone Number !")
        
           
        #Take input as Email from user :
        self.Email=input("Enter your Email :")
        email = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
        if re.search(email,self.Email):
             pass
        
        else:
            print("Please write valid Email !")
                
                
        #Take input as Address from user:
        self.address=input("Enter the Address :")
        matcher = re.finditer("\s",self.address)
        matcher = re.finditer("[0-9]",self.address)
        
        
        #Take input as Password from user:
        self.password=input("Enter the Password:")
        n = self.password
        if len(n)>=6:
             pass
        
        else:
            print("Please Enter Valid Password ")
        matcher = re.finditer("@",self.password)
        matcher = re.finditer("[0-9]",self.password)
        
            
            
        #Print all information of user:
        self.information={"Full Name":self.name,"Phone Number":self.phone_number,"Email":self.Email,"Password":self.password,"Address":self.address}
        self.food_id=len(self.details)+1
        self.details[self.food_id]=self.information
        print(" ")
        print(self.details)
        print("Register Successfully :")
        
        #Creating the json file to store the data of user:    
        with open("register.json","w") as f:
            json.dump(self.details,f)
        print(" ")
        
            
   #Create longin functions for longin user: 
    def longin(self):
        print("Longin yourself :")
        
        while True:
            #Take input as Email from user :
            self.user_name=input("Enter the Email :")
            matcher = re.finditer("@",self.user_name)
            matcher = re.finditer("[0-9]",self.user_name)
        
            #Take input as Password from user:
            self.password1=input("Enter the Password:")
            matcher = re.finditer("@",self.password1)
            matcher = re.finditer("[0-9]",self.password1)
        
            #Check the condition for Email and password enter by user are correct or not:
            if self.user_name==self.Email and self.password1==self.password:
                print("Login Successfully ")
                print("1.Place New Order \n 2.Order History \n 3.Update Profile \n 4.Exit :")
                ch=input("Enter your choice :")
                if (ch=='1'):
                    y.Place_New_order()
                elif (ch=='2'):
                    y.Order_History()
                elif (ch=='3'):
                    y.Update_Profile()
                elif (ch=='4'):
                    break
                else:
                    print("Please Enter Valid Detail")
                
            else:
                print("Please Enter valid Information :")
                

    #Creating A Function for Place a New Order:        
    def Place_New_order(self):
        self.order=[]
        while True:
            x= "1.Tandoori Chicken (4 pieces) [INR 240]"
            y= "2.Vegan Burger (1 Piece) [INR 320]"
            z= "3.Truffle Cake (500gm) [INR 900]"
            print(x)  
            print(y)
            print(z)
            print("5 .Exit")
            user1 = int(input("Enter your Choice:"))
            print(" ")
            if user1 == 1:
                x1=x.split()
                self.order.append(x1)
                print(self.order)
                print("Order Placed !")
                print(" ")
                print("4. Place More Order")
                print("5 .Exit")
                a = int(input(" "))
                if a==4:
                    pass
                if a == 1:
                    x1=x.split()
                    self.order.append(x1)
                    print(self.order)
                    print("Order Placed !")
                    print(" ")
                if a == 2:
                    x2=y.split()
                    self.order.append(x2)
                    print(self.order)
                    print("Order Placed")
                    print(" ")
                if a == 3:
                    x3=z.split()
                    self.order.append(x3)
                    print(self.order)
                    print("Order Placed")
                    print(" ")
                if a ==5:
                    break
            
            elif user1 == 2:
                y1=y.split()
                self.order.append(y1)
                print(self.order)
                print("Order Placed")
                print(" ")
                print("4. Place More Order")
                print("5 .Exit")
                a = int(input(" "))
                if a==4:
                    pass
                if a == 1:
                    y1=x.split()
                    self.order.append(y1)
                    print(self.order)
                    print("Order Placed !")
                    print(" ")
                if a == 2:
                    y1=y.split()
                    self.order.append(y1)
                    print(self.order)
                    print("Order Placed")
                    print(" ")
                if a == 3:
                    y1=z.split()
                    self.order.append(y1)
                    print(self.order)
                    print("Order Placed")
                    print(" ")
                if a ==5:
                    break
                
            elif user1 == 3:
                z1=z.split()
                self.order.append(z1)
                print(self.order)
                print("Order Placed")
                print(" ")
                print("4. Place More Order")
                print("5 .Exit")
                a = int(input(" "))
                if a==4:
                    pass
                if a == 1:
                    z1=x.split()
                    self.order.append(z1)
                    print(self.order)
                    print("Order Placed !")
                    print(" ")
                if a == 2:
                    z1=y.split()
                    self.order.append(z1)
                    print(self.order)
                    print("Order Placed")
                    print(" ")
                if a == 3:
                    y1=z.split()
                    self.order.append(y1)
                    print(self.order)
                    print("Order Placed")
                    print(" ")
                if a ==5:
                    break
        
            elif user1 ==5:
                break
            else:
                print("Sorry! Please Choose Right Choice.")
            
        #Creating the json file to store the data of user:    
        with open("Place_New_order.json","w") as f:
            json.dump(self.details,f)
        print(" ")
        
    #Creating A Fuction to see the Order History:   
    def Order_History(self):
        print("Your Order History  :")
        print(" ")
        for i in self.order:
            print(i)
         
        
        
    #Creating A Function to see the Profile Update:    
    def Update_Profile(self):
        Personal_id=int(input("Enter the id which you want to the update :"))
        print(" ")
        for i in self.details[Personal_id]:
            self.details[Personal_id][i]=input(f"Enter the {i} that you want to update :")
        print(" ")
        print("Your Profile Updated Successfully : ")
        print(self.details)
        with open("register.json","w") as f:
            json.dump(self.details,f)
        print(" ")
        
        
        
## Main
x=Restaurant()
y=user()
while True:
    print("Welcome To My Restaurant!")
    print(" ")
    print("1.Admin \n 2.User \n 3.Exit")
    a1=int(input("Enter Your Choice :"))
    if a1==1:
        print("\n*****Admin Service Chart****") 
        print("1.Add New Food Item \n 2.Edit Food Item \n 3.Delete Food Item \n 4.View Food Item ")
        a2=int(input())
        if a2==1:
            x.food_items()
        elif a2==2:
            x.Edit_food_items()
        elif a2==3:
            x.remove_food_items()
        elif a2==4:
            x.view_food_items()
        else:
            print("Sorry! Enter Valid Choice")

    elif a1==2:
        print("\n****Customer service chart***")
        print("1.User Registration \n 2.User Login with menu List \n 3.Place Order \n 4.Order History \n 5.Update Profile ")
        a3=int(input())
        if a3==1:
            y.register()
        elif a3==2:
            y.longin()
        elif a3==3:
            y.Place_New_order()
        elif a3==4:
            y.Order_History()
        elif a3==5:
            y.Update_Profile()
        else:
            print("Sorry! Enter Valid Choice ")
        
    else:
        print("Thanks To Visit In Our Restaurant!!!!")
        break


# In[ ]:




