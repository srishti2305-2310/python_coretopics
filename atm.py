class ATM:
    def __init__(self,balance,pin):
         self.balance=balance
         self.pin=pin

    def check_balance(self):
            return self.balance
        
    def withdrawl_amount(self,amount):
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Withdrawal amount must be positive.")
            if amount > self.balance:
                raise ValueError("Insufficient funds.")
            self.balance -= amount
            print("Withdrawl ${amount:.2f}. New balance is ${self.balance:.2f}.")
        except ValueError as e:
            print(f"Error: {e}")

    def deposit(self, amount):
           self.balance += amount 
           return "deposite: {amount}.New balance: {self.balance}"
def main():
        try:
             balance=float(input("enter your balance:"))   
        except ValueError:
             print("this is float value means decimal value,please enter a number")
             return       
        y=ATM(balance,1234)
        while True:       
                print("welcome to atm machine")
                try:
                       pin=int(input("enter a pin:"))
                except ValueError:
                       print("inccorect pin please enter coreect pin")
                       continue      
                if pin != y.pin:
                            print("incoorect pin")
                            continue
        
                print("1-check amount")
                print("2-withdrawl")
                print("3-deposit")
                print("4-exit")
                try:
                      z=int(input("enter your choice:"))
                except ValueError:
                      print("invalid choice option please choose valid opption")
                      continue      
            
                if z==1:
                   print("your balance",y.check_balance())
                elif z==2:
                    amount=float(input("enter your amount:"))
                    print(y.withdrawl_amount(amount)) 
                elif z==3:
                    amount=int(input("enter your deposite balance:"))
                    print(y.deposit(amount))
                elif z==4:
                    print("thankyou")
                    break
                else:
                    print("invalid")
if __name__== "__main__":
     main()                
           

      