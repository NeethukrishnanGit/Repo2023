from functools import reduce
def models(a):
    x= reduce(lambda a, b: a+","+b, [i.split()[1] for i in a])
    return x

car_makes=["Honda", "Toyota", "Ford", "Nissan", "Hyundai"]
car_models=[ "Honda Civic", "Honda Accord", "Toyota Corolla", "Toyota Camry", "Ford Fusion", "Ford Escape", "Nissan Sentra", "Hyundai Elantra"]

print(models(car_models))