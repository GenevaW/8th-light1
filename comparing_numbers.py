 #make program that user enters number and program tells user if its bigger than 10
numerics={'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,
'nine':9,'ten':10,'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,'fifteen':15,
'sixteen':16,'seventeen':17,'eighteen':18,'nineteen':19,'twenty':20,'twentyone':21,
'twentytwo':22,'twentythree':23,'twentyfour':24,'twentyfive':25,'twentysix':26,
'twentyseven':27,'twentyeight':28,'twentynine':29, 'thirty':30}

def int_input():

    print ("Enter 1 if you want to enter your numbers as integers eg. 7. \nOr Enter 2 if you want to enter your numbers written eg. seven")
    type  = raw_input()
    if type == '1':
        print("your numbers shall be entered as integers...")
        number = int(raw_input("please enter a number ... "))
        comparison = int(raw_input("please enter the comparison ... "))
    elif type == '2':
        print("your numbers shall be entered written...")
        number = raw_input("please enter a number ... ")
        comparison = raw_input("please enter the comparison ... ")
        number = number.lower()
        comparison = comparison.lower()
        number = numerics[number]
        comparison = numerics[comparison]
    else:
        print("your answer was invalid. please enter your numbers as integers...")
        number = int(raw_input("please enter a number ... "))
        comparison = int(raw_input("please enter the comparison ... "))


if number > comparison:
    print("%s is larger than %s" %(number,comparison))
elif number == comparison:
    print("%s is equal to %s" %(number,comparison))
else:
    print("%s is smaller than %s" %(number,comparison))
