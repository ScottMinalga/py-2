# s = "helloworld123"
#
# print(s.isalpha())
#
# example = {
#     "p":1,
#     "a":1,
#     "s":2,
#     "w":1,
#     "o":1,
#     "r":1,
#     "d":1,
# }
#
# fWait = 100
#
# planet_factors = {
#     "Mercury": 0.38,
#     "Venus": 0.91,
#     "Moon": 0.165,
#     "Mars": 0.38,
#     "Jupiter": 2.34,
#     "Saturn": 0.93,
#     "Uranus": 0.92,
#     "Neptune": 1.12,
#     "Pluto": 0.066
# }
#
# for sPlanet, fFactors in planet_factors.items():
#     print(f"{sPlanet:15s}\t{fWait * fFactors:10.2f}")
#
#
# for planet in planet_factors:
#     print(f"{planet:15s}\t{fWait * planet_factors[planet]:10.2f}")
#
# list = ["Hello","World"]
# string = "HELLO EVERYONE"
# string2 = "       HELLO EVERYONE            "
# string3 = "ABC123"
# print(len(string))
# print(string.lower())
# print(string.capitalize())
# print(string.title())
# print(string2.strip())
# print(string.find("EVERYONE"))
# print(string.replace("HELLO","WELCOME"))
# print(string.split(" "))
# print(" ".join(list))
# print(string3.isdigit())
# print(string3.isalpha())
# print(string.isalnum())


iAge = 21
# print("Legal") and (vaild = True) if iAge >= 21 else print("Not legal")

valid = True if iAge >= 21 else False; print("Legal" if valid else "Not legal")
print(valid)



sInitials = sName[0] + sName[sName.find(" ") + 1]


