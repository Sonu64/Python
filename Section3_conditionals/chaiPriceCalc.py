cupSize = input("Choose a Cup Size: (Small, Medium, Large)").lower()

if cupSize == "small":
    print(f"Price is 10 Rupees.")
elif cupSize == "medium":
    print(f"Price is 20 Rupees.")
elif cupSize == "large":
    print(f"Price is 40 Rupees.")
else:
    print(f"Unknown Cup Size !!")