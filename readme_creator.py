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
    informations = {
        '_Title': 'Your Project Name\n',
        '_Description': 'Project description\n<ul>\n<li>Feature 1</li>\n<li>Feature 2</li>\n<li>Feature 3</li>\n</ul>',
        'Requirements': '<pre>pip install example-library\npip install example-library</pre>',
        'Installation': '<ul>\n<li>Install required libraries</li>\n<li>Unpack rar</li>\n</ul>',
        'Versions': '<ul>\n<li>Python 3.9.4</li>\n<li>Example-library 6.2.3</li>\n</ul>',
    }
    with open('documentation_raw.txt', 'w') as file:
        file.write(f'# {informations["_Title"]}{informations["_Description"]}\n\n')
        for header in informations.keys():
            if (not header.startswith('_')):
                file.write(f'# {header}\n{informations[header]}\n\n')
        
ScrapeProjectInfo()