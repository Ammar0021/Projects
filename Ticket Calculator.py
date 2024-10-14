#Ticket Prices: Cineworld

import math

def calculate_ticket_cost():
    
    day = input("What day is it? ").strip().lower()

    
    if day == "tuesday":
       
        total_tickets = int(input("How many total tickets (adults, children, students, seniors, families combined)? "))
        total_cost = total_tickets * 5.40
        print(f"Total cost for tickets on Tuesday: £{total_cost:.2f}")
        return

    
    time = input("Is it before 5pm or after 5pm? (before/after) ").strip().lower()

    
    if time == "before":
        adult_price = 7.40
        child_price = 5.40
        student_price = 5.90
        senior_price = 5.90
        family_price = 22.60
    else:
        adult_price = 8.90
        child_price = 6.40
        student_price = 6.90
        senior_price = 6.90
        family_price = 27.60


    adult_tickets = int(input("How many adult tickets? "))
    child_tickets = int(input("How many children tickets? "))
    student_tickets = int(input("How many student tickets? "))
    senior_tickets = int(input("How many senior tickets? "))
    family_tickets = int(input("How many family tickets? "))

    
    total_cost = (adult_tickets * adult_price) + \
                 (child_tickets * child_price) + \
                 (student_tickets * student_price) + \
                 (senior_tickets * senior_price) + \
                 (family_tickets * family_price)

    # Output total cost
    print(f"Total cost for tickets: £{total_cost:.2f}")

# Call the function to calculate ticket cost
calculate_ticket_cost()

