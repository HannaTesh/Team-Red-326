import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class Passenger():
    
    #Andrew Liu
    def __init__(self, name = ' ', dob = '20221211', accomodation = 'FALSE', destination = 'France', direct_flight = 'TRUE', service_class = 'C', price = '0', preference = 'A'):
        
        self.dob = dob
        self.name = name
        self.accomodation = accomodation
        self.destination = destination
        self.direct_flight = direct_flight
        self.service_class = service_class
        self.price = price
        self.preference = preference
        
    #Patrick: with statement
    def custom_greeting(self, new_name):
        
        with open('welcome.txt', 'r+', encoding= "utf-8") as text_file:
            contents = text_file.read().replace('customer_name', str(new_name))
            print(contents)
    
    #Andrew Liu 
    def age_filter(self, new_dob):
        
        age_regex = re.search(r"^\d{4}", new_dob)
        year = int(age_regex.group(0))
        age = 2022 - year
        
        if age >= 14:
            print(f"The user is {age} years old, they are able to purchase a ticket")
        else:
            print(f"The user is {age} years old, they are too young to purchase a ticket")
            
        
    def accommodation_filter(self, accom):
        
        seat_data = pd.read_csv("flight_seating.csv")
        
        if accom == 'TRUE':
            seats = seat_data[["seat_id", "accommodation", "destination", "direct_flight", "service_class", "seat_prices", "seat_preference" ]] 
            true_accommodation = seat_data[(seat_data["accommodation"] == True)]
            accommodated_seats = pd.merge(seats, true_accommodation[["seat_id", "accommodation"]], how="right")
            print(accommodated_seats)
            self.accommodated_seats = accommodated_seats
        else:
            accommodated_seats = seat_data[["seat_id", "accommodation", "destination", "direct_flight", "service_class", "seat_prices", "seat_preference"]]
            print(accommodated_seats)
            self.accommodated_seats = accommodated_seats

# Meet Koradia
            
    def destination_filter(self, new_location):
        
        seat_data = pd.read_csv("flight_seating.csv")
        
        if new_location == 'France':
            seats = self.accommodated_seats
            true_seats = seat_data[(seat_data["destination"] == 'France')]
            destination_seats = pd.merge(self.accommodated_seats, true_seats[["seat_id", "destination"]], how="inner")
            print(destination_seats)
            self.destination_seats = destination_seats
            
        elif new_location == 'Argentina':
            seats = self.accommodated_seats
            true_seats = seat_data[(seat_data["destination"] == 'Argentina')]
            destination_seats = pd.merge(seats, true_seats[["seat_id", "destination"]], how="inner")
            print(destination_seats)
            self.destination_seats = destination_seats
            
        elif new_location == 'Croatia':
            seats = self.accommodated_seats
            true_seats = seat_data[(seat_data["destination"] == 'Croatia')]
            destination_seats = pd.merge(seats, true_seats[["seat_id", "destination"]], how="inner")
            print(destination_seats)
            self.destination_seats = destination_seats
            
        elif new_location == 'Morocco':
            seats = self.accommodated_seats
            true_seats = seat_data[(seat_data["destination"] == 'Morocco')]
            destination_seats = pd.merge(seats, true_seats[["seat_id", "destination"]], how="inner")
            print(destination_seats)
            self.destination_seats = destination_seats
            
        else:
            seats = self.accommodated_seats
            print(destination_seats)
            self.destination_seats = destination_seats

        seat_data = pd.read_csv("flight_seating.csv")
        destcount = seat_data["destination"].value_counts()
        plt.pie(destcount, labels = destcount.index)
        plt.show()
            
            
    def direct_flight_filter(self, direct):
        
        seat_data = pd.read_csv("flight_seating.csv")
        
        if direct == 'D':
            seats = self.destination_seats
            true_direct = seat_data[(seat_data["direct_flight"] == True)]
            direct_seats = pd.merge(seats, true_direct[["seat_id", "direct_flight"]], how="inner")
            print(direct_seats)
            self.direct_seats = direct_seats
            
        else:
            seats = self.destination_seats
            true_direct = seat_data[(seat_data["direct_flight"] == False)]
            direct_seats = pd.merge(seats, true_direct[["seat_id", "direct_flight"]], how="inner")
            print(direct_seats)
            self.direct_seats = direct_seats
            
    def seat_choice(self, placement): 

        seat_data = pd.read_csv("flight_seating.csv")
    
        seats = self.direct_seats
        preferred_placement = seat_data[(seat_data["service_class"] == placement)]
        placement_seats = pd.merge(seats, preferred_placement[["seat_id", "service_class"]], how="inner") 
        print(placement_seats)
        print("Here are all the coach seats available")
        self.placement_seats = placement_seats
            
         
    def price_filter(self, new_price):
        
        # Clean up
        
        seat_data = pd.read_csv("flight_seating.csv")
        
        price = int(new_price)
        
        if price < 69:
            print("There are no available seats within that price range")
        elif price < 100:
            seats = self.placement_seats
            priced_seats = seat_data[(seat_data['seat_prices'] <= price)]
            merged_seats = pd.merge(seats, priced_seats[['seat_id', 'seat_prices', 'service_class']], how='inner')
            print("Here are seats within your budget.")
            print(merged_seats)
            self.merged_seats = merged_seats
        elif price < 360:
            seats = self.placement_seats
            priced_seats = seat_data[(seat_data['seat_prices'] <= price)]
            merged_seats = pd.merge(seats, priced_seats[['seat_id', 'seat_prices', 'service_class']], how='inner')
            print("Here are seats within your budget.")
            print(merged_seats)
            self.merged_seats = merged_seats
        elif price < 1400:
            seats = self.placement_seats
            priced_seats = seat_data[(seat_data['seat_prices'] <= price)]
            merged_seats = pd.merge(seats, priced_seats[['seat_id', 'seat_prices', 'service_class']], how='inner')
            print("Here are seats within your budget.")
            print(merged_seats)
            self.merged_seats = merged_seats
        else:
            merged_seats = self.placement_seats
            print("All seats are within your budget")
            print(merged_seats)
            self.merged_seats = merged_seats
    
# Meet Koradia

    def seat_preference_filter(self, new_preference):
        
        seat_data = pd.read_csv("flight_seating.csv")
        
        if new_preference == "M":
            seats = self.merged_seats
            seat_preference = seat_data[(seat_data["seat_preference"] == "M")]
            seat_location = pd.merge(seats, seat_preference[["seat_id", "seat_preference"]], how="inner")
            print(seat_location)
            print("Here are all the middle seats available")
            self.seat_location = seat_location
            
        if new_preference == "A":
            seats = self.merged_seats
            seat_preference = seat_data[(seat_data["seat_preference"] == "A")]
            seat_location = pd.merge(seats, seat_preference[["seat_id", "seat_preference"]], how="inner")
            print(seat_location)
            print("Here are all the middle seats available")
            self.seat_location = seat_location
            
        if new_preference == "W":
            seats = self.merged_seats
            seat_preference = seat_data[(seat_data["seat_preference"] == "W")]
            seat_location = pd.merge(seats, seat_preference[["seat_id", "seat_preference"]], how="inner")
            print(seat_location)
            print("Here are all the middle seats available")
            self.seat_location = seat_location

        seatcount = seat_data["seat_preference"].value_counts()
        plt.pie(seatcount, labels = seatcount.index)
        plt.show() 
                 
def demo():
    
    passenger = Passenger()
    
    #passenger.custom_greeting(input("what is your name \n"))

    passenger.age_filter(input("what is your date of birth? Format: YYYYMMDD \n"))
    
    passenger.accommodation_filter(input("Enter TRUE or FALSE to if you need accommodations: \n"))
    
    passenger.destination_filter(input("Please enter your desired destination. Today's available locations are: France, Argentina, Croatia, and Morocco \n"))
    
    passenger.direct_flight_filter(input("Enter D if you would like to board a direct flight or C if you would like to board a connecting flight: \n"))
    
    passenger.seat_choice(input("Would you like to fly coach, buisness, or first class? Coach(C), Buisness(B), First Class(F). \n"))
    
    passenger.price_filter(input("What's the most you're willing to spend on this ticket? \n"))
    
    passenger.seat_preference_filter(input("Would you like a middle, aisle, or window seat? Middle(M), Aisle(A), Window(W). Asile is reserved for accomodations and has a higher price point \n"))

# Meet Koradia

def __repr__(self):
    return f'Name: {self.name}, DOB: {self.dob}, Accomodation: {self.accomodation}, Destination: {self.destination}, Direct-Flight: {self.direct_flight}, Class: {self.service_class}, Price: {self.price}, Preference: {self.preference}'   

if __name__ == "__main__":
    demo()
