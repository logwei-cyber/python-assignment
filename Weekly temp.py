temperatures = []

print("Enter temperatures for the week:")

for day in range(7):
    temp = float(input(f"Enter temperature for day {day + 1}: "))
    temperatures.append(temp)

lowest_temp = min(temperatures)
highest_temp = max(temperatures)
sum_temp = sum(temperatures)
avg_temp = sum_temp / len(temperatures)

print("\nTemperature Summary:")
print(f"Lowest Temperature: {lowest_temp}")
print(f"Highest Temperature: {highest_temp}")
print(f"Sum of Temperatures: {sum_temp}")
print(f"Average Temperature: {avg_temp:.2f}")
