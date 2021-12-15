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
    return (duedate, priority, task)
def multi_input(dct):
    answer = input("Continue adding tasks? y/n")
    while answer != 'y' or answer != 'n':
        if answer == 'y':
            input_tasks()
        if answer == 'n':
            return dct
def assertdate(dct):
    curdate = str(datetime.datetime.now())
    for key in dct.keys():
        if key == curdate[:11]:
            return dct[key]
