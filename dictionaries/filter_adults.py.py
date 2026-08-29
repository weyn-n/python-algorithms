users = {
    "Alex": 20,
    "John": 17,
    "Maria": 22,
    "Bob": 15,
    "Kate": 19,
    "Mike": 16
}

adults = {}

for name, age in users.items():
    
    if age >= 18:
        adults[name] = age
        
print(adults)