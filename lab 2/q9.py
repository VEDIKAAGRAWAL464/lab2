p=float(input("imput principle amount "))
t=float(input("input time period for RD "))
r=7.1
SI=p*r*t/(100*12)
if t>6 and p>500:
    print(SI)
else:
    print("invalid input")