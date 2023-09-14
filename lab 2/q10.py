x=int(input("enter seconds "))
if x>1 and x<86400:
     hour=x//3600
     r1=(x*24)%86400     #UNITARY METHOD, 86400 SEC=24 HRS SO  1 SEC =(1*24)/864000  
     minute=r1//(24*60)
     seconds=x%60
     print(hour,"hours" ,minute,"minutes" ,seconds,"seconds")
else:
    print("ENTER SECONDS BETWEEN 1 TO 86400")
