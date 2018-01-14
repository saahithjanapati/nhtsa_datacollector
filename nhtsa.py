import urllib
from urllib.request import urlopen
from urllib.request import urlretrieve
from json import load
from tkinter import *
from PIL import ImageTk, Image

def second_screen():
		
		canvas1.delete('all')

		import tkinter as tk
		modelyear = modelyearbox.get()
		make = makebox.get()
		model = modelbox.get()
		print(modelyear, make, model)
		apiUrl ="http://www.nhtsa.gov/webapi/api/SafetyRatings"
		apiParam = "/modelyear/"+modelyear+"/make/"+make+"/model/"+model
		outputFormat = "?format=json"

		print(apiUrl + apiParam + outputFormat)
		response = urlopen(apiUrl + apiParam + outputFormat)

		json_obj = load(response)

		#Load the Result (vehicle collection) from the JSON response
		print('------------------------------')
		print('           Result			 ')
		print('------------------------------')
		array = json_obj['Results']
		dictionary = array[0]
		vehicle_name = dictionary['VehicleDescription']
		vehicle_id = str(dictionary['VehicleId'])

		#{'Count': 2, 'Message': 'Results returned successfully', 'Results': [{'VehicleDescription': '2013 Acura RDX SUV 4WD', 'VehicleId': 7731}, {'VehicleDescription': '2013 Acura RDX SUV FWD', 'VehicleId': 7520}]}

		print(vehicle_name, vehicle_id)

		apiUrl ="http://www.nhtsa.gov/webapi/api/SafetyRatings"
		apiParam = "/VehicleId/" + vehicle_id
		outputFormat = "?format=json"

		print(apiUrl + apiParam + outputFormat)
		response = urlopen(apiUrl + apiParam + outputFormat)

		header = Label(root, text = vehicle_name)
		header.config(font=("Courier", 44))
		header.pack()
		

		json_obj = load(response)
		for objectCollection in json_obj['Results']:
			# Loop each vehicle in the vehicles collection
			for variable, value in objectCollection.items():

				if variable == "VehiclePicture":
					urllib.request.urlretrieve(str(value), "car-picture.jpg")
					
					path = "car-picture.jpg"
					image = Image.open(path)
					photo = ImageTk.PhotoImage(image)

					labelpic = Label(root, image=photo)
					
					labelpic.pack()

				if "Picture" not in str(variable) and "Video" not in str(variable):
					string = str(variable) + ": " + str(value)
					print(string)
					print("\n")
					label = Label(root, text = string).pack()



		canvas1.delete("all")
		root.mainloop()


root = Tk()
canvas1 = Canvas(root)
root1 = Tk()
canvas = Canvas(root1, width=1000, height=700)

blanklabel1 = Label(root1, text= ' ').pack()
modelyearlabel = Label(root1, text= 'Enter the model year of your car').pack()
	
modelyearbox = Entry(root1)
modelyearbox.pack()
	

blanklabel2 = Label(root1, text= ' ').pack()
makeboxlabel = Label(root1, text= 'Enter the manufacturer of your car').pack()
makebox = Entry(root1)
makebox.pack()

blanklabel3 = Label(root1, text= ' ').pack()
modellabel = Label(root1, text= 'Enter the model of your car').pack()
modelbox = Entry(root1)
modelbox.pack()

blanklabel4 = Label(root1, text= ' ').pack()


button = Button(root1, text = 'Submit', command = second_screen)
button.pack()


root1.mainloop()
canvas.mainloop()