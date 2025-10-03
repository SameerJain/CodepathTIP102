"""
U-get the sum of all ticket sales (dict values)
P- iterate thru the dictionary, add up every value to a variable, return it 
I- 
"""


def total_sales(ticket_sales):
    sum_val = 0

    for value in ticket_sales.values():
        sum_val += value
    return sum_val

ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

print(total_sales(ticket_sales))