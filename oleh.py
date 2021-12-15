"""my lab"""
# def dict_add(dict, date, prior, action):
def dict_add(dict1, tuple1):
    """
    add a new action to the dict
    >>> print(dict_add({"12.03.2022": ["matan"], "11.03.2022":\
 ["matan"]}, ("12.03.2022", '2', "litak")))
    {'12.03.2022': ['matan', 'litak'], '11.03.2022': ['matan']}
    """
    date = tuple1[0]
    prior = int(tuple1[1])
    action = tuple1[2]
    if date in dict1.keys():
        value = dict1[date]
        new_action = [action]
        value = value[0:prior - 1] + new_action + value[prior - 1:]
        dict1[date] = value
    else:
        dict1[date] = (action)
    return dict1

# print(dict_add({"12.03.2022": ["matan"], "11.03.2022": ["matan"]} , ("12.03.2022", '2', "litak")))

# if __name__ == "__main__":
#     import doctest
#     print(doctest.testmod())
