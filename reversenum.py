def reverse_digits(number):
    if number < 10:  # Base case: single-digit number
        return number
    else:
        last_digit = number % 10
        remaining_digits = number // 10
        reversed_remaining_digits = reverse_digits(remaining_digits)
        return int(str(last_digit) + str(reversed_remaining_digits))

def main():
    try:
        input_number = int(input("Enter a four-digit integer: "))
        if 1000 <= input_number <= 9999:
            reversed_number = reverse_digits(input_number)
            print("Reversed number:", reversed_number)
        else:
            print("Please enter a valid four-digit integer.")
    except ValueError:
        print("Invalid input. Please enter a valid four-digit integer.")

if __name__ == "__main__":
    main()
