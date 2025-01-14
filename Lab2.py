#Program Name: Lab2.py
#Course: IT1114
#Name: Bampfield, Jaxon
#Assignment number: 2
#Due Date: ?
#Purpose: Program computes pizzas needed and salads needed
import math
def main():
    pizza = int(input("Enter number of people who want pizza: "))
    salad = float(input("Enter number of people that want salad: "))

    cost_of_salad = salad * 7.99

    num_of_pizza_slices = pizza * 3

    total_pizzas_ordered = math.ceil(num_of_pizza_slices / 12)

    cost_of_pizzas = total_pizzas_ordered * 15.99

    if total_pizzas_ordered > 10:
        pizza_discount = cost_of_pizzas * 0.15
    if total_pizzas_ordered < 10:
        pizza_discount = 0
    if salad > 10:
        salad_discount = cost_of_salad * 0.15
    if salad < 10:
        salad_discount = 0
    
    total_discount = pizza_discount + salad_discount

    total_cost = cost_of_pizzas + cost_of_salad

    delivery_fee = total_cost * 0.07

    if delivery_fee < 20:
        delivery_fee = 20

    total_cost_all = total_cost + delivery_fee - total_discount
    print("Pizzas Ordered:" , total_pizzas_ordered)
    print("Pizza cost $" , cost_of_pizzas)
    print("Salad cost $" , cost_of_salad)
    print("Total $" , total_cost )
    print("Discount $" , total_discount)
    print("delivery fee $" , delivery_fee)
    print("Total amount due $" , total_cost_all)
main()
