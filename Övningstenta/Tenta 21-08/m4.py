"""
Solutions to exam tasks for module M4
Name:
Code:
"""



# A9
def get_balance(index):
    """This method opens customers.json and returns the field
    'balance' for the person with the given index.
    Leave this method as is.
    Note that '$' and ',' are removed from 'balance' in the jason file"""
    import json
    with open('customers.json') as f:
        data = json.load(f)
        return float(data[index]['balance'].replace('$', '').replace(',', ''))


def get_total_balance():
    """Method that runs get_balance in parallel for each index 0-111.
    The method should return the sum of all balances."""
    import multiprocessing as mp
    import concurrent.futures as future

    with future.ProcessPoolExecutor(
            mp_context=mp.get_context('fork')) as ex:
        index = range(112)
        results = ex.map(get_balance, index)

    total = sum(list(results))
    return total






# A10

def get_mean_balances():
    import json
    with open('customers.json') as f:
        data = json.load(f)
    print(data[0]['gender'])
    """Method that return the mean balance for male and female customes. Gender
    is set in the field 'gender' ('male' or 'female')"""
    male_data = []
    female_data = []

    for i in range(112):
        if data[i]['gender'] == 'male':
            male_data.append(lambda: get_balance(i))
        else:
            female_data.append(lambda: get_balance(i))

    # print(male_data)
    # avg_m = sum(male_data) / len(male_data)
   #  avg_f = sum(female_data) / len(female_data)

    #return (avg_m, avg_f)




    pass # remove and write your code here
    
# B4
def leapyears(years):
    """A method the returns the leap years of the years in the in argument years"""
    return [year for year in years if (year % 4 == 0 and not year % 100 == 0) or year % 400 == 0]


def main():
    print('Test of A9 ')
    print(get_total_balance())
    print('Test of A10 ')
    print(get_mean_balances())
    print('Test of B4 ')
    ly=leapyears(range(1900,2101))
    print(ly)
    if ly != None:
        print(len(ly))

    ly = leapyears(range(1599, 1650))
    print(ly)
    if ly != None:
        print(len(ly))

if __name__ == "__main__":
    main()
    print('Over and out')
