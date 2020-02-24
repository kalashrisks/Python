# Write a program input customer name and slab type(i/c/r)
# Calculate units consumed
# Conditions :
    # if slab type is industry then unit rate is 5.25/-
    # if slab type is commercial then unit rate is 4.00/-
    # if slab type is residencial then unit rate is 3.08/-
    # calculate total bill

units = int(input("PLease eneter number of units consumed: "))

if units < 50:
    amount = units * 2.60
    surcharge = 25
elif (units <= 100):
    amount = 130 + ((units - 50) * 3.25)
    surcharge = 35
elif (units <= 200):
    amount = 130 + 162.50 + ((units - 100) * 5.26)
    surcharge = 45
else:
    amount = 130 + 162.50 + 526 + ((units - 200) * 8.45)

total = amount + surcharge
print("\nElectricity Bill = %.2f" %total)
# %.2f is replaced by second value

################################################################
#
units = int(input("Please enter the number of units consumed in a month"))
if(units <= 100):
    payAmount = units*1.5
    fixedcharge = 25.00
elif (units <= 200):
    payAmount = (100 * 1.5) + (units - 100) * 2.5
    fixedcharge = 50.00
elif (units <= 300):
    payAmount = (100 * 1.5) + (200 - 100) * 2.5 + (units - 200) * 4
    fixedcharge = 75.00
elif (units <= 350):
    payAmount = (100 * 1.5) + (200 - 100) * 2.5 + (300 - 200) * 4 + (units - 300) * 5
    fixedcharge = 100.00
else:
    payAmount = 0
    fixedcharge = 1500.00

Total = payAmount + fixedcharge
print("\nElectricity bill = %.2f"%Total)

###########################################################


