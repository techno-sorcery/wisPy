# Website Interpreter, Static aka wisPy (not a backronym guys I swear)
# Hayden Buscher, 2023

import markdown
import configparser
import os

config = configparser.ConfigParser()

# Main method
def main() -> None:
	params = configParse('wispy_config.ini')

	for i in range(len(params)):
		pathIn = params[i][0]
		for file in os.listdir(pathIn):
			if file.lower().endswith('.md'):
				pathOut = params[i][1] + os.path.splitext(file)[0] + '.html'

				print(pathIn+file+' -> '+pathOut)
				mdConvert(open(pathIn+file,'r'),pathOut,params[i][2])	

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

# Create .html file, handle template
def mdConvert(fileIn, fileOutPath, template) -> None:
	fileOut = open(fileOutPath,'w')

	# Checks if template is in use
	if not template is None:
		useTemplate = False
		
		# Writes template to file
		for line in open(template,'r').readlines():
			# Looks for <head>, and inserts metadata
			if '<head>' in line:
				fileOut.write(line)
				metaParse(fileIn, fileOut)
			# Looks for INSERT tag
			elif '<!--INSERT-->' in line:
				useTemplate = True
				markParse(fileIn, fileOut)
			else:
				fileOut.write(line)
				
		# Clears file if insert tag not found
		if not useTemplate:
			open(fileOutPath,'w').close()
			fileOut = open(fileOutPath,'w')
			markParse(fileIn, fileOut)
	else:
		markParse(fileIn, fileOut)

# Convert and write markdown text to file
def markParse(fileIn, fileOut) -> None:
	head = True
	write = True
	for line in fileIn.readlines():
		if '---' in line and head:
			write = False
		elif '---' in line and not head:
			write = True
		elif write:
			thisLine = markdown.markdown(line)
			fileOut.write(thisLine+'\n')
		head = False

# Convert and write metadata to file
def metaParse(fileIn, fileOut) -> None:
	head = True
	for line in fileIn.readlines():
		line = line.strip()
		if (not('---' in line)and head) or ('---' in line and not head):
			break
		# title
		elif 'title: ' in line:
			print('<title>'+line[7:]+'</title>'+'\n')
			fileOut.write('<title>'+line[7:]+'</title>'+'\n')
		head = False


if __name__ == "__main__":
    main()