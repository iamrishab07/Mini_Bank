import sys
from termcolor import colored
# functions
# Deposit Function
def deposit():
    outfile = open("statement.txt","a")
    total_amount = 0
    date = input(colored("Enter today's Date (DD/MM/YYYY): \n","green"))
    outfile.write("\n\nEntry Date : " + str(date) + "\n")

    while(1):
        amount = int(input("Enter amount : \n"))
        print "Enter details : \n"
        s = sys.stdin.readline()

        outfile.write("Deposit : " + str(amount) + " \nReason : " + s + "\n")
        total_amount += amount

        print colored("\n////////      Deposit Successful      ////////\n","green")
        
        print "\nDo you have other entries?\n\nEnter 1 for termination , any other key to continue\n\nEnter your choice : \n"
        st = int(input())
        if (st == 1 | st == 1):
            break
    
    outfile.close()
    outfile = open("balance.txt","r")
    sr = outfile.read()

    outfile.close()
    outfile = open("balance.txt","w")
    n = int(sr)
    n = n + total_amount
    outfile.write(str(n))
    print colored("\n\n////////      Thanks for using our services      ////////\n\n","green")
    outfile.close()



# Function for withdraw

def withdraw():
    outfile = open("statement.txt","a")
    total_amount = 0
    date = input(colored("Enter today's Date (DD/MM/YYYY): \n","green"))
    outfile.write("\n\nEntry Date : " + str(date) + "\n")

    while(1):
        amount = int(input("Enter amount : \n"))
        print "Enter details : \n"
        s = sys.stdin.readline()

        outfile.write("Withdraw : " + str(amount) + " \nReason : " + s + "\n")
        total_amount += amount
        print colored("\n////////      Withdraw Successful      ////////\n","green")
        print "\nDo you have other entries?\n\nEnter 1 for termination , any other key to continue\n\nEnter your choice : \n"
        st = int(input())
        if (st == 1 | st == 1):
            break
    
    outfile.close()
    outfile = open("balance.txt","r+")
    sr = outfile.read()

    outfile.close()
    
    outfile = open("balance.txt","w")
    n = int(sr)
    n = n - total_amount
    outfile.write(str(n))
    print colored("\n////////      Thanks for using our services      ////////\n","green")
    outfile.close()



# Function for Balance check

def balance():
    outfile = open("balance.txt","r")
    print "\nYour current balance is : " + outfile.read()
    #print colored("\nHello\n","red")
    print colored("\n////////      Thanks for using our services      ////////\n","green")
    outfile.close()



# Start of main code
while(1):
    option = int(input("\nWhat do you want to do sir?\n\nEnter 1 for Deposit\n\nEnter 2 for withdraw\n\nEnter 3 for Balance check\n\nEnter any other number for exit\n\nYour entry : \n"))
    #print option
    if option == 1:
        deposit()
    elif option == 2:
        withdraw()
    elif option == 3:
        balance()
    else:
        break

print colored("\n\n       Thanks for using. Visit Again       \n\n","yellow")
# End of main code
