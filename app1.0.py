print('welcome to the online supermarket')
input("please enter your name : ")
input('please enter your contact number or email : ')

potato = 15
potato = int(potato)
potatovalue = input("enter the amount of potatoes you need in kg's:")
potatovalue = int(potatovalue)
totalpotato = (potato * potatovalue)
totalpotato = int(totalpotato)
print(totalpotato)

onion = 20
onion = int(onion)
onionvalue = input("enter the amount of onions you need in kg's:")
onionvalue = int(onionvalue)
totalonion = (onion * onionvalue)
totalonion = int(totalonion)
print(totalonion)

tomato = 10
tomato = int(tomato)
tomatovalue = input("enter the amount of tomatoes you need in kg's:")
tomatovalue = int(tomatovalue)
totaltomato = (tomato * tomatovalue)
totaltomato = int(totaltomato)
print(totaltomato)

Cauliflower = 25
Cauliflower = int(Cauliflower)
Cauliflowervalue = input("enter the amount of cauliflowers you need in kg's:")
Cauliflowervalue = int(Cauliflowervalue)
totalcauliflower: int = (Cauliflower * Cauliflowervalue)
totalcauliflower = int(totalcauliflower)
print(totalcauliflower)

Cabbage = 27
Cabbage = int(Cabbage)
Cabbagevalue = input("enter the amount of cabbages you need in kg's:")
Cabbagevalue = int(Cabbagevalue)
totalcabbage = (Cabbage * Cabbagevalue)
totalcabbage = int(totalcabbage)
print(totalcabbage)


totalbill = totaltomato + totalonion + totalpotato + totalcauliflower + totalcabbage
totalbill = int(totalbill)
tax = 0.5
homedeliveycharge = 0.5
homecondition = input("if you want home delivery please type Y or if no then type N : ")


def finish_function():
    if homecondition == 'Y':
        print(totalbill + tax + homedeliveycharge)
    elif homecondition == 'N':
        print(totalbill + tax)


finish_function()
print('Your final total is above.')

Payment = input('''Please enter your payment method from the following
                    1. Please Enter 1 for UPI transaction
                    2. Please Enter 2 for Net banking
                    3. Please Enter 3 for Cash on Delivery
                    : ''')
