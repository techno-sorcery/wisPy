# Website Interpretor, Static aka wisPy (not a backronym guys I swear)
# Hayden Buscher, 2023

import markdown
import configparser
import os

config = configparser.ConfigParser()

# Main method
def main() -> None:
	params = configParse('wispy_config.ini')
	#mdConvert(open(pathIn,'r'),open(pathOut,'w'))

	for i in range(len(params)):
		pathIn = params[i][0]
		for file in os.listdir(pathIn):
			if file.lower().endswith('.md'):
				pathOut = params[i][1] + os.path.splitext(file)[0] + '.html'

				print(pathIn+file+' -> '+pathOut)
				mdConvert(open(pathIn+file,'r'),open(pathOut,'w'))
		

# Parse configuration file
def configParse(path) -> list:
		config.read(path)
		paths = config.sections()
		params: list = []

		for i in paths:
			keyList = list(config[i].keys())

			# Input value error checking
			if not 'input' in keyList or config[i]['input'] == '':
				print('Invalid input path for '+i+', aborting.')
				exit()
			
			pathIn = config[i]['input']
			pathOut: str = ''
			template: str = None

			# Check if 'output' exists
			if 'output' in keyList and not(config[i]['output'] == ''):
				pathOut = config[i]['output']
			else:
				pathOut = pathIn

			# Check if 'template' exists
			if 'template' in keyList:
				template = config[i]['template']
				if template == '':
					template = None

			# Ensure paths end with /
			if not pathIn.endswith('/'):
				pathIn = pathIn+'/'
			if not pathOut.endswith('/'):
				pathOut = pathOut+'/'

			params.append((pathIn, pathOut, template))
		return params

# Convert individual .md file to .html
def mdConvert(fileIn, fileOut) -> None:
	thisIn = fileIn.readlines()
	for line in thisIn:
		thisLine = markdown.markdown(line)
		fileOut.write(thisLine+'\n')

if __name__ == "__main__":
    main()