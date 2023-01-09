import abtools as at

def create(split, lvl, wlvl, goal, tgoal, loc, quan):
	if not split == "split" and not split == "wb":
		raise ValueError("The given value for 'split' is not valid. It needs to be 'wb' or 'split'.")

	plan = [] # every sublist represents a new day, every sub-sublist a new exercise

	if quan == 3:
		split_type = "PPL" # push pull legs
	if quan == 4:
		split_type = "BPLO" # back/biceps; push (chest, triceps); legs; other (shoulders, forearms)
	if quan == 5:
		split_type = "CBASL" # chest, back, arms, shoulders, legs
	if quan == 6:
		split_type = "PPL" # push pull legs
		alt_split_type = "Arnold" # cblsa -> chest & back, legs, shoulder & arms

	daycount = 1
	ex = []

	for i in range(quan):

		# ---------------------------- PPL PLAN CREATION ----------------------------

		if split_type == "PPL":
			if daycount == 1:
				ex = at.find_exercises("", "", wlvl, "", "Push", "", "")[1:] # finds exercises for given fitness level

				if wlvl != "Beginner": # only for non beginner lvl bc there is no level below beginner
					ex2 = at.find_exercises("", "", at.minus_level(wlvl), "", "Push", "", "")[1:] # finds exercises for level below

					for item in ex2:
						ex.append(item) # append 2nd list to 1st

				ex.sort(key=lambda x: x[0]) # sort combined list using the muscle (-> eg calves, quads...)
				del_ind = []

				for count, value in enumerate(ex):
					if value[3] == "Lower":
						del_ind.append(count)
					else:
						value.append(list(at.repset(tgoal, lvl))) # calculate reps based on level and goal with abtools
						#value.append(at.calculate_reps(value)) # calculate reps based on gear with abtools (OUTDATED) (return ex type too!)

			if daycount == 2:
				ex = at.find_exercises("", "", wlvl, "", "Pull", "", "")[1:] # finds exercises for given fitness level

				if wlvl != "Beginner": # only for non beginner lvl bc there is no level below beginner
					ex2 = at.find_exercises("", "", at.minus_level(wlvl), "", "Pull", "", "")[1:] # finds exercises for level below

					for item in ex2:
						ex.append(item) # append 2nd list to 1st

				ex.sort(key=lambda x: x[0]) # sort combined list using the muscle (-> eg calves, quads...)
				del_ind = []

				for count, value in enumerate(ex):
					if value[3] == "Lower":
						del_ind.append(count)
					else:
						value.append(list(at.repset(tgoal, lvl))) # calculate reps based on level and goal with abtools
						#value.append(at.calculate_reps(value)) # calculate reps based on gear with abtools (OUTDATED) (return ex type too!)

			if daycount == 3:
				ex = at.find_exercises("", "", wlvl, "Lower", "", "", "")[1:] # finds exercises for given fitness level

				if wlvl != "Beginner": # only for non beginner lvl bc there is no level below beginner
					ex2 = at.find_exercises("", "", at.minus_level(wlvl), "Lower", "", "", "")[1:] # finds exercises for level below

					for item in ex2:
						ex.append(item) # append 2nd list to 1st

				ex.sort(key=lambda x: x[0]) # sort combined list using the muscle (-> eg calves, quads...)
				del_ind = []

				for count, value in enumerate(ex):
					if value[3] == "Upper" or value[3] == "Core":
						del_ind.append(count)
					else:
						value.append(list(at.repset(tgoal, lvl))) # calculate reps based on level and goal with abtools
						#value.append(at.calculate_reps(value)) # calculate reps based on gear with abtools (OUTDATED) (return ex type too!)

			if loc != "GYM":
				for count, value in enumerate(ex):
					if "BW" not in value[5]:
						if count not in del_ind:
							del_ind.append(count)

			del_ind.sort(reverse=True) 

			for index in del_ind:
				ex.pop(index)

			previous_previous_muscle = None # not more than 2 ex./muscle
			previous_muscle = None
			del_ind = []

			for count, value in enumerate(ex):
				if value[0] == previous_previous_muscle:
					del_ind.append(count)
				previous_previous_muscle = previous_muscle
				previous_muscle = value[0]

			del_ind.sort(reverse=True)

			for item in del_ind:
				ex.pop(item)

			day = ex
			plan.append(day)

			if quan == 6 and daycount == 3:
				daycount = 1
			else:
				daycount += 1

	# ---------------------------- PPL PLAN CREATION ENDS HERE ----------------------------

	return plan

plan = create("split", 1, "Beginner", "GW", "PS", "GYM", 6)

print(plan[0])
print("\n")
print(plan[1])
print("\n")
print(plan[2])