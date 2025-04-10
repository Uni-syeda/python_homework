import csv
import traceback
import custom_module
import pprint

#-------------------------------------#
def read_employees():
    data = {}
    rows = []
    
    try:
        with open("../csv/employees.csv", "r", newline="") as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                if i == 0:
                    data["fields"] = row
                else:
                    rows.append(row)
        data["rows"] = rows
        return data
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        exit(1)
employees = read_employees()  

#-------------------------------------#
def column_index(column_name):
    return employees["fields"].index(column_name)
employee_id_column = column_index("employee_id")

#-------------------------------------#

def first_name(employee_index):
    return employees["rows"][employee_index][column_index("first_name")]
#-------------------------------------#
def employee_find(index):
    matches = []
    for row in employees["rows"]:
        if row[0] == str(index):
            matches.append(row)
    return matches
#-------------------------------------#

def employee_find_2(index):
    sorted_rows = sorted(employees["rows"], key=lambda row: row[1])  # sort by first_name (index 1)
    return [sorted_rows[index]]
#-------------------------------------#

def sort_by_last_name():
    sorted_rows = sorted(employees["rows"], key=lambda row: row[column_index("last_name")])
    #pprint.pprint("DEBUG------------------>:",sorted_rows)
    return sorted_rows

#-------------------------------------#
def employee_dict(row):
    return {
        field: value
        for field, value in zip(employees["fields"], row)
        if field != "employee_id"
    }

#-------------------------------------#
def all_employees_dict():
    result = {}
    for row in employees["rows"]:
        emp_id = row[column_index("employee_id")]
        result[emp_id] = {
            field: value
            for field, value in zip(employees["fields"], row)
            if field != "employee_id"
        }
    return result

#-------------------------------------#
def get_this_value():
    return "ABC"

#-------------------------------------#

def set_that_secret(value):
    custom_module.set_that_secret(value)

#-------------------------------------#
minutes1 = None  # Global variable

def read_minutes():
    global minutes1


    minutes1 = [
        ("Alice Smith", "November 12, 1990"),
        ("Tony Henderson", "November 15, 1991"),
        ("John Doe", "November 20, 1992")
    ]

    minutes2 = [
        ("Bob Brown", "November 17, 1987"),
        ("Linda White", "November 18, 1986"),
        ("Sarah Murray", "November 19, 1988")
    ]

    d1 = {"rows": minutes1}
    d2 = {"rows": minutes2}

    return d1, d2
#-------------------------------------#

minutes_set = None  # Global variable

def create_minutes_set():
    global minutes_set

    minutes_set = set()

    for i in range(1, 47):  # 1 to 46 inclusive
        entry = f"Person {i}"
        minutes_set.add(entry)

    return minutes_set

#-------------------------------------#
from datetime import datetime

minutes_list = None  # Global variable

def create_minutes_list():
    global minutes_list

    # Simulated data with (name, date string)
    raw_data = [
        ("Alice Smith", "November 12, 1990"),
        ("Tony Henderson", "November 15, 1991"),
        ("Sarah Murray", "November 19, 1988")
    ]

    # Convert date strings to datetime objects
    minutes_list = [(name, datetime.strptime(date_str, "%B %d, %Y")) for name, date_str in raw_data]

    return minutes_list

#-------------------------------------#
import os
import csv
from datetime import datetime

def write_sorted_list():
    # Simulated unsorted data
    data = [
        ("Alice Smith", "November 12, 1990"),
        ("Jason Tucker", "September 20, 1980"),
        ("Tony Henderson", "November 15, 1991"),
        ("Sarah Murray", "November 19, 1988")
    ]

    # Sort by date
    sorted_list = sorted(data, key=lambda x: datetime.strptime(x[1], "%B %d, %Y"))

    # Write to minutes.csv
    with open("minutes.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Date"])
        writer.writerows(sorted_list)

    return sorted_list

pprint.pprint(employees)

