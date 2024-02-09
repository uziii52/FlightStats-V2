def display_airline_options():
    print("Airline Options:")
    print("1) Alaska Airlines")
    print("2) Delta Airlines")
    print("3) United Airlines")
    print("4) ExpressJet")

def display_flight_options():
    print("\nFlight Options:")
    print("1) ASM - Airline Seat Mile")
    print("2) RPM - Rate per Mile")
    print("3) Passengers")
    print("b) Go back")

def display_location_options():
    print("\nLocation Options:")
    print("1) Domestic")
    print("2) International")
    print("b) Go back")

# Main program
while True:
    display_airline_options()

    airline_choice = input("\nChoose an airline (1-4, or 'q' to quit): ")
    if airline_choice.lower() == 'q':
        break

    if airline_choice in ['1', '2', '3', '4']:
        while True:
            display_flight_options()
            flight_choice = input("\nChoose a flight option (1-3, or 'b' to go back): ")

            if flight_choice == 'b':
                break

            if flight_choice in ['1', '2', '3']:
                while True:
                    display_location_options()
                    location_choice = input("\nChoose a location option (1-2, or 'b' to go back): ")

                    if location_choice == 'b':
                        break

                    # Here you can perform calculations or actions based on the chosen options
                    print(f"Processing data for {airline_choice}, Flight Option {flight_choice}, Location Option {location_choice}...")
            else:
                print("Invalid flight option. Please choose again.")
    else:
        print("Invalid airline choice. Please choose again.")
