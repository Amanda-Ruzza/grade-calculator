
print("Hello, I am your 'Grade Calculator Assistant'\nI will help you calculate your 5 test scores, one by one\n")

class ScoreRangeException(Exception):
    '''Raised when the input value is correct'''
    pass 


test_scores_processing = []
grade_f = "F"
grade_d = "D"
grade_c = "C"
grade_b = "B"
grade_a = "A"

def calculator():
    test_scores_input = int(input("Please enter the test result score:\n"))
    # if isnum(test_scores_input) == False
    #     raise ValueError :
    #     print("I can only process numbers, please try again")
    # else:
    #     continue    
    try:
        if test_scores_input <= 100 or  0:
            test_scores_processing = [test_scores_input]
        # if test_scores_input.isdigit(): 
            grade_result = [grade_f if num < 61 else grade_d if num < 70 else grade_c if num < 80 else grade_b if num < 90 else grade_a if num < 101 else None for num in test_scores_processing ]    
            print(f"The grade is {grade_result}")
            print(f"This is the test score processing list: {test_scores_processing}")
                       
        elif test_scores_input > 100:
            raise ValueError(f"I can only process numbers from '0 - 100'. {test_scores_input} is greater than 100!")
        elif test_scores_input < 0:
            raise ValueError(f"I can only process numbers from '0 - 100'. {test_scores_input} is a negative number!")
        else:
            print("testing")
            # raise ValueError  
            # print(f)
            
        
    except ValueError:
        
            print("I can only process numbers, please try again")

calculator()
calculator()
added_scores = test_scores_processing.append(test_scores_processing)
print(f"This is the added scores list: {added_scores}") 
calculator()
added_scores = test_scores_processing.append(test_scores_processing)
print(f"This is the added scores list: {added_scores}") 
calculator()
added_scores = test_scores_processing.append(test_scores_processing)
print(f"This is the added scores list: {added_scores}") 
calculator()
added_scores = test_scores_processing.append(test_scores_processing)
print(f"This is the added scores list: {added_scores}") 

# calculate the sum of added_scores
# calculate the average of all those scores, compare them to the grades items and print the average grade result

print("The average grade of the 5 grades is: \n")
print("This processing job is concluded, goodbye!\n")

exit()
        
