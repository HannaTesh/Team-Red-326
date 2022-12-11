import pandas as pd
import re

class Passenger:
    """Declaration of a Passenger class that accounts for passenger information 
       such as name, date of birth, whether the person has accommodations, 
       what service class they belong to, and their preference of seat within 
       the row.

    Attributes:
	    name(str): the name of the user.
     
	    dob(int): the user's date of birth.
     
	    accommodation_status(bool): Whether or not the user has a seating 
        accommodation.
        
	    accommodation_type(str): The type of accommodation the user possesses.
     
	    service_class(str): The airplane class of the user. 
        It will be one of the three class, first class, business class, 
        and coach. It is represented as (F, B, C) respectively.
      
	    seat_preference(str): The user's preferred seat
    """
    
    def __init__(self, flight_seating, name, dob):
        """Current booking with Customer information

	    Args:
	        name(str): Name of user
	        dob(int): Date of birth of user
	        accommodation_status(bool): Whether or not the person has a seating 
            accommodation.
            
	        accommodation_type(str): What type of accommodation the user 
            possesses, must be one of these three senior, pregnant, disabled.
            
	        service_class(str): The service class section of the airplane where 
            the user will be seated.
            
	        seat_preference(str): The preference in the seat the user wants.
        """
        
        flight_seating = pd.read_csv("flight_seating.csv")
        self.flight_seating = flight_seating
        self.name = name
        self.dob = dob
        
    def age_filter(self, dob):
        
        # access the file path
        # reads the user inputted age (Format: "year/mm/dd")
        # uses regex to a determine whether a passenger is over the age of 14
        # If under the age of 14 "You cant fly alone"
        
        dob = self.dob
        #dob = input("what is your date of birth? Format: year")
        
        age_regex = re.search(r"^\d{4}", dob)
        
        year = int(age_regex.group(0))
        
        age = 2022 - year
        
        if age >= 14:
            print(f"The user is {age} years old, they are able to purchase a ticket")
            
        else:
            print(f"The user is {age} years old, they are too young to purchase a ticket")
        
# Patrick Polglase    
    def accommodation_filter(self):
        
        #access the filepath
        #read the user input of desired accommodation 
        #if accommodation is need, accomodation seats will be displayed to choose from, accommodation seats will cost less
        #if not, all seats will be displayed
        
        seat_data = self.flight_seating

        person_with_accommodation = input
        ("Enter TRUE or FALSE to if you need accommodations:")
        
        if person_with_accommodation == 'TRUE':
            seats = seat_data[["seat_id", "accommodation"]] 
            true_accommodation = seat_data[(seat_data["accommodation"] == True)]
            accommodated_seats = pd.merge(seats, true_accommodation[["seat_id", 
                                                "accommodation"]], how="right")
            print(accommodated_seats)
        else:
            all_seats = seat_data[["seat_id", "accommodation"]]
            print(all_seats)   
        
    def service_class_filter(self):
        
        #access the filepath
        #read the user input of desired service class
        #conditional will display available seats based on desired service class (F, B, C)
        #Help: Accommadation and pricing 
        #If budget input is 80 and the user needs an accommadation, the user cannot afford the ticket
        
        seat_data = self.flight_seating
        
        price_str = input("What's the most you're willing to spend on this\n"
                          "ticket?")
        price = int(price_str)
        
        if price < 69:
            print("There are no available seats within that price range")
            
        elif price < 100:
            priced_seats = seat_data[(seat_data['seat_prices'] <= price)]
            seats = seat_data[['seat_id', 'seat_prices', 'service_class ']]
            merged_seats = pd.merge(seats, priced_seats[['seat_id', 
                                'seat_prices', 'service_class ']], how='right')
            print("Here are seats within your budget.\n"
                  "You're only able to purchase coach")
            print(merged_seats)
            
        elif price < 360:
            priced_seats = seat_data[(seat_data['seat_prices'] <= price)]
            seats = seat_data[['seat_id', 'seat_prices', 'service_class ']]
            merged_seats = pd.merge(seats, priced_seats[['seat_id', 
                                'seat_prices', 'service_class ']], how='right')
            
            print("Here are seats within your budget.\n"
                  "You're able to purchase either coach or business")
            print(merged_seats)
            
        elif price < 1400:
            priced_seats = seat_data[(seat_data['seat_prices'] <= price)]
            seats = seat_data[['seat_id', 'seat_prices', 'service_class ']]
            merged_seats = pd.merge(seats, priced_seats[['seat_id', 
                                'seat_prices', 'service_class ']], how='right')
            
            print("Here are seats within your budget.\n"
                  "You're able to purchase coach, business, or first class")
            print(merged_seats)
            
        else:
            seats = seat_data[['seat_id', 'seat_prices', 'service_class']]
            print("Here are seats within your budget")
            print(seats)
            
        
            
    def seat_preference_filter(self):
        
        #access the filepath
        #read the user input of desired seat_preference
        #conditional will display available seats based on desired seat_preference (A, M, W)
<<<<<<< HEAD
        
        seat_data = self.flight_seating
=======
        seat_data = pd.read_csv("flight_seating.csv")
>>>>>>> 1082c37fe722c32df33a650d69564491aa330fc6
        preference = input("Would you like a middle, aisle, or window seat?\n"
                           "Middle(M), Aisle(A), Window(W). Aisle is reserved\n" 
                           "for accommodations and has a higher price point")
        if preference == "M":
            preferred_seats = seat_data[(seat_data["seat_preference"] == "M") & 
                                        (seat_data["seat_id"])]
            print(preferred_seats)
            print("Here are all the middle seats available")
        if preference == "A":
            preferred_seats = seat_data[(seat_data["seat_preference"] == "A") & 
                                        (seat_data["seat_id"])]
            print(preferred_seats)
            print("Here are all the Aisle seat available")
        if preference == "W":
            preferred_seats = seat_data[(seat_data["seat_preference"] == "W") & 
                                        (seat_data["seat_id"])]
            print(preferred_seats)
            print("Here are all the window seats available")
        
        
    def __repr__(self):
        #Show final seat the user selects based on criteria they inputted.
        # (Input values narrowed down)
        # 
        
    def main(flight_seating):
        """Merges the information from class person and class reservation

	    Args:
		    Filepath(str): path to the file
		    Available_seats(int): seats available
		    available _subcategory(str): class of seats available

	    Side Effects:
	    Merging of class person and class reservation
        """
        
        flight_seating = pd.read_csv("flight_seating.csv")
        
        seat_data = Passenger(flight_seating)
        filtered_age = seat_data.age_filter(input("what is your date of birth? Format: YYYYMMDD"))
        
        print(filtered_age, )
        
        
        
    def arg_parse(args):
        """Processes command line argument

        Args:
	        args(list of strings): command-line arguments
        """
