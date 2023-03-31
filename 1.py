# range and for loop
m = range(4,24,2)
for i in m:
  print(i)

#while loop and break
i=1
while i<10:
    print(i)
    if i==5:
     break
    i+=1
    
#pass 
i=100
j=20
if i<j:
    pass
else:
    print("No")

#continue
i = 0
while i < 9:
  i += 1
  if i == 3:
    continue
  print(i)
