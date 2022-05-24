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

def ScrapeProjectInfo(fileName):
    informations = {
        '_Title': 'Your Project Name\n',
        '_Description': 'Project description\n<ul>\n\t<li>Feature 1</li>\n\t<li>Feature 2</li>\n\t<li>Feature 3</li>\n</ul>',
        'Requirements': '<ul>\n\t<li>Python 3.9.4</li>\n\t<li>Example-library 6.2.3</li>\n</ul>',
        'Installation': '<ol>\n\t<li>\n\t\tInstall required libraries\n\t\t<pre>pip install example-library\npip install next-example-library</pre>\n\t</li>\n\t<li>\n\t\tUnpack rar package\n\t\t<pre>unpack file.rar</pre>\n\t</li>\n</ol>',
    }
    with open('README_T.md', 'w') as file:
        file.write(f'# {informations["_Title"]}{informations["_Description"]}\n\n')
        for header in informations.keys():
            if (not header.startswith('_')):
                file.write(f'# {header}\n{informations[header]}\n\n')
        functions = ScrapeFunctions(fileName)
        file.write('# Functions\n<ul>\n')
        for function in functions:
            file.write(f'\t<li>\n\t\t<b>{function}</b> - function description\n\t\t<br>\n\t\t<ul>\n\t\t\t<li></li>\n\t\t</ul>\n\t\t<br>\n\t\t<pre>{function}\noutput</pre>\n\t</li>\n\n')
        file.write('</ul>')
        
ScrapeProjectInfo('readme_creator.py')