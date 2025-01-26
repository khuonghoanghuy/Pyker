import json

def initData():
    saveData({
        'score': 0
    })

def saveData(data, filename='savefile.json'):
    with open(filename, 'w') as f:
        json.dump(data, f)

def loadData(filename='savefile.json'):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return initData()
    
def resetData(filename='savefile.json'):
    saveData({}, filename)
    return initData()