import os


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
                dict[spl_line[0]] = dict.get(spl_line[0], []) + [spl_line[1].strip()]
        return dict
    else:
        with open(path, mode="w", encoding="utf-8") as file:
            file.write("Deadline,What_to_do")
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





