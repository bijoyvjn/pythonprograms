from functools import reduce

employe=[
    {"id":1000, "name":"bijoy", "salary":80000, "designation":"developer"},
    {"id":1001, "name":"arun", "salary":70000, "designation":"qa"},
    {"id":1002, "name":"cheru", "salary":50000, "designation":"developer"}
]

high=reduce(lambda sal1,sal2:sal1 if sal1>sal2 else sal2,
            list(map(lambda employe:employe["salary"],employe)))
print(high)