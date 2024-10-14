# How can you make this more scalable and reusable later?
def find_armstrong_numbers(numbers):
    armstrong_list = []
    start = numbers[0]
    end = max(numbers) + 1
    revised_numbers = list(range(start, end))
    
    # Checking if numbers' length is 1.
    # If so, the function will just return the number.
    if len(numbers) == 1:
        return numbers
    else:
        for num in revised_numbers:
            exp_digit_sum = 0
            num_list = [int(digit) for digit in str(num)]
            exponent = len(num_list)
            for i in num_list:
                exp_digit_sum += i ** exponent
            if exp_digit_sum == num:
                armstrong_list.append(num)
            exp_digit_sum = 0
    return armstrong_list
        