def models(a):
    return list(map(lambda x:x.split()[1],a))

car_makes=["Honda", "Toyota", "Ford", "Nissan", "Hyundai"]
car_models=[ "Honda Civic", "Honda Accord", "Toyota Corolla", "Toyota Camry", "Ford Fusion", "Ford Escape", "Nissan Sentra", "Hyundai Elantra"]

print(models(car_models))