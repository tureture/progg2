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
    Note that '$' and ',' are removed from 'balance' in the json file"""
    import json
    with open('customers.json') as f:
        data = json.load(f)
        return float(data[index]['balance'].replace('$', '').replace(',', ''))

def get_total_balance():
    """Method that runs get_balance in parallel for each index 0-111.
    The method should return the sum of all balances."""
    # pass # remove and write your code here
    indexes=range(112)
    import concurrent.futures as future
    with future.ThreadPoolExecutor() as ex:
        balances = list(ex.map(get_balance, indexes))
    return sum(balances)

# A10
# the following is invented by the student
def get_gender(index):
    import json
    with open('customers.json') as f:
        data = json.load(f)
        if data[index]['gender'] == 'male':
            return 0
        else:
            return 1

def get_mean_balances():
    """Method that return the mean balance for male and female customes. Gender 
    is set in the field 'gender' ('male' or 'female')"""
    # pass # remove and write your code here
    balances=[0,0]
    n_male_female=[0,0]
    for index in range(112):
        gender=get_gender(index)
        balance=get_balance(index)
        if gender==0:
            balances[0]+=balance
            n_male_female[0]+=1
        else:
            balances[1]+=balance
            n_male_female[1]+=1
    return [balances[0]/n_male_female[0], balances[1]/n_male_female[1]]

# B4
def leapyears(years):
    """A method the returns the leap years of the years in the in argument years"""
    # pass # remove and write your code here
    return [y for y in years if (y%4 == 0 and y%100 != 0) or (y%400 == 0)]


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

if __name__ == "__main__":
    main()
    print('Over and out')
