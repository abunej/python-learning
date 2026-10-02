hours=input("enter hours: ")
h=float(hours)
rate=input("enter rate: ")
r=float(rate)
if h<=40:
    pay=h*r
else:
    regular_pay=40*r
    overtime_hours=h-40
    overtime_pay=overtime_hours*(r*1.5)
    pay=regular_pay+overtime_pay
print(pay)