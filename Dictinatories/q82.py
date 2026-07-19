"""
Create a Dicitionary mapping five countries  to theie captial cities, iterate to the
dictioanry using items() method. And print each pair in this format Country -->captial
"""

Country = {
    "India": "Delhi",
    "USA": "Washington",
    "Japan": "Tokyo",
    "France": "Paris",
    "Australia": "Canberra",
}

for country,captail in Country.items():
    print(f"{country} --> {captail}")