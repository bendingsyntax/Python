#Daniel De Jesus
#09/28/17

#Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and
#create a function called computepay which takes two parameters (hours and rate).
#Enter Hours: 45
#Enter Rate: 10
#Pay: 475.0

def computepay(h,r):
    if h > 40:
        overtime = h - 40
        regpay = 40 * r
        overpay = (r * 1.5) * overtime
        totalpay = (overpay + regpay)
        return (round(totalpay,2))
    else:
        regpay = h * r
        return round(regpay,2)

hrs = float(input("Enter Hours:"))
rate = float(input("Enter rate:"))

p = computepay(hrs,rate)
print(p)
