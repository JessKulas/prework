# question 1 
def hello_name(name):
    username = "hello USERNAME"
    print("hello_"+user_name)
user_name = input('Hello USERNAME ')
hello_name(user_name)


# question 2 def first_odd():
for i in range(1,100):
    if i % 2 != 0:
        print(i)


# question 3
def max_num_in_list(a_list):
    maximum - a_list[0]
    for i in range(len(a_list)):
        if a_list[i] > maximum:
            maximum = a_list[i]
    return maximum
a_list = [10, 20, 30, 40, 50]
print(max_num_in_list(a_list))


# question 4
def is_leap_year(a_year):
    # checking if the year is divible by 400
    if(a_year % 400 == 0):
        return True
    # Checking if the year is divisible 100. If it is divisible then it is
    # Not a leap year
    elif a_year % 100 == 0:
        return False
    # Checking if the year is divisible by 4.
    elif a_year%4 == 0:
        return True
    # Otherwise False
    else:
        return False
# Asking the user to enter year
a_year = int(input(2022))
# Calling function is_leap_year
print(is_leap_year(a_year))


# question 5
def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))
# Driver Code
a_list = [2,3,4,5,6,7]
print(is_consecutive(a_list))