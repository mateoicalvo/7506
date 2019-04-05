import json
def main():
    
    with open("desc.json") as json_file:
        data = json.load(json_file)
        
    for dataframe, columnas in data.items():
        for columna, campos in columnas.items():
            print("{},{},{},{}".format(dataframe, columna, campos["desc"], \
                campos["transformation"]))

main()
