# creates a dictionary filled with Roman numeral values
roman_values = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

def romantoint(roman_numeral):
    # Initialize total and the value of the previous numeral (in the reversed order)
    total_value = 0
    previous = 0

    # Loop through each Roman numeral character in reverse (right to left)
    for i in reversed(roman_numeral):
        # Get the numerical value of the current Roman numeral
        value = roman_values[i]

        # If the current value is less than the previous value, subtract it (e.g., IV => 1 < 5)
        if value < previous:
            total_value -= value
        else:
            # Otherwise, add it (e.g., VI => 5 <= 1, so add 5 and 1)
            total_value += value
        
        # Update 'previous' to the current value for the next loop iteration
        previous = value

    # Print the final integer value of the Roman numeral
    print(total_value)

