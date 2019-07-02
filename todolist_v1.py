import json

number = input("enter a number of event to do:")
list=[]
while len(list) <= int(number):
    items = event , time = [x for x in input("Enter event and time(wrt hour) here. please split with comma',' : ").split(',')]
    list.append(items)
    print("is that event done? ")
    completing=input("enter if yes = y , no = n : ")
    if completing == "n" :
        print(list.append("not completed"))
    else :
        print(list.append("completed"))

data = json.dumps(list)
print("all list: ")
print(data)
