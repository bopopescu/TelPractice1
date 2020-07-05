def person(name,**data):
    print(name)
    print(data)
    for key,value in data.items():
        print(key,' ',value)



person(name='geetha',age=30,city='Bangalore',phoneno=675786298)