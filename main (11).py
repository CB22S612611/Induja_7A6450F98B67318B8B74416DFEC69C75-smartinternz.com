def recursion_fact(x):
  if x == 1:
    return 1
  else:
    return (x*recursion_fact(x-1))


number =int(input("enter a value:"))
if number >= 1:
  print("the factorial of", number, "is", recursion_fact(number))
