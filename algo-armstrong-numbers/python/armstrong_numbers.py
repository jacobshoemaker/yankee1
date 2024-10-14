# How can you make this more scalable and reusable later?
def find_armstrong_numbers(numbers):
    # Create an empty list named armstrong_list that will contain all armstrong numbers within a given range
    armstrong_list = []
    # Creating a start variable and end variable that are values the first and last elements of the numbers list.
    start = numbers[0]
    end = max(numbers) + 1
    # Creating a revised list of the input list to be inclusive of the last element of the input list.
    revised_numbers = list(range(start, end))
    
    # Checking if numbers' length is 1.
    # If so, the function will just return the number.
    if len(numbers) == 1:
        return numbers
    # If the length of the numbers input is greater than 1, execute following logic.
    else:
        # Iterating through the list revised_numbers
        for num in revised_numbers:
            # Creating a sum variable that holds the value of the current number's sum of exponential digits.
            exp_digit_sum = 0
            # Creating a list of the digits of each number in revised_numbers using list comprehension
            num_list = [int(digit) for digit in str(num)]
            # Creating an exponent variable based on the length of num_list
            exponent = len(num_list)
            # Iterating through num_list to calculate a running total for the sum of exponential digits.
            for i in num_list:
                exp_digit_sum += i ** exponent
            # Checking if the exponential digit sum is equal to the current number in revised_numbers.
            # If so, we append that number to armstrong_list
            if exp_digit_sum == num:
                armstrong_list.append(num)
            # Resetting exp_digit_sum back to zero for the next iteration.
            exp_digit_sum = 0
    return armstrong_list
        