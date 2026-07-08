plastics = {
    1: ("PET", "Water bottles", "Highly Recyclable", "Do not reuse many times"),
    2: ("HDPE", "Milk containers", "Highly Recyclable", "Safe and durable"),
    3: ("PVC", "Pipes", "Difficult to Recycle", "May release harmful chemicals"),
    4: ("LDPE", "Plastic bags", "Limited Recycling", "Reduce usage"),
    5: ("PP", "Food containers", "Recyclable", "Widely used"),
    6: ("PS", "Disposable cups", "Rarely Recycled", "Avoid excessive use"),
    7: ("Others", "Mixed plastics", "Generally Not Recyclable", "Dispose carefully")
}

code = int(input("Enter Recycling Code (1-7): "))

if code in plastics:
    name, product, recycle, remark = plastics[code]
    print("\nPlastic Information")
    print("Polymer Name:", name)
    print("Common Products:", product)
    print("Recyclability:", recycle)
    print("Environmental Remarks:", remark)
else:
    print("Invalid recycling code!")
