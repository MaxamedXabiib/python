first_number = float(input("enter your first numper: "))
operator = input("chose your operator:")
second_number = float(input("enter your second numper:"))
if operator == "+":
    print(first_number + second_number) 
elif operator == ("-"):
    print(first_number - second_number)
elif operator == ("*"):
    print(first_number * second_number)
elif operator == ("/"):
<<<<<<< HEAD
    print(first_number / second_number)
=======
    print(first_number / second_number)    
>>>>>>> ffeefd93c0d160f4ee3af88ead0d502289dd040f
else:
    print("invailed operator")   
