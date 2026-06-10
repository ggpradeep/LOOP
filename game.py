guess = int(input("Enter a number between 1 and 50"))
number = int(input("Enter a number"))
attempt = 0
attempt = attempt + 1
while attempt < 5:
 if guess != number:
  if  guess - 5 == number:
   print("Hot")
 elif guess - 10 == number:
   print("Warm")
 elif guess - 15 == number:
   print("Cold")
 elif guess - 15 == number:
   print("Ice cold")
 else:
   print("Correct")

   