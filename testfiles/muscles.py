import string

def exercise_list():
	with open("exercises.csv", "r") as ex:
		content = ex.readlines()
		return content

def find_exercises(muscle, level, gear):
	content = exercise_list()

	legend = content[0].split(",")
	results = []

	for line in content:
		line = line.split(",")

		if muscle in line[legend.index("Muscle")]:
			if level in line[legend.index("Level")]:
				if gear in line[legend.index("Gear")]:
					results.append(line)

	return results

#find_exercises("Quadriceps", "Beginner", "M")

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

#print(get_exercise_info("Leg extension"))

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
	elif "C" in exercise[legend.index("Gear")]:
		if string.capwords("pulldown") in exercise[legend.index("Exercise")]:
			exercise_type = "cable-pulldown"
			reps = 15
			sets = 3
		if string.capwords("fly") in exercise[legend.index("Exercise")]:
			exercise_type = "cable-fly"
			reps = 10
			sets = 5
	elif "M" in exercise[legend.index("Gear")]:
		exercise_type = "machine"
		reps = 10
		sets = 5
	else:
		exercise_type = "other"
		reps = 15
		sets = 5

	out = [exercise_type, reps, sets]

	return out

print(find_exercises("Biceps", "Beginner", "FW"))