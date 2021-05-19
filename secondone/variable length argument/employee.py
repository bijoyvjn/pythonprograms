emp={
    1004:{"eid":104, "name":"bijoy","salary":45454,"desig":"hr"},
    1005:{"eid":105, "name":"arun","salary":85157,"desig":"clerk"}
}

def printe(**kwargs):
    id=kwargs["id"]
    prop=kwargs["prop"]

    if id in emp:
        print(emp[id]["name"])
        print(emp[id][prop])
    else:
        print("invalid id")

printe(id=1004,prop="desig")