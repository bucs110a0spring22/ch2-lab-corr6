import random
#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)
classes_per_week = 2
print("Classes per week:", classes_per_week)
print(classes_per_week, type(classes_per_week))
cost_per_class = (cost_per_week / classes_per_week)
print("Cost per Class:", cost_per_class)
print(cost_per_class, type(cost_per_class))

#Part B
list = [1,2,3,4,5]
random.choice(list)
print(random.choice(list))