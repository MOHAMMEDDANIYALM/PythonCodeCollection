class BankAccount:
 def __init__(self , account_holder , balance = 0):
    self.account_holder = account_holder
    self.balance = balance
 def deposit(self , amount):
     if amount > 0 :
      self.balance += amount
      print (f"Deposited{amount}") 
     else : 
       print ("Deposit amount must be positive.")

 def withdraw(self , amount):
     if self.balance >= amount:
      self.balance -= amount
      print (f"Whithrawal{amount}")
     else :
      print ("insuffisiant funds ")
 def check_balance(self):
    print (f"Balance:{self.balance}")

acc1 =BankAccount("DANIYAL",500)
acc1.deposit(200)
acc1.withdraw(100)
acc1.check_balance()
