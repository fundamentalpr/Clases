#Serialization Examples
#With pickle

import pickle
pickled_string = pickle.dumps([1, 2, 3, "a", "b", "c"])
print(pickled_string)
print(pickle.loads(pickled_string))


#with json note you need to run
#easy_install simplejson before you have the proper libraries.
import json
json_string = json.dumps([1, 2, 3, "a", "b", "c"])
print(json_string)
print(json.loads(json_string))


#using the file io operations you could save the state of your objects using this techniques. they work on objects
class Student:
    def __init__(self, name):
        self.__name = name
        self.__average = 0
        self.__listOfClassesCompleted = []

    @property
    def Name(self):
        return self.__name

    @property
    def Average(self):
        return self.__average

    def _setName(self, name):
        self.__name = name

    def _addCompletedClass(self, className, result):
        self.__updateAverage(result)
        self.__listOfClassesCompleted.append(className)

    def __updateAverage(self, newClassScore):
    
        numberOfClasses = len(self.__listOfClassesCompleted)
        #first class scenario
        if ( numberOfClasses == 0):
            self.__average = newClassScore
            #anything else
        else:
            self.__average = (self.__average * numberOfClasses + newClassScore)/(numberOfClasses + 1)
estudiante = Student("Raul")
estudiante._addCompletedClass("matematica", 4.0)
print("Ejemplo con estudiante")
json_string = pickle.dumps(estudiante)
print(json_string)
estudiante2 = pickle.loads(json_string)
print(estudiante2)
print(estudiante2.Name)
print(estudiante2.Average)
