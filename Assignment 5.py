elements = {
    "Na": {"Atomic Number": 11, "Atomic Mass": 22.99, "Group": 1, "Period": 3,
           "Electronic Configuration": "2,8,1", "Oxidation State": "+1",
           "Application": "Street lighting"},
    "Fe": {"Atomic Number": 26, "Atomic Mass": 55.85, "Group": 8, "Period": 4,
           "Electronic Configuration": "2,8,14,2", "Oxidation State": "+2, +3",
           "Application": "Construction"},
    "Cl": {"Atomic Number": 17, "Atomic Mass": 35.45, "Group": 17, "Period": 3,
           "Electronic Configuration": "2,8,7", "Oxidation State": "-1",
           "Application": "Water purification"},
    "Cu": {"Atomic Number": 29, "Atomic Mass": 63.55, "Group": 11, "Period": 4,
           "Electronic Configuration": "2,8,18,1", "Oxidation State": "+1, +2",
           "Application": "Electrical wiring"}
}

symbol = input("Enter element symbol (Na, Fe, Cl, Cu): ")

if symbol in elements:
    print("\nElement Information:")
    for key, value in elements[symbol].items():
        print(f"{key}: {value}")
else:
    print("Element not found!")
