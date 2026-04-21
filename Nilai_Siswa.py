print("=== STUDENT GRADING PROGRAM ===")
print("\033[0;35;40m Type 'DONE' to exit. \033[0m")

total = 0
passed = 0
failed = 0

grade_list = []

while True:
    user_input = input("Enter Grade : ".lower().strip())
    if user_input == "done":
        break

    try:
        # We change the comma to a period BEFORE converting to float
        cleaned_input = user_input.replace(",",".")
        grade = float(cleaned_input)

        if grade <0 or grade >100:
            print("Invalid input. Rage 0 - 100")
        else:
            total +=1
            grade_list.append(grade)

            if grade >= 75:
                print("\033[1;94;100m PASSED \033[0m")
                passed +=1
            else:
                print("\033[2;91;40m FAILED \033[0m")
                failed +=1

    except ValueError:
        print("Input must be a number or type 'exit' to quit!")

# Checking if grade_list is empty to avoid error ZeroDivisionError
if total > 0:
    print("\n === RESULT ===")
    print("Total Grades Entered : ", total)
    print("Passed : ", passed)
    print("Failed : ", failed)
    print("Grade List : ", grade_list)
    print("Highest Grade : ",max(grade_list))
    print("Lowest Grade : ",min(grade_list))
    print("Average : ", sum(grade_list) / len(grade_list))
else:
    print("\n No data entered.")