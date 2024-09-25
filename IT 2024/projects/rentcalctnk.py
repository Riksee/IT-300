# Import tkinter
from tkinter import *
class RentCalculator:

	def __init__(self):

		window = Tk() # Create a window
		window.title("Caretaker Rent Calculator") # Set title
		# create the input boxes.
		Label(window, text = "Annual Rent").grid(row = 1,
										column = 1, sticky = W)
		Label(window, text = "Number of Months Used").grid(row = 2,
									column = 1, sticky = W)
		Label(window, text = "Number of Months Left").grid(row = 3,
								column = 1, sticky = W)
		Label(window, text = "Monthly Payment").grid(row = 4,
									column = 1, sticky = W)
		Label(window, text = "Total Rent left").grid(row = 5,
									column = 1, sticky = W)

		# for taking inputs
		self.annualRentVar = StringVar() 
		Entry(window, textvariable = self.annualRentVar,
					justify = RIGHT).grid(row = 1, column = 2)
		self.numberOfMonthsUsedVar = StringVar()

		Entry(window, textvariable = self.numberOfMonthsUsedVar,
				justify = RIGHT).grid(row = 2, column = 2)
		self.numberOfMonthsLeftVar = StringVar()

		Entry(window, textvariable = self.numberOfMonthsLeftVar,
			justify = RIGHT).grid(row = 3, column = 2)
		self.monthlyPaymentVar = StringVar()
		lblMonthlyPayment = Label(window, textvariable =
						self.monthlyPaymentVar).grid(row = 4,
						column = 2, sticky = E)

		self.totalRentLeftVar = StringVar()
		lbltotalRentLeft = Label(window, textvariable =
					self.totalRentLeftVar).grid(row = 5,
					column = 2, sticky = E)
		
		# create the button
		btComputePayment = Button(window, text = "Compute Payment",
								command = self.computePayment).grid(
								row = 6, column = 2, sticky = E) 
		window.mainloop() # Create an event loop


	# compute the total payment.
	def computePayment(self):
				
		monthlyPayment = self.getMonthlyPayment(
		float(self.annualRentVar.get()),
		)

		self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f'))
		totalRentLeft = float(self.monthlyPaymentVar.get())* int(self.numberOfMonthsLeftVar.get())

		self.totalRentLeftVar.set(format(totalRentLeft, '10.2f'))

	def getMonthlyPayment(self, annualRent): 
		# compute the monthly payment.
		monthlyPayment = annualRent/12
		return monthlyPayment;
		root = Tk() # create the widget

# call the class to run the program.
RentCalculator()
