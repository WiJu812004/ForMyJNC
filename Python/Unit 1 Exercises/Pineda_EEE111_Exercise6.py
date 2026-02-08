input_line = input("Enter numbers separated by spaces: ")
string_numbers = input_line.split()
numbers = [int(num) for num in string_numbers]
total = sum(numbers)
average = total / len(numbers) if numbers else 0
print("Sum =", total)
print("Average =", average)
print()

color_codes = {
    "black": 0, "brown": 1, "red": 2, "orange": 3,
    "yellow": 4, "green": 5, "blue": 6, "violet": 7,
    "gray": 8, "white": 9
}
multipliers = {
    "black": 1, "brown": 10, "red": 100, "orange": 1_000,
    "yellow": 10_000, "green": 100_000, "blue": 1_000_000,
    "violet": 10_000_000, "gray": 100_000_000, "white": 1_000_000_000,
    "gold": 0.1, "silver": 0.01
}
tolerances = {
    "brown": "+/- 1%", "red": "+/- 2%", "green": "+/- 0.5%", "blue": "±+/- 0.25%",
    "violet": "+/- 0.1%", "gray": "+/- 0.05%", "gold": "+/- 5%", "silver": "+/- 10%"
}

colors = input("Enter four resistor colors separated with spaces: ").lower().split()

if len(colors) != 4:
    print("Please enter exactly four colors.")
else:
    try:
        digit1 = color_codes[colors[0]]
        digit2 = color_codes[colors[1]]
        multiplier = multipliers[colors[2]]
        tolerance = tolerances.get(colors[3], "+/- 20%")

        resistance = (digit1 * 10 + digit2) * multiplier

        print(f"Resistance: {resistance} {tolerance}")
    except KeyError:
        print("Invalid color entered. Please check your input.")