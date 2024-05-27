import datetime
def converter(amount, rate):
    return amount*rate

e = datetime.datetime.now()
print("Currency Converter")

curr1 = input("Enter the currency of 1st country: ")
curr2 = input("Enter the currency of 2nd country:")
a = int(input("Enter the amount: "))

india = ["INR", "inr", "rupees"]
eu = ["euros"]
uk = ["pounds", "Pounds"]
us = ["Dollars", "dollars","usd"]
canada = ["cad dollar", "cad"]
russia = ["ruble"]
china = ["yuan"]
japan = ["yen"]

inr = 0
pou = 0
usd = 0
cad = 0
euro = 0
ruble = 0
yuan = 0
yen = 0

# conversion rates
if curr1 in india:
    pou = 0.011  # for uk(pounds)
    usd = 0.012  # for America
    cad = 0.017  # for canada
    euro = 0.012  # europe
    ruble = 0.75  # for russia
    yuan = 0.088  # for china
    yen = 1.80  # for japan

elif curr1 in japan:
    inr = 0.56
    pou = 0.006
    usd = 0.0068
    cad = 0.0092
    euro = 0.0068
    ruble = 0.42
    yuan = 0.049

elif curr1 in china:
    inr = 11.41
    pou = 0.12
    usd = 0.14
    cad = 0.19
    euro = 0.14
    ruble = 8.63
    yen = 20.41

elif curr1 in russia:
    inr = 1.32
    pou = 0.014
    usd = 0.016
    cad = 0.022
    euro = 0.016
    yuan = 0.12
    yen = 2.36

elif curr1 in canada:
    inr = 60.81
    pou = 0.65
    usd = 0.74
    euro = 0.74
    ruble = 45.99
    yuan = 5.33
    yen = 108.75

elif curr1 in us:
    inr = 81.98
    pou = 0.88
    euro = 1
    cad = 1.35
    ruble = 62
    yuan = 7.18
    yen = 146.62

elif curr1 in uk:
    inr = 93.28
    usd = 1.14
    euro = 1.14
    cad = 1.53
    ruble = 70.54
    yuan = 8.17
    yen = 166.82

elif curr1 in eu:
    inr = 81.98
    pou = 0.88
    usd = 1
    cad = 1.35
    ruble = 62
    yuan = 7.18
    yen = 146.62

if curr2 in india:
    print(converter(a, inr))

elif curr2 in us:
    print(converter(a, usd))

elif curr2 in uk:
    print(converter(a, pou))

elif curr2 in canada:
    print(converter(a, cad))

elif curr2 in eu:
    print(converter(a, euro))

elif curr2 in russia:
    print(converter(a, ruble))

elif curr2 in china:
    print(converter(a, yuan))

elif curr2 in japan:
    print(converter(a, yen))

else:
    print("wrong input")

print (e.strftime("%Y-%m-%d %H:%M:%S"))


print (e.strftime("%a, %b %d, %Y"))
