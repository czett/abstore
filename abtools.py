import string, math
from py_edamam import Edamam

def repset(goal, lvl):

	# Goal = "ME" (muscular endurance), "MS" (muscular size), "PS" (power & strength)
	# Lvl = 1 (beginner), 2 (intermediate), 3 = (expert)

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

def exercise_list():
	with open("exercises.csv", "r") as ex:
		content = ex.readlines()
		return content

def find_nutrients(term): # to be added: carbs, fat
	e = Edamam(nutrition_appid='c3d0e8a5', nutrition_appkey='d2af91e496fc2906ccec7c9bf0b46f40')

	cal = e.search_nutrient(search_value)['totalNutrients']['ENERC_KCAL']['quantity'] # kcal
	prt = e.search_nutrient(search_value)['totalNutrients']['PROCNT']['quantity'] # in grams

	return cal, prt

def lbs_to_kg(lbs, oz):
	kgs = lbs * 0.4536
	kgs = kgs + oz * 0.02835

	return kgs

def ft_to_cm(ft, inc):
	cm = ft * 30.48
	cm = cm + inc * 2.54

	return cm

def kg_to_lbs(kg):
	lbs = math.floor(kg * 2.2045)
	oz = round(kg * 35.2733) - lbs * 16

	return lbs, oz

def cm_to_ft(cm):
	ft = math.floor(cm * 0.0328)
	inc = round(cm * 0.3937) - ft * 12

	return ft, inc

def get_exercise_info(exercise):
	content = exercise_list()
	legend = content[0].split(",")
	content = content[1:]

	results = []

	for line in content:
		line = line.split(",")
		if string.capwords(exercise) in line[legend.index("Exercise")]:
			results.append(line)

	return results

def find_exercises(Muscle, Exercise, Level, Region, PushPull, Gear, Joint):

	# Level in words!!! Gear = M (machine), F (free weight), C (cables), BW (Bodyweight; (BWA means Bodyweight-Attention (there may be additional equipment required)))

	content = exercise_list()

	legend = content[0].split(",")
	legend[-1] = legend[-1].strip()

	results = []

	for line in content:
		line = line.split(",")
		line[-1] = line[-1].strip()

		if Muscle in line[legend.index("Muscle")] or Muscle == "":
			if Exercise in line[legend.index("Exercise")] or Exercise == "":
				if Level in line[legend.index("Level")] or Level == "":
					if Region in line[legend.index("Region")] or Region == "":
						if PushPull in line[legend.index("PushPull")] or PushPull == "":
							if Gear in line[legend.index("Gear")] or Gear == "":
								if Joint in line[legend.index("Joint")] or Joint == "":
									results.append(line)

	return results

def calculate_reps(exercise):
	content = exercise_list()
	legend = content[0].split(",")
	
	exercise_type = None
	reps = None
	sets = None
	out = []

	if "FW" in exercise[legend.index("Gear")]:
		if string.capwords("barbell") in exercise[legend.index("Exercise")]:
			exercise_type = "barbell"
			reps = 5
			sets = 10
		elif string.capwords("dumbbell") in exercise[legend.index("Exercise")]:
			exercise_type = "dumbbell"
			reps = 10
			sets = 5
		else:
			exercise_type = "free weights"
			reps = 10
			sets = 5
	elif "C" in exercise[legend.index("Gear")]:
		if string.capwords("pulldown") in exercise[legend.index("Exercise")]:
			exercise_type = "cable-pulldown"
			reps = 15
			sets = 3
		if string.capwords("fly") in exercise[legend.index("Exercise")]:
			exercise_type = "cable-fly"
			reps = 10
			sets = 5
		else:
			exercise_type = "cable"
			reps = 10
			sets = 5
	elif "M" in exercise[legend.index("Gear")]:
		exercise_type = "machine"
		reps = 10
		sets = 5
	elif "BW" in exercise[legend.index("Gear")]:
		exercise_type = "bodyweight"
		reps = 15
		sets = 3
	else:
		exercise_type = "other"
		reps = 15
		sets = 5

	out = [exercise_type, sets, reps]

	return out

def minus_level(level):
	try:
		if level == "Beginner":
			return ValueError("Invalid value.")
		elif level == "Intermediate":
			return "Beginner"
		elif level == "Advanced":
			return "Intermediate"
		else:
			return ValueError("Invalid Value.")
	except:
		return ValueError("Invalid Value.")

def repset(goal, lvl):
	try:
		if goal == "ME":
			sets = 2
			reps = round(12 + lvl * 3)
			return sets, reps
		elif goal == "MS":
			sets = 3
			reps = round(7 + lvl * 2.5)
			return sets, reps
		elif goal == "PS":
			sets = 4
			reps = round(1 + lvl * 0.4)
			return sets, reps
		else:
			raise ValueError("The given value for 'goal' is not valid.")

		if not lvl == 1 and not lvl == 2 and not lvl == 3:
			raise ValueError("The given value for 'level' is not valid. It needs to be 1, 2 or 3 (as an integer).")
	except:
		raise ValueError("An error occured.")