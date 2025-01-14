#Program Name: Lab2.py
#Course: IT1114
#Name: Bampfield, Jaxon
#Assignment number: 2
#Due Date: ?
#Purpose: Program computes pizzas needed and salads needed
import math
def main():
    pizza = int(input("Enter number of people that want pizza: "))
    salad = int(input("Enter number of people that want salad: "))

    cost_of_salad = salad * 7.99

    ppp = pizza * 3

    pizza_ordered = math.ceil(ppp / 12)

    total_cost_pizza = pizza_ordered * 15.99

    if pizza_ordered > 10:
        total_cost_pizza *= (1 - 0.15)

    total_cost = cost_of_salad + total_cost_pizza

    delivery_charge = total_cost * 0.07
    if delivery_charge < 20:
        delivery_charge = 20

    total_cost_with_delivery = total_cost + delivery_charge

    print("Pizzas Ordered:" , pizza_ordered)
    print("Total Pizza Cost:" , total_cost_pizza)
    print("Salad Cost:" , cost_of_salad)
    print("Delivery Charge:" , delivery_charge)
    print("Total Cost:" , total_cost_with_delivery)

main()
