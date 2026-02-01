import math


num = int(input("Enter a number: "))

sqrt_value = math.sqrt(num)
log_value = math.log(num)      # Natural log (base e)
sin_value = math.sin(num)      # Sine in radians

print(f"Square root of", num, "is:", sqrt_value)
print(f"Natural logarithm of", num, "is:", log_value)
print(f"Sine of", num, "is:", sin_value)
