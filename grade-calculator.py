import sys

print("Hello, I am your 'Grade Calculator Assistant'\nI will help you calculate your 5 test scores, one by one\n")

test_scores_processing = []

        
def calculate_grade():
    added_scores = [] 

    for i in range(5):

        print(f"Test score number:  {i+1}\n")
    
        try:
            test_scores_input = int(input("Enter the test result score:\n"))   
            if test_scores_input <= 100 or  0:
                added_scores.append(test_scores_input)
                     
            elif test_scores_input > 100:
                raise ValueError(f"I can only process numbers from '0 - 100'. {test_scores_input} is greater than 100!")
            elif test_scores_input < 0:
                raise ValueError(f"I can only process numbers from '0 - 100'. {test_scores_input} is a negative number!")
                                    
        except ValueError as e:
            print(e.args)
            print("I can only process numbers, please try again\n")
            sys.exit("Program exiting\n")
        else:
            print("\nI'm ready to acept the next score\n")
    average_grade = sum(added_scores) / len(added_scores)
    grade_result = ["F" if num < 61 else "D" if num < 70 
                                else "C" if num < 80 else "B" if num < 90 
                                else "A" if num < 101 else None 
                                for num in [average_grade] ]    
    print(f"The grade for all the five test scores combined is {grade_result}, which equals to {average_grade}.\n")

calculate_grade()


sys.exit("This processing job is concluded, goodbye!\n")
        
