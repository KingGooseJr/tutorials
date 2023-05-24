# eaten_peas = True
# eaten_carrots = False

# if eaten_peas or eaten_carrots:
#     print('You get ice cream')
# else:
#     print('Nothing for you!')

give_me_money = False
fuel_my_car = False

if (give_me_money or fuel_my_car) and not (give_me_money and fuel_my_car):
    print('Thank you')
elif give_me_money and fuel_my_car:
    print('No you are too generous')
else:
    print('I need your help!')

if give_me_money and fuel_my_car:
    print('No you are too generous')
elif give_me_money or fuel_my_car:
    print('Thank you')
else:
    print('I need your help!')