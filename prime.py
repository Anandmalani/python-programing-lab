x= int(input("enter the number"))
if x<0:
  print("enter the positive no.")
elif x==1:
  print("neither prime nor composite")
else:
  c=0
  for i in range(1,x):
    if x%i==0:
      c=c+1
    else:
      c=c
  if c>1:
    print("composite no")
  else:
    print("prime no") 

