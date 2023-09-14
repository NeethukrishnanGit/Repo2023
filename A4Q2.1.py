def dictmake(a, b):

    x = {make: model for (make, model) in zip(a, [[i.split()[1] for i in b if j == i.split()[0]] for j in a])}
    return x


car_makes=["Honda", "Toyota", "Ford", "Nissan", "Hyundai"]
car_models=[ "Honda Civic", "Honda Accord", "Toyota Corolla", "Toyota Camry", "Ford Fusion", "Ford Escape", "Nissan Sentra", "Hyundai Elantra"]
print(dictmake(car_makes, car_models))