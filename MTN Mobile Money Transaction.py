print("--- MTN Mobile Money Transaction ---")

amount = float(input("Enter the amount to send: GHS ")) # Assume user enters a number

# Determine charge based on amount
if amount <= 100:
    charge = 2
elif 100 < amount <= 500:
    charge = 5
else: # amount > 500
    charge = 10

final_amount = amount - charge

print("\n--- Transaction Summary ---")
print(f"Amount Sent: GHS {amount:}")
print(f"MoMo Charge: GHS {charge:}")
print(f"Amount Received by Recipient: GHS {final_amount:}")
