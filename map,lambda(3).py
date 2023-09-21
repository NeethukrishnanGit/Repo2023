car_models=["Honda Civic", "Honda Accord", "Toyota Corolla", "Toyota Camry", "Ford Fusion", "Ford Escape", "Nissan Sentra", "Hyundai Elantra"]


def carmodels():
    temp=[]
    for ele in car_models:
        temp.append(ele.split())
    print(temp)
    temp=list(map(lambda x:x[1],temp))
    print(temp)
carmodels()