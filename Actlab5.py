def classify_age(age):
	if age < 0:
		print("Invalid age, cannot be found. ")
	elif age <= 12:
		print("You are a child. ")
	elif age <= 19:
		print("You are a teen. ")
	elif age <= 64:
		print("You are an adult. ")
	else:
		print("You are a senior. ")
		
classify_age(-5)