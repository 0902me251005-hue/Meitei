humidity = float(input("Enter Relative Humidity (%): "))
temperature = float(input("Enter Temperature (°C): "))
ph = float(input("Enter pH: "))
salt = input("Salt Present? (Yes/No): ").lower()

score = 0

if humidity > 70:
    score += 1
if temperature > 35:
    score += 1
if ph < 5 or ph > 9:
    score += 1
if salt == "yes":
    score += 1

if score <= 1:
    print("Corrosion Risk: Low")
elif score <= 3:
    print("Corrosion Risk: Moderate")
else:
    print("Corrosion Risk: High")
