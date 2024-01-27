def line(katz_deli):
    if not katz_deli:
        print("The line is currently empty.")
        return

    result = []
    for index, name in enumerate(katz_deli, start=1):
        result.append(f"Welcome, {name}. You are number {index} in line.")
    
    return result

katz_deli = ["Alice", "Bob", "Charlie"]
list_of_customers = line(katz_deli)
for customer in list_of_customers:
    print(customer)


def take_a_number(katz_deli, name):
    katz_deli.append(name)
    position = len(katz_deli)
    print(f"Welcome, {name}. You are number {position} in line.")
    return katz_deli

# Example usage:
katz_deli = ["Alice", "Bob", "Charlie"]
take_a_number(katz_deli, "David")


def now_serving(katz_deli):
    if not katz_deli:
        print("There is nobody waiting to be served!")
    else:
        serving_customer = katz_deli.pop(0)
        print(f"Currently serving {serving_customer}.")

    return katz_deli

# Example usage:
katz_deli = ["Logan", "Avi", "Spencer"]
now_serving(katz_deli)  # Should print "Currently serving Logan."


