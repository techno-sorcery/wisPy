# Website Interpreter, Static aka wisPy (not a backronym guys I swear)
# Hayden Buscher, 2023 - Version 1.0

import markdown
import configparser
import os

config = configparser.ConfigParser()
md = markdown.Markdown(extensions = ['meta'])
metaList = ['author', 'keywords', 'description', 'viewport']

# Main method
def main() -> None:
	params = configParse('wispy_config.ini')
	# Parse through folders specified in config
	for i in range(len(params)):
		pathIn = params[i][0]
		metadata = []

		for file in os.listdir(pathIn):
			if file.lower().endswith('.md'):
				pathOut = params[i][1] + os.path.splitext(file)[0] + '.html'

				# md to html conversion
				print(pathIn+file+' -> '+pathOut)
				metadata.append(mdConvert(pathIn+file,pathOut,params[i]))

# Parse config file
def configParse(path) -> list:
		config.read(path)
		paths = config.sections()
		params: list = []
		
		for i in paths:
			keyList = list(config[i].keys())
			tempParams = {'input': None, 'output': None, 'template': None, 'suffix': None}

			# Input value error checking
			if not 'input' in keyList or config[i]['input'] == '':
				print('Invalid input path for '+i+', aborting.')
				exit()

			for j in range(len(keyList)):
				index = keyList[j]
				# Set parameters
				if index in tempParams and not(config[i][keyList[j]] == ''):
					tempParams[index] = config[i][index]
					# Ensure paths end with /
					if not tempParams[index].endswith('/') and (index == 'input' or index == 'output' or index == 'tableOut'):
						tempParams[index] = tempParams[index]+'/'
					# Fill in home directory refrences
					if tempParams[index].startswith('~'):
						tempParams[index] = os.path.expanduser('~')+tempParams[index][1:]
			
			# Blank path checking
			if tempParams['output'] is None:
				tempParams['output'] = tempParams['input']

			# Generate list from dict
			myParams = []
			for i in tempParams.values():
				myParams.append(i)
			params.append(myParams)	
		return params

# Create .html file, apply template
def mdConvert(fileInPath, fileOutPath, params): # -> None:
	template = params[2]
	fileIn = open(fileInPath,'r').read()
	fileOut = open(fileOutPath,'w')
	parsedMeta = None

	# Checks if template is in use
	if not template is None:
		useTemplate = False
		
		# Writes template to file
		for line in open(template,'r').readlines():
			# Looks for <head>, and inserts metadata
			if '<head>' in line:
				fileOut.write(line)
				output = metaParse(fileIn, fileOut, params[3])
				fileIn = output[0]
				parsedMeta = output[1]
			# Looks for INSERT tag
			elif '<!--INSERT-->' in line:
				useTemplate = True
				fileOut.write(markdown.markdown(fileIn))
			else:
				fileOut.write(line)
				
		# Clears file if insert tag not found
		if not useTemplate:
			open(fileOutPath,'w').close()
			fileOut = open(fileOutPath,'w')
			fileOut.write(markdown.markdown(fileIn))
	else:
		fileOut.write(markdown.markdown(fileIn))
	return parsedMeta

# Convert and write metadata to file
def metaParse(fileIn, fileOut, suffix): # -> None:
	if suffix is None:
		suffix = ''
	html = md.convert(fileIn)
	if 'title' in md.Meta:
		fileOut.write('\t<title>'+md.Meta['title'][0]+suffix+'</title>\n')
	for i in metaList:
		if i in md.Meta:
			fileOut.write('\t<meta name=\"'+i+'\" content=\"'+md.Meta[i][0]+'\">\n')
	return (html,md.Meta)

if __name__ == "__main__":
    main()