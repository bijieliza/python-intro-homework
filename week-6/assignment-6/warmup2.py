
def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9
for c in [0, 100]:
   f=celsius_to_fahrenheit(c)
   print(f"{c}°C = {f:.1f}°F")

f=72
c=fahrenheit_to_celsius(f)
print(f"{f}°F = {c:.1f}°C")

