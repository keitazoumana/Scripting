def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def get_series_of_numbers():
    number_values = input("How large will the list be:  ")

    if(not(is_number(number_values))):
        print("Please enter valid values.")
        exit()

    else:
        counter = 1
        final_list = []

        while(counter < int(number_values) +1 ):
            value = input("Enter number {} of {}: ".format(counter, number_values))
            if(not(is_number)):
                print("Please enter valid values.")
                exit()
            final_list.append(int(value))
            counter = counter + 1

        print("Lowest Number: {:.1f}".format(min(final_list)))
        print("Highest Number: {:.1f}".format(max(final_list)))
        print("Sum: {:.1f}".format(sum(final_list)))
        print("Average: {:.1f}".format(sum(final_list)/len(final_list)))
        
if __name__ == "__main__":
    get_series_of_numbers()