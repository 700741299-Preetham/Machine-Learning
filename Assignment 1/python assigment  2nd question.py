#creating empty dict
dog = {}
print("",type(dog))

#creating keys and values to dog dict
dog = {"name":"Milky", "color":"White", "breed":"Pug", "legs":"tall", "age":"2years"}
print('', dog)

#creating keys and values to student dict
student = {"first_name":"Preetham", "last_name":"Kesireddy", "gender":"male", "age":"24", "marital status":"single", "skill":"Python", "country":"India", "city":"Warangal", "address":"1-14 Malkapur"}
print('',student)

#getting the length of student dict
print("length of student dict is :", len(student))

#getting skill and its type in list format
list = [student['skill'],type(student['skill'])]
print("skill and type of skill is :",list)

#adding more skill values
student['skill']="Python,Airflow"
print("",student)

#printing dict keys as list
print(student.keys())

#printing dict values as list
print(student.values())
