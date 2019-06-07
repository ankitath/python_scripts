hrs = input("hours")
h = float(hrs)
rph = input("rate per hours")
r = float(rph)
def computepay(h,r):
    if(h <= 40):
        gross_pay = h*r
    elif(h>40):
        hrs1 = h-40
        gross_pay1 = 40*r
        gross_pay2=(hrs1+hrs1*0.5)*r
        gross_pay = gross_pay1+gross_pay2
        return gross_pay
p = computepay(h,r)
print("Pay",p)
