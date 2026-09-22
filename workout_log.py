# First I define a class with its name, I did not put () because it does not inherit anything
class Workout:
    # Defined the first method __init__ to name the day of the workout
    def __init__(self,day_name):

        self.day_name = day_name
        self.saved = []  # Making a list to append the items needed to save the workout

    # Defined the log method to save our exercises, including 4 parameters
    def log(self,name,sets,reps,kg):

        if name == "" or sets <= 0 or reps <=0 or kg <= 0:
            return "Not Valid"

        new_list = [name,sets,reps,kg]
        self.saved.append(new_list)
      
  
  
        return f"{self.day_name}\nExercise: {name}\nSets: {sets}\nReps: {reps}\nKG: {kg} "

    # Made an update method to update any item to the value we want using kwargs which takes any number of arguments
    def update(self,index,**kwargs):

        if index < 0 or index >= len(self.saved): # First making an if condition to not have invalid arguments
            return "Not Valid"

        # Making a dictionary to assign the indexes of the values we need to update
        mapping = {
            "name" : 0,
            "sets" : 1,
            "reps" : 2,
            "kg" : 3}

        # Used a for loop to unpack kwargs and to take the key from mapping and update its value
        for key,value in kwargs.items():
            if key in mapping:
                position = mapping[key]
                self.saved[index][position] = value

        return "Updated"

    # Lastly made a remove method to pop any item from the list
    def remove(self,index=0):

        if index < 0 or index >= len(self.saved):
            return "Not Valid"

        self.saved.pop(index)
        return "Exercise removed"



            


        
        
exercise_1 = Workout("Push Day")



print(exercise_1.log("Shoulder Press",3,10,30))
print(exercise_1.log("Bench Press",4,8,60))
print(exercise_1.saved)



print(exercise_1.update(0,kg = 40))
print(exercise_1.saved)

print(exercise_1.remove(1))
print(exercise_1.saved)