import pandas as pd
import re

class Reservations:
    """Declaration of a class that identifies seats that can be reserved within its sub categories: coach, business, first class

    Attributes:
        Seats (int):  number of seats available
        coach(str): Coach class on the plane
        business(str): Business class on the plane
        first_class(str): First class on the plane
    """
    
    def __init__(self, seats, coach, business, first_class):
    
        """Initializes a seat object

	    Args:
            Seats (int):  number of seats available
		    coach(str): Coach class on the plane
		    business(str): Business class on the plane
		    first_class(str): First class on the plane
	
	    Side Effects:
	        Ctreates and sets the attributes of the Reservations class
        """
        
    def available_subcatogory(self, seats):
        
        """Creates a list of available seats within all the categories

	    Args:
		    seats(int): number of seats available 

	    Side Effects:
		    Creates an updated list of seats within different categories
        """
        
    def reserve_seat(self, seats, users):
        """Append users to the available empty list of seats
        
        Args:
            Seats(int): Number of available seats
		    Users(str): Users that will be appended to the empty seats

        Side effects:
	        Appends to a list of available seats
        """
        
    def accommodate(self, accomodation_type):
	    """Determines whether the customer is disable, pregnant or a senior citizen. Uses a regex to determine how old a user is and whether they are eligible for senior citizen status.

	    Args:
		    Accommodation_status(boolean): States whether a user has an accommodation or not 
		    Accommodation_type(str): The type of accommodation a user possesses

	    Side Effects:
	    Sets self to a specific accomodation_status
        """
        
    def finalized_booking(dataframe1, dataframe2):
        """Pulls existing booking from the person class, and uses pandas to concatenate it to booking being upgraded. Can be used by the main function to finalize booking 
        
        Args:
	        Dataframe1 (dataframe): passenger chart
	        Dataframe2 (dataframe): table of seats available 

        Side Effects:
	        Concatenates both data frames together
        """
        


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
    
    def __init__(self, name, dob, accommodation_status, service_class, seat_preference):
        """Current booking with Customer information

	    Args:
	        name(str): Name of user
	        dob(int): Date of birth of user
	        accommodation_status(bool): Whether or not the person has a seating accommodation
	        accommodation_type(str): What type of accommodation the user possesses, must be one of these three senior, pregnant, disabled.
	        service_class(str): The service class section of the airplane where the user will be seated.
	        seat_preference(str): The preference in the seat the user wants
        """

    def Flight_Booking(filepath):
        """reads a data file and place it into a dataframe
    
        Args:
        filepath(str): file path to the data
    
        Side effect:
        Reads data file and appends it to a dataframe"""

    def seat_filter(self, seats):
        """Uses pandas to filter a table of seats
        
        Args:
            seats(int): number of seats available
	
	    Side Effects: 
        Sets a new filtered table of seats
        """
        
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
