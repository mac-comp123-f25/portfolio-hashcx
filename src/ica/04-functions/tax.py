def add_tax(price, tax_rate):
    tax_amt = price * tax_rate
    return price + tax_amt


'''
Local Environment
   price  25.99
tax_rate    .0725
 tax_amt   1.8842749999999997
'''
print(add_tax(25.99, 0.0725))
