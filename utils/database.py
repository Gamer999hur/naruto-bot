import json



def LoadDadosFrom(ArqJson: str):
    with open(ArqJson, "r") as f:
        return json.load(f)
    
def WriteDadosIn(ArqJson: str, value):
    with open(ArqJson, "w") as f:
        return json.dump(value, f, indent=4)