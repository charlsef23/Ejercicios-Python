#COMO ORDENAR DICCIONARIOS

datos = {"Juan": 20, "Pepe": 21, "Maria": 18, "Ana": 20, "Carlos": 19, "Daniel": 21, "Luis": 22, "Jose": 20}

dict(sorted(datos.items(), key=lambda x: x[1]))

