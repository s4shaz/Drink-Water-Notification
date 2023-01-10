import time
from plyer import notification

while True:
	notification.notify(
		title='Drink Water!',
		message='It has been 15 minutes since you last drank water',
		app_name='Water-Alert',
		app_icon= r"C:\Users\Lenovo\OneDrive\Desktop\Shashank Jha\cool projects\icon.ico",
		timeout = 6,
		ticker='Water Alert',
	)
	time.sleep(900)

	
