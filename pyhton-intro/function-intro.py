
# function define
'''
structure to define function 
def fucntion name(arguments1, argument2...):
    implementation 
    retun 
'''

# define a function which take 2 no's and return addition of those

def addition(arg1, arg2):
    return arg1+arg2

# call a funtion by creating the obj
obj = addition(4,7)
print("returened value from funtion is : ",obj)

'''
call a function from anopther function 
'''
'''
 eg: market function take item as input from another function and give the price of the item

'''
print("*"*30)
def market(item):
    items_dict = {"rice":67,"dal":78}

    if item in items_dict.keys():
        return items_dict[item]
    else:
        return 'no item found in market'

def getvlaue_from_market():
    obj = market('rice')
    print("returned value from market function: ",obj)


obj = getvlaue_from_market()
