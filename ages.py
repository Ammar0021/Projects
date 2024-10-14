import math

def get_ages():
    
    ages = []
    
    for i in range(5):
        
        while True:
            
            try:
                
                age = int(input(f"Enter the age of student {i+1} (between 7 and 13): "))
                
                if age >= 7:
                    if age <= 13:
       

                        ages.append(age)
                    
                    break
                
                else:
                    print("Please enter an age between 7 and 13.")
                    
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    return ages

def calculate_age_difference(ages):
    
    total_sum = sum(ages)
    age_diff = max(ages) - min(ages)
    return total_sum, age_diff

# Main program
ages = get_ages()
total_sum, age_diff = calculate_age_difference(ages)

print(f"\nThe ages entered are: {ages}")
print(f"The sum of the ages is: {total_sum}")
print(f"The difference between the oldest and youngest student is: {age_diff}")
