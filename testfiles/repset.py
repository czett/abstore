def calc(goal, lvl):
	try:
		if goal == "ME":
			sets = 3
			reps = round(12 + lvl * 3)
			return sets, reps
		elif goal == "MS":
			sets = 4
			reps = round(5 + lvl * 2.5)
			return sets, reps
		elif goal == "PS":
			sets = 5
			reps = round(1 + lvl * 0.4)
			return sets, reps
		else:
			raise ValueError("The given value for 'goal' is not valid.")

		if not lvl == 1 and not lvl == 2 and not lvl == 3:
			raise ValueError("The given value for 'level' is not valid. It needs to be 1, 2 or 3 (as an integer).")
	except:
		raise ValueError("An error occured.")

print(calc("MS", 2))