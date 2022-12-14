# Redline Airlines Airplane Bording Ticket and Reservation
### Team Red INST326 0101

## Purpose:

The purpose of our program is to let the user choose a desired Seat on our airline based on their desired inputted criteria. At the end of the program, the user will recieve a *'Boarding Ticket'* detailing each of their selections throughout the code.

## How to run our Program:
The program narrows down to a user's preferred seating choice by filtering through a series of questions.

The program first asks for the user's name.
The user then needs to input their their name.

The user then needs to enter their date of birth in the format: **YYYYMMDD.**
The program then uses a regular expression to determine the user's age.
In order to purchase a ticker, the user must be 14 years old or more, if they are not the program will stop

Next, the user will be asked will if they require accommodating seating.
The user will address this question as ```TRUE``` if they need accommodations or ```FALSE``` if they do not need accommodations.
If a user enters ```TRUE```, the accomodating seat's price will drop $30
If a user enters ```FALSE```, accomodating seats will still be shown as they are still available for everyone to purchase.
The program then prints out a table of all available seats based on the user's inputted criteria 

The folowing question the program asks is the desired destination that the user would like to fly to. The outgoing flights of the day are Morocco, France, Argentina and Croatia.
The user will then select their destination and will then be able to see a table of available seats based on all of their selected criteria.
Additionally, after a selection is made, a pie chart will pop up with all the outgoing flights for that day. The graph displays how many of each flights to each destination. After viewing this graph, the user **must close it to move further.**

The next question the program asks is if the user wants a direct flight or a connecting flight.
The user will then answer this by typing ```D``` for direct flight or ```C``` for connecting flight.

The next question asked will be service class which has options to travel in coach, business or first class.
The user addresses this question by answering ```C``` for coach, ```B``` business or ```F``` for first class.

The next question asked will be user's price preference which range from 50-1500.
Here the user picks their prefered price.

The next question program will ask is their seat preference with options of aisle, middle or window.
Here the user will type ```A``` for aisle seat, ```M``` for middle seat or ```W``` for window seat.

Once every user input decision has been made, every choice is compiled into a *'Boarding Ticket'*.

## Team Contributions:
### Tega Ojegun
Methods/Functions: **__init__() & boarding_ticket()**

Concepts: **Implementation of optional parameters & Implementation of sequence unpacking**

### Patrick Polglase
Methods/Functions: **custom_greeting() & seat_choice()**

Concepts: **Implementation of with statement & Implementation of an f string**

### Andrew Liu
Methods/Functions: **age_filter() & direct_flight_filter()**

Concepts: **Implementation of regular expression & Implementation of merge operation using Pandas dataframe**

### Hanna Teshome
Methods/Functions: **accomodation_filter() & price_filter()**

Concepts: **Implementation of a custom list sorting with a key function (lambda expression) & Implementation of a conditional expression**

### Meet Koradia
Methods/Functions: **destination_filter(), seat_preference_filter() & __str__()**

Concepts: **Implementation of data visualization using pyplot & Implementation of a magic method __str__()**
