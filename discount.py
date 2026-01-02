def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    Only applies the discount if it is 20% or higher.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Main program to get user input
try:
    # 1. Prompt the user for input
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    # 2. Call the function
    final_price = calculate_discount(original_price, discount_percentage)

    # 3. Print the results
    if final_price != original_price:
        print(f"Discount applied. The final price is: {final_price}")
    else:
        print(f"No discount applied (less than 20%). The price remains: {original_price}")

except ValueError:
    print("Please enter valid numbers for the price and discount.")
