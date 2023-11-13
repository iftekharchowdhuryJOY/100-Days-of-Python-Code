print("Thank you for choosing python pizza deliveries")
pizza_size = input("Enter your Pizza SIZE? S,M, L: ")  # S, M, L

add_pepperoni = input("Do you want pepperoni? Y or N: ")

extra_cheese = input("Do you want extra cheese? Y or N: ")
total_bill = 0
pepperoni_price_medium_or_large_pizza = 3
extra_cheese_for_any_size_pizza = 1

if pizza_size == 'S':
    small_pizza_price = 15

    pepperoni_price_small_pizza = 2
    extra_cheese_price_for_small_pizza = 1

    if add_pepperoni == 'Y' and extra_cheese == 'Y':
        total_bill = small_pizza_price + pepperoni_price_small_pizza + extra_cheese_price_for_small_pizza
        print(f"Thank you choosing python Pizza Deliveries! Your final bill is: ${total_bill}")

    if add_pepperoni == 'Y':
        total_bill = small_pizza_price + pepperoni_price_small_pizza
        print(f"Thank you choosing python Pizza Deliveries! Your final bill is: ${total_bill}")

    if extra_cheese == 'Y':
        total_bill = small_pizza_price + extra_cheese_price_for_small_pizza
        print(f"Thank you choosing python Pizza Deliveries! Your final bill is: ${total_bill}")

    if add_pepperoni == 'N' and extra_cheese == 'N':
        print(f"Thank you choosing python Pizza Deliveries! Your final bill is: ${total_bill}")

if pizza_size == 'M':
    medium_pizza_price = 20
    pepperoni_price_medium_or_large_pizza = 3

    if add_pepperoni == 'Y':
        total_bill = medium_pizza_price + pepperoni_price_medium_or_large_pizza
        print(f"Thank you choosing python Pizza Deliveries! Your final bill is: ${total_bill}")

    if extra_cheese == 'Y':
        total_bill = medium_pizza_price + extra_cheese_for_any_size_pizza
        print(f"Thank you choosing python Pizza Deliveries! Your final bill is: ${total_bill}")

    if add_pepperoni == 'Y' and extra_cheese == 'Y':
        total_bill = medium_pizza_price + pepperoni_price_medium_or_large_pizza + extra_cheese_for_any_size_pizza
        print(f"Thank you choosing python Pizza Deliveries! Your final bill is: ${total_bill}")

    if add_pepperoni == 'N' and extra_cheese == 'N':
        print(f"Thank you choosing python Pizza Deliveries! Your final bill is: ${total_bill}")

if pizza_size == 'L':
    large_pizza_price = 25
    pepperoni_price_medium_or_large_pizza = 3

    if add_pepperoni == 'Y':
        total_bill = large_pizza_price + pepperoni_price_medium_or_large_pizza
        print(f"Thank you choosing python Pizza Deliveries! Your final bill is: ${total_bill}")

    if extra_cheese == 'Y':
        total_bill = large_pizza_price + extra_cheese_for_any_size_pizza
        print(f"Thank you choosing python Pizza Deliveries! Your final bill is: ${total_bill}")

    if add_pepperoni == 'Y' and extra_cheese == 'Y':
        total_bill = large_pizza_price + pepperoni_price_medium_or_large_pizza + extra_cheese_for_any_size_pizza
        print(f"Thank you choosing python Pizza Deliveries! Your final bill is: ${total_bill}")

    if add_pepperoni == 'N' and extra_cheese == 'N':
        print(f"Thank you choosing python Pizza Deliveries! Your final bill is: ${total_bill}")

