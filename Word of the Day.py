#import ui, appex
import requests

#Url to to the word of the day website
url = "https://www.merriam-webster.com/word-of-the-day"

#Function to return the word of day and application
#(Returns number of lines for IPhone Application)
def getWordOfDay(url):
	word = ""
	
	#Gets html text from website
	html = requests.get(url).text
	
	#Finds the word of the day in html text
	word = html[html.find("Word of the Day:"): html.find("Word of the Day:")+ 40]
	word = word[0:word.find("|")]
	
	#Finds definition in html file
	definition = html[html.find("<h2>Definition</h2>")+12:html.find("<h2>Definition</h2>") + 2000]
	definition = definition[definition.find("</strong>")+9:definition.find("</p>")]
	
	#Removes html links from text
	while(definition.find("<a href") != -1):
		definition = definition[0: definition.find("<a href")] + definition[definition.find('">')+2: len(definition)]
		definition = definition[0:definition.find("</a>")] + definition[definition.find("</a>")+4:len(definition)]

	#Removes html strong
	while(definition.find("<strong>") != -1):
		definition = definition[0: definition.find("<strong>")] + definition[definition.find('<strong>')+8: len(definition)]
		definition = definition[0:definition.find("</strong>")] + definition[definition.find("</strong>")+9:len(definition)]

	
	#Formats definition into multiple lines	
	characters = 0
	multiDefinition = ""
	numberOfLines = 2
	
	for words in definition.split(" "):
		characters += len(words)
		
		if(characters > 35):
			characters = 0
			multiDefinition += "\n\t"
			numberOfLines = numberOfLines + 1
		
		multiDefinition += words + " "
		
	return (word + "\n\t" + multiDefinition, numberOfLines)
	
	
wordOfDay = getWordOfDay(url)

#Prints out the definition

print("")
print(wordOfDay[0])
print("")

#IPhone widget interface__________________________

# label = ui.Label(font=('Menlo', 14), alignment=ui.ALIGN_CENTER)
# label.number_of_lines = wordOfDay[1]
# label.text = wordOfDay[0]

# appex.set_widget_view(label)
