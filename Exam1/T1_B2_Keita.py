def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def compute_earning():

    number_working_days = input("How many days will you work?  ")

    if(not(is_number(number_working_days)):
        print("Please enter valid values.")
        exit()

    else:
        print("Day\t\tEarnings")
        number_working_days = int(number_working_days)
        CURRENT_PENNY = 0.01 
        total_earnings = 0

        for day in range(1, number_working_days + 1):
    
            print("Day {}\t\t{:.2f}".format(day, CURRENT_PENNY))
            total_earnings = total_earnings + CURRENT_PENNY
            CURRENT_PENNY = CURRENT_PENNY * 2

        print("\nTotal Earnings:  {:.2f}".format(total_earnings))

if __name__ == "__main__":
    compute_earning()