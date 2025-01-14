def main():
    l = float(input("Enter the Length: "))
    w = float(input("Enter the Width: "))
    fpsf = float(input("Enter the cost of the flooring per swuare foot: "))

    square_feet = l * w #calculating total square feet

    flooring_cost = square_feet * fpsf #calculating flooring cost

    tax = flooring_cost * .07 #calculating tax

    total_cost = flooring_cost + tax #calculating total cost of everything

    print("Square Feet:" , square_feet)
    print("Flooring:" , flooring_cost)
    print("Tax:" , tax)
    print("Total: " , total_cost)

main()
