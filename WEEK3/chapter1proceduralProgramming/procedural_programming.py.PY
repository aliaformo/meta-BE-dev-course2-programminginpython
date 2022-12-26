# BILL_TOTAL FUNCTION

def bill_total(bill):
    total =0.00
    for k, v in bill.items():
        total += v
    return total

# calculate_tax function

def calculate_tax(percent, bill_total):
    return round((bill_total*percent)/100.0, 2)


food_bill = {
    'juice': 3.99,
    'bread': 4.55,
    'tea': 2.00,
    'salad': 1.25
}

food_total = bill_total(food_bill)
tax_total = calculate_tax(15, food_total)

print('Total', food_total)
print('Tax:', tax_total)

print('overall:', food_total + tax_total)