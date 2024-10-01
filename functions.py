#functions - python 

# declare a function
# Key word def is used to declare a function
# name of the function is add
# () is used to pass the parameters
# : is used to start the function
# indentation is used to define the scope of the function
# return is used to return the value from the function

def range_sum():
    # solution one 
    nums  = range(1, 11)
    sum = 0

    for num in nums:
        sum += num
    
    # print(sum)

    # solution two
    # print(sum(range(1, 11)))

    # solution three
    # sum = 0
    # for i in range(1, 11):
    #     sum += i

    return sum

range_sum()

# check if the result is an even or odd number
def even_or_odd(number):
    result = number % 2
    print(f"{number} % 2 = {result}")  # Print the arithmetic operation
    if result == 0:
        return "Even"
    else:
        return "Odd"
    
print(even_or_odd())




def number_of_students():
    # solution one 

    # counting = 0
    # print("Enter the number of students. type stop when done." )

    # while True: 
    #     name = input("Enter the name of the student or stop to finish: ")
    #     if name == "stop":
    #         break
    #     counting += 1
    #     print(f" Total number of students is {counting}")

    #solution two
    # number_of_students = 10
    # additional_students = int(input("How many more students are in the class: "))

    # number_of_students += additional_students
    # print(f"Total number of students in the class is {number_of_students}")

    # solution three 
    # students = []

    # while True:
    #     student = input("Please enter student name or q to exit: ")
    #     if student == "q":
    #         break
    #     students.append(student)

    # print(f"\n The total number of students in the class is {len(students)}")

    # solution four
    # students = input("Enter the names of the students separated by commas: ")
    # students_list = students.split(",")
    # print(f"The total number of students in the class is {len(students_list)}")

    # solution five
    
    number_students = int(input("Whats the current number of students in the class: "))
    new_students = int(input("How many more students do you want to add (or subtract):"))
    number_students += new_students

    print(f"The total number of students in the class is {number_students}")

    
def sum_of_numbers():
    sjdhvbjhsdbvshd = "sdvsdvs"



