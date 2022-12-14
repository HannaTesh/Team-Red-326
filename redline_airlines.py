import re
import pandas as pd
import matplotlib.pyplot as plt
import sys
import numpy as np

seat_data = pd.read_csv("flight_seating.csv")

class Passenger():
    """An instance of a class asks the user a series of questions that allows them 
    to get their most desired seat based on many aspects such as accommodations,
    price, seat preference, direct flight, and destination.
    
    Attributes:
    
    name(str): the name of user
    
    dob(int): date of birth of the user
    
    accommodation(boolean): Whether the user requires seating accommodation.
    TRUE for yes
    FALSE for no
    
    destination(string): string representation of the desired location 
    
    direct_flight(boolean): The status of whether the flight is connecting 
    (FALSE) or the flight is direct (TRUE)
    
    price(int): the price of flight ticket
    
    preference(string): the preference of seat location on the plane 
    (A, M, W)
    
    new_name(str): The user's input of the name of user
    
    new_dob(int): The user's input of the date of birth
    
    yes_accom(boolean): The status of the user's accommodation; TRUE or FALSE
    
    new_preference(string): Seat position on the plane (Aisle, Middle, Window)
    
    placement(string): the class placement on the plane as coach, business, and 
    first class (C, B, F)

    """

# Tega Ojegun
# Concept: Implementation of optional parameters.
    def __init__(self, name = ' ', dob = '', accommodation = 'FALSE', destination = '', direct_flight = 'TRUE', service_class = '', price = '0', preference = ''):
        """
        Args:
        
        name(str): name of user
        
        dob(int): the date of birth of the user
        
        accommodation(boolean): whether the user requires an accommodation, 
        TRUE or FALSE
        
        destination(string): desired location 
        
        direct_flight(boolean): User's choice of a connecting or direct flight
        
        price(int): price of flight
        
        preference(string): location of seat
        
        direct(boolean): whether the flight is a direct flight or connecting 
        flight. TRUE is for direct flight, FALSE represent a connect flight.
        
        """
        self.dob = dob
        self.name = name
        self.accommodation = accommodation
        self.destination = destination
        self.direct_flight = direct_flight
        self.service_class = service_class
        self.price = price
        self.preference = preference
        
# Patrick Polglase
# Concept: Implementation of with statement.
    def custom_greeting(self, new_name):
        """Opens a text file that reads a welcome message and replaces the 
        specified region with the string representation of the user's name.
        
        Args:
        new_name(string): the inputted name of user
        
        Side Effects:
        prints new content to the text file and prints said contents 
        into the console.
        """
        
        with open('welcome.txt', 'r+', encoding= "utf-8") as text_file:
            contents = text_file.read().replace('customer_name', str(new_name))
            print("========================================================================================================\n")
            print(contents)
    
# Andrew Liu
# Concept: Implementation of regular expression.
    def age_filter(self, new_dob):
        """ Uses the user's birth year to determine their age to see if 
        they're old enough to buy a plane ticket.
        
        Args:
        new_dob(int): YYYYMMDD (Year, Month, Day)

        Side Effects:
        Prints message to the console that determines if the user is above of
        below the age requirement.
        """
        
        age_regex = re.search(r"^\d{4}", new_dob)
        year = int(age_regex.group(0))
        age = 2022 - year
        
        if age >= 14:
            print(f"The user is {age} years old, they are able to purchase a ticket")
            print("========================================================================================================\n")
        else:
            print(f"The user is {age} years old, they are too young to purchase a ticket")
            print("========================================================================================================\n")
            sys.exit()
            
# Hanna Teshome
# Concept: Implementation of a custom list sorting with a key function; 
# lambda expression
    def accommodation_filter(self, yes_accom):
        """Filtering out dataset based on if user needs accommodations or not
        Args:
        yes_accom(boolean): TRUE if user needs an accommodation, FALSE if it not required.

        Side Effects:
        prints filtered dataset to the console 
        """

        if yes_accom == 'TRUE':
            seats = seat_data[["seat_id", "accommodation", "destination", "direct_flight", "service_class", "seat_prices", "seat_preference" ]] 
            true_accommodation = seat_data[(seat_data["accommodation"] == True)]
            accommodated_seats = pd.merge(seats, true_accommodation[["seat_id", "accommodation"]], how="right")
            accommodated_seats["seat_prices"] = accommodated_seats["seat_prices"].apply(lambda x: x - 30)
            print(f"Because you have decided to purchase an accomodation seat, there is a 30 dollar increase your ticket price")
            print(accommodated_seats)
            print("========================================================================================================\n")
            self.accommodated_seats = accommodated_seats
        elif yes_accom == 'FALSE':
            accommodated_seats = seat_data[["seat_id", "accommodation", "destination", "direct_flight", "service_class", "seat_prices", "seat_preference"]]
            print(accommodated_seats)
            print("========================================================================================================\n")
            self.accommodated_seats = accommodated_seats
        else:
            print("Invalid response")
            sys.exit()

# Meet Koradia
# Concept: Implementation of data visualization using pyplot.
            
    def destination_filter(self, new_location):
        """Gives the user the option of the location they want to travel to and the number of flights for each location
        Args:
        new_location(string): The location name

        Side Effects:
        prints filtered dataset to the console
        """
        
        if new_location == 'France':
            seats = self.accommodated_seats
            true_seats = seat_data[(seat_data["destination"] == 'France')]
            destination_seats = pd.merge(self.accommodated_seats, true_seats[["seat_id", "destination"]], how="inner")
            print(destination_seats)
            print("========================================================================================================\n")
            self.destination_seats = destination_seats
            
        elif new_location == 'Argentina':
            seats = self.accommodated_seats
            true_seats = seat_data[(seat_data["destination"] == 'Argentina')]
            destination_seats = pd.merge(seats, true_seats[["seat_id", "destination"]], how="inner")
            print(destination_seats)
            print("========================================================================================================\n")
            self.destination_seats = destination_seats
            
        elif new_location == 'Croatia':
            seats = self.accommodated_seats
            true_seats = seat_data[(seat_data["destination"] == 'Croatia')]
            destination_seats = pd.merge(seats, true_seats[["seat_id", "destination"]], how="inner")
            print(destination_seats)
            print("========================================================================================================\n")
            self.destination_seats = destination_seats
            
        elif new_location == 'Morocco':
            seats = self.accommodated_seats
            true_seats = seat_data[(seat_data["destination"] == 'Morocco')]
            destination_seats = pd.merge(seats, true_seats[["seat_id", "destination"]], how="inner")
            print(destination_seats)
            print("========================================================================================================\n")
            self.destination_seats = destination_seats
            
        else:
            seats = self.accommodated_seats
            #print(destination_seats)
            print("There are no available flights to that location")
            print("========================================================================================================\n")
            sys.exit()

        destcount = seat_data["destination"].value_counts()
        plt.title("Pie Chart Representing the Number of outgoing flights by Destination")
        plt.pie(destcount, labels = destcount.index)
        plt.show()
            
 # Andrew Liu
 # Implementation of merge operation using Pandas dataframe.          
    def direct_flight_filter(self, direct):
        """Allows user to pick if they want a direct of a connecting flight

        Args:
        direct(string): D for direct. C for connecting

        Side Effects:
        prints a filtered dataframe
        """
                
        if direct == 'D':
            seats = self.destination_seats
            true_direct = seat_data[(seat_data["direct_flight"] == True)]
            direct_seats = pd.merge(seats, true_direct[["seat_id", "direct_flight"]], how="inner")
            print(direct_seats)
            print("========================================================================================================\n")
            self.direct_seats = direct_seats
            
        elif direct == 'C':
            seats = self.destination_seats
            true_direct = seat_data[(seat_data["direct_flight"] == False)]
            direct_seats = pd.merge(seats, true_direct[["seat_id", "direct_flight"]], how="inner")
            print(direct_seats)
            print("========================================================================================================\n")
            self.direct_seats = direct_seats
            
        else:
            print("Invalid response")
            print("========================================================================================================\n")
            sys.exit()
            
# Patrick Polglase
# Concept: Implementation of an f string.         
    def seat_choice(self, placement):
        """ Allows user to select from a dataframe of available seats that 
        match their preferred class placement.

        Args:
            placement (str): The location of the seating class onboard the 
            plane. A string character of 'C', 'B', or 'F'
        """
    
        seats = self.direct_seats
        preferred_placement = seat_data[(seat_data["service_class"] == placement)]
        placement_seats = pd.merge(seats, preferred_placement[["seat_id", "service_class"]], how="inner") 
        print(placement_seats)
        print(f"Here are all the seats available based off your selected placement: {placement}")
        print("========================================================================================================\n")
        self.placement_seats = placement_seats
            
# Hanna Teshome 
# Concept: Implementation of a conditional expression
    def price_filter(self, new_price):
        """ Allows user to see what seats are available based on their ticket 
        price budget 
        
        Args:
        new_price(int): The highest cost the user is willing to pay

        Side Effects:
        prints out a filtered dataset and a message to the console 
        containing the selected placement.
        
        """

        price = int(new_price)

        if price < 55:
            print("There are no available seats within that price range")
        elif price < 100:
            seats = self.placement_seats
            priced_seats = seat_data[(seat_data['seat_prices'] <= price)]
            merged_seats = pd.merge(seats, priced_seats[['seat_id', 'seat_prices', 'service_class']], how='inner')
            print(merged_seats)
            print("========================================================================================================\n")
            self.merged_seats = merged_seats
        elif price < 360:
            seats = self.placement_seats
            priced_seats = seat_data[(seat_data['seat_prices'] <= price)]
            merged_seats = pd.merge(seats, priced_seats[['seat_id', 'seat_prices', 'service_class']], how='inner')
            print(merged_seats)
            print("========================================================================================================\n")
            self.merged_seats = merged_seats
        elif price < 1400:
            seats = self.placement_seats
            priced_seats = seat_data[(seat_data['seat_prices'] <= price)]
            merged_seats = pd.merge(seats, priced_seats[['seat_id', 'seat_prices', 'service_class']], how='inner')
            print(merged_seats)
            print("========================================================================================================\n")
            self.merged_seats = merged_seats
        else:
            merged_seats = self.placement_seats
            print(merged_seats)
            self.merged_seats = merged_seats

            print("There are no available seats for that price. Try Spirit Airlines!") if price < 55 else print("Here are seats within your budget!")
            print("========================================================================================================\n")
    
# Meet Koradia
# Concept: Implementation of data visualization using pyplot.
    def seat_preference_filter(self, new_preference):
        """Allows user to pick where in the plane they want to sit and displays
        a pie chart of the percentage of seats by flight class

        Args
        new_preference(string): Aisle(A), Middle(M), Window(M)

        Side Effects:
        prints filtered dataframe and a message to the console
        """
                
        if new_preference == "M":
            seats = self.merged_seats
            seat_preference = seat_data[(seat_data["seat_preference"] == "M")]
            seat_location = pd.merge(seats, seat_preference[["seat_id", "seat_preference"]], how="inner")
            print(seat_location)
            print("Here are all the middle seats available")
            print("========================================================================================================\n")
            self.seat_location = seat_location
            
        if new_preference == "A":
            seats = self.merged_seats
            seat_preference = seat_data[(seat_data["seat_preference"] == "A")]
            seat_location = pd.merge(seats, seat_preference[["seat_id", "seat_preference"]], how="inner")
            print(seat_location)
            print("Here are all the middle seats available")
            print("========================================================================================================\n")
            self.seat_location = seat_location
            
        if new_preference == "W":
            seats = self.merged_seats
            seat_preference = seat_data[(seat_data["seat_preference"] == "W")]
            seat_location = pd.merge(seats, seat_preference[["seat_id", "seat_preference"]], how="inner")
            print(seat_location)
            print("Here are all the middle seats available")
            print("========================================================================================================\n")
            self.seat_location = seat_location

        seatcount = seat_data["seat_preference"].value_counts()
        plt.title("Chart Representing the Seats Available by Flight Class")
        plt.pie(seatcount, labels = seatcount.index)
        plt.show()

# Tega Ojegun 
# Concept: Implementation of sequence unpacking.         

def boarding_ticket():
    """Displays users information and prints it out as a boarding ticket
    
    Side Effects:
        Prints out all of the user inputs and displays the the subsequent 
        passenger information on the boarding ticket.

    """

    passenger = Passenger()

    print("========================================================================================================\n")
    name = input("what is your name \n")
    passenger.custom_greeting(name)

    year = input("what is your date of birth? Format: YYYYMMDD \n")
    passenger.age_filter(year)

    acc = input("Enter TRUE or FALSE to if you need accommodations: \n")
    passenger.accommodation_filter(acc)

    dest = input("Please enter your desired destination. Today's available locations are: France, Argentina, Croatia, and Morocco \n")
    passenger.destination_filter(dest)

    dir = input("Enter D if you would like to board a direct flight or C if you would like to board a connecting flight: \n")
    passenger.direct_flight_filter(dir)

    sc = input("Would you like to fly coach, business, or first class? Coach(C), Business(B), First Class(F). \n")
    passenger.seat_choice(sc)

    pr = input("What's the most you're willing to spend on this ticket? \n")
    passenger.price_filter(pr)

    loc = input("Would you like a middle, aisle, or window seat? Middle(M), Aisle(A), Window(W). Aisle is reserved for accommodations and has a higher price point \n")
    passenger.seat_preference_filter(loc)

    boarding_ticket = [name, year, acc, dest, dir, sc, pr, loc]

    name, dob,accommodation,destination,direct_flight,seat_choice,price_filter,seat_preference = boarding_ticket

    print("========================================================================================================\n")
    print("Boarding Ticket Information:")
    print(f" NAME: {name} \n DOB: {dob} \n ACCOMMODATION: {accommodation} \n DESTINATION: {destination} \n DIRECT FLIGHT: {direct_flight} \n SEAT CHOICE: {seat_choice} \n PRICE: ${price_filter} \n SEAT PREFERENCE: {seat_preference}")
    print(f" Thank you for choosing Redline Airlines! Enjoy your flight {name}!")
    print("========================================================================================================\n")

# Meet Koradia
# Concept: Implementation of a magic method __str__().

def __str__(self):
    """The informal string representation of the Passenger object detailing the 
    flight information to the end user.

    Returns:
        str: Returns the string representation of the passenger object and its attributes. 
    """
    return f'Name: {self.name}, DOB: {self.dob}, Accommodation: {self.accommodation}, Destination: {self.destination}, Direct-Flight: {self.direct_flight}, Class: {self.service_class}, Price: {self.price}, Preference: {self.preference}'   

if __name__ == "__main__":
    boarding_ticket()
