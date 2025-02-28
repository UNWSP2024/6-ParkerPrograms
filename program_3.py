# Nathan Parker
# 2/28/25
# Program #3: Tax Rate

#define the state and county sales tax rates
state_sales_tax_rate = 0.05
county_sales_tax_rate = 0.025

#get the total monthly sales from the user
total_monthly_sales = float(input('Enter the total sale for the month: '))

#define a function that calculates the county sales tax
def county_sales_tax(rate):
    return rate * total_monthly_sales

#define a function that calculates the state sales tax
def state_sales_tax(rate):
    return rate * total_monthly_sales

#define a function that can add the county and state sales tax
def total_sales_tax(tax_1,tax_2):
    return tax_1 + tax_2

#call the county sales tax function to calculate the county sales tax
county_sales_tax = county_sales_tax(county_sales_tax_rate)

#call the state sales tax function to calculate the state sales tax
state_sales_tax = state_sales_tax(state_sales_tax_rate)

#call the total sales tax function to calculate the total sales tax
total_sales_tax = total_sales_tax(county_sales_tax,state_sales_tax)

#display the county, state, and total sales tax
print(f'''County sales tax: ${county_sales_tax:,.2f}
State sales tax: ${state_sales_tax:,.2f}
Total sales tax: ${total_sales_tax:,.2f}''')

