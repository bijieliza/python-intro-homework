def ctof(c):
   f= (c * 9/5) + 32
   print(f"{c}°C = {f}°F")
ctof(100)
ctof(0)
def ftoc(f):
   c= (f - 32) * 5/9
   print(f"{f}°F = {c:.1f}°C")
ftoc(72)

