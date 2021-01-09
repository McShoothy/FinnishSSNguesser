list = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F","H","J","K","l","M","N","P","R","S","T","U","V","W","X","Y"]
bday = input("birthday (DD/MM/YY):")
gender = raw_input("gender (M/F): ")
ccs = raw_input("last charecter of your SSN:")
CS = list.index(ccs)
print("Possible SSNs:")

for i in range(0,100):
      if (i+bday*1000)%31 == (CS) and gender == ("M") and i%2 == (1):
        print bday,"A",i, ccs
      elif (i+bday*1000)%31 == (CS) and gender == ("F") and i%2 == (0):
        print bday,"A",i,ccs


#for i in range(0,1000):
 #   for j in range(0,32):
  #      if (i+bday*1000)%31 == list[j] and gender == ("M") and i%2 ==(1):
   #     elif (i+bday*1000)%31 == list[j] and gender == ("F") and i%2 ==(0):
     #       print bday, "A", i, list[j]

