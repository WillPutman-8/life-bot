import random
from datetime import datetime


TODAY = datetime.now()
date = TODAY
day = TODAY.isoweekday()


def work_out(day_of_week):
    work = []
    # Push (chest/Shoulder/Triceps):

    mon = ["Incline dumbell press (4 sets of 10)", "Shoulder press (4 sets of 10)", "Shrugs (4 sets of 10)", "latteral raises (4 sets of 10)", "Bench Press (4 sets of 10)", "Incline bench (4 sets of 10)",
    "push down machine (4 sets of 15)", "Dealers choice"]
    
    # Pull (Back/biceps/forearms):

    tues = ["Dealers choice", "rows (4 sets of 20)", "Lat pull down (4 sets of 20)", "Bicep Curls (4 sets of 10)", "Pulls up (4 sets of 10)", "Dips (4 sets of 10)"]
    
    # Legs:
     
    wed = ["Squats (4 sets of 10)", "leg press (4 sets of 20)", "Lunge (4 sets of 10)", "Leg curl (4 sets of 10)"]
    
    # Abbs and Body weight:

    thur = ["russian twists (4 sets of 10)", "light weight front squat (4 sets of 10)", "sit ups (4 sets of 10)", "push ups (4 sets of 10)", "plank (4 for 1 min)"]
    
    # Weekend cardio upkeep:

    weekend = "Do 1hr of bag work if you feel like it after your long day of work."
    cardio = "30min of heavy bag work."
    
    # Making the workout list:

    if day_of_week == 1:
        use = mon
    elif day_of_week == 2:
        use = tues
    elif day_of_week == 3:
        use = wed
    elif day_of_week == 4:
        use = thur
    else:
        use = weekend
    
    if use != weekend:
        work.append(cardio)
        for i in range(5):
            x = random.choice(use)
            work.append(x)
            use.pop(x)
    else:
        work.append(weekend)

    return work
            
def chores(day_of_week):
    todo = []
    chore_list = ["clean and vacume living room", "wash dishes", "clean bathroom", "take out trash", "clean tub", "clean toilet" ]
    monday_list = ["clean and vacume room", "clean out car", "meal prep"]
    weekend = "No chores Since you had to work all day today bud"
    if day_of_week == 1:
        todo.append(monday_list)
    elif day_of_week > 1 and day_of_week < 6:
        for i in range(3):
            x = random.choice(chore_list)
            todo.append(x)
            chore_list.pop(x)
    else:
        todo.append(weekend)
    
    return todo
         
def eating():
    x = random.randint(0,501)
    if x != 500:
        meal = "Breakfast drink, tuna or chicken for lunch and dinner"
    else:
        meal = "The odds were against you but today is a cheat day for you!"
    
    return meal



gym = work_out(day)
my_chore = chores(day)
food = eating()

print(gym)
print(my_chore)
print(food)