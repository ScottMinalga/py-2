#Joseph Picard
#Inter Planetary Weights Using Dictionaries and Pickling
#CIT-117
import pickle

def main():
    #Dictionary of planet names and conversion factors
    dPlanets = {
        "Mercury": 0.38,
        "Venus": 0.91,
        "our Moon": 0.165,
        "Mars": 0.38,
        "Jupiter": 2.34,
        "Saturn": 0.93,
        "Uranus": 0.92,
        "Neptune": 1.12,
        "Pluto": 0.066
    }

    #Open Pickling file that stores previous if it exists
    dPlanetHistory = {} #Declaring empty dictionary
    eof = False
    try:
        input_file = open("jpPlanetaryWeights.db", "rb")
        #If execution reaches here load key/values
        while not eof:
            try:
                dPlanetHistory = pickle.load(input_file)
            except EOFError:
                eof = True
        input_file.close()
    except FileNotFoundError:
        pass #If file is not present skip loading of the dictionary

    #Asking user if they would like to see the history y/n
    if input("Would you like to see the history y/n: ").lower() == "y":
        if dPlanetHistory:
            for name, data in dPlanetHistory.items():
                print(f"{name}, here are your weights on our Solar System's Planets")
                for planet, weight in data.items():
                    print(f'Weight on {planet:20s}: {weight:10.2f}')
        else:
            print('No history found')
    #Code a loop that prompts user for unique name, prompts earth weight,
    while True:
        sName = input("Enter a unique name (press enter to exit): ") #Prompting for unique name
        if not sName:
            break
        if sName in dPlanetHistory: #Checking if name is in history
            print(f"{sName} already exists. Please enter a unique name.")
            continue
        while True:
            try:
                fWeight = float(input("Enter Weight on Earth: ")) #Prompting for earth weight
                break
            except ValueError:
                print("Invalid weight. Please enter a number.")

        dictPersonWeights = {}
        for planet, weight in dPlanets.items():
            fPlanetWeight = fWeight * weight
            dictPersonWeights[planet] = fPlanetWeight
            print(f"Weight on {planet:20s}: {fPlanetWeight:10.2f}")

        dPlanetHistory[sName] = dictPersonWeights #Adding persons name and dictPersonWeights to history dictionary
        print(dPlanetHistory)
    #saving output
    output_file = open("jpPlanetaryWeights.db", 'wb')
    pickle.dump(dPlanetHistory, output_file)
    output_file.close()
main()