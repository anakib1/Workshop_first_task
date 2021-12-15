
import os

# coding = utf-8
import datetime


def input_tasks():
    dct = {}
    print(""" Insert the due date of, your task, priority of task. Consider preserving this order(date, task, priotity
    Example: 2021-12-15 matan 1""")
    try:
        duedate, task, priority = input(">>> ").split()
    except Exception:
        if input(">>> ") == "вихід":
            quit()
        else:
            input_tasks()
    dct = csv_read("db.csv")
    csv_write("db.csv", dict_add(dct, (duedate, priority, task)))
    multi_input()


def multi_input():
    answer = input("Continue adding tasks? y/n")
    if answer == 'y':
        input_tasks()
    if answer == 'n':
        assertdate(csv_read("db.csv"))


def assertdate(dct):
    curdate = str(datetime.datetime.now())
    for key in dct.keys():
        if key == curdate[:11]:
            print(dct[key])


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
        dict1[date] = [action]
    return dict1


def csv_read(path):
    """
    Reads csv
    """
    if os.path.exists(path):
        with open(path, mode="r", encoding="utf-8") as file:
            first = file.readline()
            lines = file.readlines()
            dict = {}
            for line in lines:
                spl_line = line.split(",")
                for s in spl_line:
                    s = s.strip()
                dict[spl_line[0]] = dict.get(spl_line[0], []) + [spl_line[1].strip()]
        return dict
    else:
        with open(path, mode="w", encoding="utf-8") as file:
            file.write("Deadline,What_to_do" + "\n")
            dict = {}
        return dict


def csv_write(path, dict):
    """
    Writes csv
    """
    with open(path, mode="w", encoding="utf-8") as file:
        file.write("Deadline,What_to_do" + "\n")
        for key in dict:
            for task in dict[key]:
                file.write(key + "," + task + "\n")


def main():
    input_tasks()


main()
