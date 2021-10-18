a = int(input("Enter the password"))
a = "4736"
c = 4
while a>=0:
       if (a == 4736):
                  print("your password is correct")
                  break
       else:
             c = c - 1
             print("your password is incorrect")
             print(f"{c} attempts left")
