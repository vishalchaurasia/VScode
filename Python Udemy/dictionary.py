#keys and values pair
thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

print(thisdict["year"])

a = {"brand": "Ford","model": "Mustang","year": 1964,"colour":"black"}
print(a.keys())
print(a.values())

for k in a.keys():
    print(k)
for k in a.values():
    print(k)


internet_celebrities = {"DrDisrespect": "YouTube", "ZLaner": "Facebook", "Ninja": "Mixer"}
another_one = {"shroud": "Twitch"}
internet_celebrities.update(another_one)  
gamers = internet_celebrities.copy()  
internet_celebrities.clear()  
print(internet_celebrities)  
print(gamers)  

computers = {"google": "chromebook", "apple": "mac", "microsoft": "surface pro"}
if "lenevo" not in computers:
    computers["lenevo"]="thinkpad"
print(computers)