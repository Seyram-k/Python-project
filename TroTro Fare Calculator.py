print("=== TroTro Fare Calculator ===")

# Getting user input
route_input = input("Enter your route (e.g., 'Accra to Madina'): ").lower()
num_passengers = int(input("How many passengers are boarding? "))

# Define fares
fares = {
    "accra to madina": 5,
    "accra to kasoa": 10,
    "accra to tema": 8
}

# Calculate fare based on route
if route_input in fares:
    base_fare = fares[route_input]
    total_fare = base_fare * num_passengers
    print(f"\nRoute: {route_input.title()}")
    print(f"Number of Passengers: {num_passengers}")
    print(f"Total Fare: GHS {total_fare:}")
else:
    print("Sorry, that route is not available. Please choose from Accra to Madina, Accra to Kasoa, or Accra to Tema.")
