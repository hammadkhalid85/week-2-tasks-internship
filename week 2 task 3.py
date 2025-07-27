var1 = "Hello"     # string
var2 = 25          # integer
var3 = 3.14        # float
var4 = True        # boolean
var5 = 2 + 3j      # complex

variables = [var1, var2, var3, var4, var5]

print("\nOriginal Values and Types:")
for v in variables:
    print(f"Value: {v}, Type: {type(v)}")

print("\nAfter Conversions:")
try:
    print(int(var3))      # converting float to int
except Exception as e:
    print("Cannot convert:", e)

try:
    print(str(var5))      # complex to string
except Exception as e:
    print("Cannot convert:", e)


