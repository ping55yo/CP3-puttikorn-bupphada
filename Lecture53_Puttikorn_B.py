price= int(input('ราคา= '))
def vat_7(price):
    Netprice = price+(price*7/100)
    return Netprice
print(vat_7(price))
