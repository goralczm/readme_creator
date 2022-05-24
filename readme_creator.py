import re

def ScrapeFunctions(fileName):
    functions = {}
    with open(fileName, 'r') as file:
        content = file.readlines()
        for line in content:
            line = line.strip() #cleared white spaces
            functionMatch = re.findall("def .*:", line) #EXAMPLE RETURN ['def Multiply(x, y):']
            if (len(functionMatch) > 0): #if there is a match
                functionClearedStr = functionMatch[0][4:-1] #gets rid of 'def' keyword and a colon
                variables = re.findall("\(.*\)", functionClearedStr)[0][1:-1] #cleared the first match of given pattern from brackets
                variablesCleared = re.split(',', variables)
                variablesCleared = [variable.strip() for variable in variablesCleared] #cleared white spaces
                functions[functionClearedStr] = variablesCleared
    return functions

def ScrapeProjectInfo():
    projectInfos = {}
    with open('documentation_raw.txt', 'r') as file:
        content = file.readlines()
        currentHeader = '' 
        for line in content:
            if (line.startswith('---')):
                currentHeader = line.strip()[4:-4].capitalize() #cleaned '---' and capitalized strings
                projectInfos[currentHeader] = []
            else:
                if (line.startswith('/t')):
                    print(line)
    return projectInfos

print(ScrapeProjectInfo())
exit()

informations = { #Key names starting with '_' are automatically set
    'Title': '',
    'BulletDescription': '',
    'Requirements': '',
    'InstallationSteps': '',
    'PythonVersion': '',
    '_Functions': {},
}

scriptName = input("What's the name of script to scrape functions from? ")
informations['_Functions'] = ScrapeFunctions(scriptName)

for info in informations.keys():
    if ('_' not in info):
        informations[info] = input(f'{info}: ')