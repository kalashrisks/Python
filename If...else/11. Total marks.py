"""
Write a program input Total Marks.
if tm>360 then print "First Class"
if tm>==300 and tm<360 then print "Second class"
if tm<300 then print "third class"
"""

tm = int(input("Enter Total Marks: "))
if tm > 360:
    print("First Class")
elif tm >= 300 and tm <= 360:
    print("Second Class")
elif tm < 300 and tm >=0:
    print("Third Class")
else:
    print("Invalid Class")
