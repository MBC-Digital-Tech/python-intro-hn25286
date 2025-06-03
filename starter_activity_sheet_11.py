# program to check answers from user

def get_answer():
    # Declare a variables to hold input
    num = 1
    ans = ""
    
    while True:
        try:
            # Get input from the user
            ans = input("Please enter a number between 1 and 10: ")
            
            # cast the input to an integer
            num = int(ans)
            
            # Check if the number is within the valid range
            if 1 <= num <= 10:
                break
            else:
                print("Number out of range. Try again.")
        except ValueError:
            print("That's not a valid number. Please try again.")
            continue
        
    print(f"You entered a valid number: {num}")
        
        
def check_answer(answer):
    is_correct = False
    
    try:
        # Check if a number has been entered.
        num = int(answer)
        
        # Check the number is between 1 and 10
        if num > 0 and num < 11:
            return True # The number is between 1 and 10
        
    except ValueError:
        # answer is a non numeric char string
        pass
    
    # The answer is not numeric or out of the valid range    
    return False
