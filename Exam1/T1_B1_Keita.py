def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def compute_tax():

    amount_purchase = input("Enter the amount of the purchase:  ")

    if(not(is_number)):
        print("Please enter valid values.")
        exit()

    else:
        STATE_TAX = 0.05
        COUNTY_TAX = 0.025

        amount_purchase = float(amount_purchase)
        state_tax = amount_purchase * STATE_TAX
        county_tax = amount_purchase * COUNTY_TAX

        total_sale_tax = state_tax + county_tax 
        total_sale = total_sale_tax + amount_purchase 

        print("Purchase Amount: \t{:.2f}".format(amount_purchase))
        print("State Tax: \t{:.2f}".format(state_tax))
        print("County Tax: \t{:.2f}".format(county_tax))
        print("Total Tax: \t{:.2f}".format(total_sale_tax))
        print("Sale Total: \t{:.2f}".format(total_sale))

if __name__ == "__main__":
    compute_tax()