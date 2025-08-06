def generate_invoice(customer_name: str="Guest", *items: str, **charges: float) -> str:
    print(f"Invoice for {customer_name}\n")
    total = 0.0
    if items:
        print(f"Items:\n")
        for item in items:
            print(f"-{item}\n")
    if charges:
        print(f"Charges:\n")
        for charge, amount in charges.items():
            print(f"{charge.capitalize()}: {amount}\n")
            total += float(charges[charge])
    print(f"Total Amount Due: ₹{total}.\n")

#generate_invoice("Amit", "Burger", "Fries", tax=50.0, service=20.0)
generate_invoice()

