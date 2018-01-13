from urllib.request import urlopen
from json import load
from tkinter import *



modelyear = ""
make = ""
model = ""

root = Tk()

canvas = Canvas(root, width=1000, height=700)

def mubmit():

	apiUrl = "http://www.nhtsa.gov/webapi/api/SafetyRatings"

	apiParam = "/modelyear/2013/make/Acura/model/rdx"

	outputFormat = "?format=json"

	response = urlopen(apiUrl + apiParam + outputFormat)




	#################################################################
	json_obj = load(response)

	#Load the Result (vehicle collection) from the JSON response
	print('------------------------------')
	print('           Result			 ')
	print('------------------------------')
	for objectCollection in json_obj['Results']:
		# Loop each vehicle in the vehicles collection
	    for variable, value in objectCollection.items():
	        print(variable, ": ", value)
	    print("\n")




blanklabel1 = Label(root, text= ' ').pack()
modelyearlabel = Label(root, text= 'Enter the model year of your car').pack()
modelyearbox = Entry(root, textvariable=modelyear).pack()

blanklabel2 = Label(root, text= ' ').pack()
makeboxlabel = Label(root, text= 'Enter the manufacturer of your car').pack()
makebox = Entry(root, textvariable=make).pack()

blanklabel3 = Label(root, text= ' ').pack()
modellabel = Label(root, text= 'Enter the model of your car').pack()
modelbox = Entry(root, textvariable=model).pack()

blanklabel4 = Label(root, text= ' ').pack()
button = Button(root, text = 'Submit', command = mubmit,fg = 'black', bg='white').pack()

canvas.pack()
root.mainloop()





