# Define the list of available mobile phones
mobile_phones = [
    {"brand": "Samsung", "model": "Galaxy S21", "price": 150000},
    {"brand": "Apple", "model": "iPhone 12", "price": 100000},
    {"brand": "OnePlus", "model": "9 Pro", "price": 60000},
    {"brand": "Google", "model": "Pixel 5", "price": 55000}
]

# Define a function to display the available mobile phones
def display_mobile_phones():
    print("Available mobile phones:")
    for index, mobile_phone in enumerate(mobile_phones):
        print(f"{index+1}. {mobile_phone['brand']} {mobile_phone['model']}: Rs.{mobile_phone['price']}")

# Define a function to handle the purchase of a mobile phone
def purchase_mobile_phone():
    # Display the available mobile phones
    display_mobile_phones()
    # Prompt the user to select a mobile phone to purchase
    selection = int(input("Enter the number of the mobile phone you wish to purchase: "))
    selected_mobile_phone = mobile_phones[selection-1]
    # Prompt the user to confirm the purchase
    print(f"You have selected the {selected_mobile_phone['brand']} {selected_mobile_phone['model']} for ${selected_mobile_phone['price']}.")
    confirm_purchase = input("Enter 'y' to confirm your purchase, or 'n' to cancel: ")
    if confirm_purchase == "y":
        print("Thank you for your purchase!")
    else:
        print("Purchase cancelled.")

# Call the purchase_mobile_phone function to start the program
purchase_mobile_phone()
