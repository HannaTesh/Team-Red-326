import pandas as pd
import re


class Passenger:
    """Declaration of a Passenger class that accounts for passenger information such as name, date of birth, whether the person has accommodations, what service class they belong to, and their preference of seat within the row.

    Attributes:
	    name (str): the name of the user
	    dob (int): the users date of birth
	    accommodation_status(bool): Whether or not the user has a seating accommodation
	    accommodation_type(str): Type of accommodation
	    service_class(str): The class the user will be in 
	    seat_preference(str): The users preferred seat
    """
    
    def __init__(self, name, dob, accommodation, service_class, seat_preference, price):
        """Current booking with Customer information

	    Args:
	        name(str): Name of user
	        dob(int): Date of birth of user
	        accommodation_status(bool): Whether or not the person has a seating accommodation
	        accommodation_type(str): What type of accommodation the user possesses, must be one of these three senior, pregnant, disabled.
	        service_class(str): The service class section of the airplane where the user will be seated.
	        seat_preference(str): The preference in the seat the user wants
        """
        #connecting flights, 
        seat_data = pd.read_csv("flight 201 seating chart.csv")
        self.name = name
        self.dob = dob
        self.accomodation = accommodation
        self.service_class = service_class
        self.seat_preference = seat_preference
        self.price = price
        

    def Flight_Booking(filepath):
        """reads a data file and place it into a dataframe
    
        Args:
        filepath(str): file path to the data
    
        Side effect:
        Reads data file and appends it to a dataframe"""
        
        filepath = pd.read_csv("flight 201 seating chart.csv")
        

    #def seat_filter(self, seats):
        #"""Uses pandas to filter a table of seats
        
        #Args:
            #seats(int): number of seats available
	
	    #Side Effects: 
        #Sets a new filtered table of seats
        #"""
        
    def age_filter(filepath):
        
        # access the file path
        # reads the user inputted age (Format: "year/mm/dd")
        # uses regex to a determine whether a passenger is over the age of 14
        # If under the age of 14 "You cant fly alone"
        
        filepath = pd.read_csv("flight 201 seating chart.csv")
        
        dob = input("what is your date of birth? Format: year")
        
        age_regex = re.search(r"^\d{4}", dob)
        
        year = int(age_regex.group(0))
        
        age = 2022 - year
        
        if age >= 14:
            print(f"The user is {age} years old, they are able to purchase a ticket")
            
        else:
            print(f"The user is {age} years old, they are too young to purchase a ticket")
        
        
    def accomodation_filter(self):
        
        #access the filepath
        #read the user input of desired accomodation 
        #if accomodation is need, accomodation seats will be displayed to choose from, accomodation seats will cost less
        #if not, all seats will be displayed
        seat_data = pd.read_csv("flight_seating.csv")

        person_with_accommodation = input("Enter TRUE or FALSE to if you need accommodations:")
        if person_with_accommodation == 'TRUE':
            seats = seat_data[["seat_id", "accommodation"]] 
            true_accomodation = seat_data[(seat_data["accommodation"] == True)]
            accommodated_seats = pd.merge(seats, true_accom[["seat_id", "accommodation"]], how="right")
            print(accommodated_seats)
        else:
            all_seats = seat_data[["seat_id", "accommodation"]]
            print(all_seats)   
        
    def service_class_filter(self):
        
        #access the filepath
        #read the user input of desired service class
        #conditional will display available seats based on desired service class (F, B, C)
        #Help: Accomadation and pricing 
        #If budget input is 80 and the user needs an accomadation, the user cannot afford the ticket
        
        seat_data = pd.read_csv("flight_seating.csv")
        price_str = input("What's the most you're willing to spend on this ticket?")
        price = int(price_str)
        
        if price < 69:
            print("There are no available seats within that price range")
            
        elif price < 100:
            priced_seats = seat_data[(seat_data['seat_prices'] <= price)]
            seats = seat_data[['seat_id', 'seat_prices', 'service_class']]
            merged_seats = pd.merge(seats, priced_seats[['seat_id', 'seat_prices', 'service_class']], how='right')
            print("Here are seats within your budget. You're only able to purchase coach")
            print(merged_seats)
            
        elif price < 360:
            priced_seats = seat_data[(seat_data['seat_prices'] <= price)]
            seats = seat_data[['seat_id', 'seat_prices', 'service_class']]
            merged_seats = pd.merge(seats, priced_seats[['seat_id', 'seat_prices', 'service_class']], how='right')
            print("Here are seats within your budget. You're able to purchase either coach or buisness")
            print(merged_seats)
            
        elif price < 1400:
            priced_seats = seat_data[(seat_data['seat_prices'] <= price)]
            seats = seat_data[['seat_id', 'seat_prices', 'service_class']]
            merged_seats = pd.merge(seats, priced_seats[['seat_id', 'seat_prices', 'service_class']], how='right')
            print("Here are seats within your budget. You're able to purchase coach, buisness, or first class")
            print(merged_seats)
            
        else:
            seats = seat_data[['seat_id', 'seat_prices', 'service_class']]
            print("Here are seats within your budget")
            print(seats)
            
        
            
    def seat_preference_filter():
        
        #access the filepath
        #read the user input of desired seat_preference
        #conditional will display available seats based on desired seat_preference (A, M, W)
        seat_data = pd.read_csv("flight 201 seating chart.csv")
        preference = input("Would you like a middle, aisle, or window seat? Middle(M), Aisle(A), Window(W). Asile is reserved for accomodations and has a higher price point")
        if preference == "M":
            perfered_seats = seat_data[(seat_data["seat_preference"] == "M") & (seat_data["seat_id"])]
            print(perfered_seats)
            print("Here are all the middle seats available")
        if preference == "A":
            perfered_seats = seat_data[(seat_data["seat_preference"] == "A") & (seat_data["seat_id"])]
            print(perfered_seats)
            print("Here are all the Aisle seat available")
        if preference == "W":
            perfered_seats = seat_data[(seat_data["seat_preference"] == "W") & (seat_data["seat_id"])]
            print(perfered_seats)
            print("Here are all the window seats available")
        
        
        
        
        
        
    def __repr__(self):
        #Show final seat the user selects based on criteria they inputted.(Input values narrowed down)
        
    def main(filepath, available_seats, available_subcategory):
        """Merges the information from class person and class reservation

	    Args:
		    Filepath(str): path to the file
		    Available_seats(int): seats available
		    available _subcategory(str): class of seats available

	    Side Effects:
	    Merging of class person and class reservation
        """
        
    def arg_parse(args):
        """Processes command line argument

        Args:
	        args(list of strings): command-line arguments
        """
