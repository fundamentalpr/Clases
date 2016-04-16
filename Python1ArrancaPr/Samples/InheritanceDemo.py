#File written by Alfredo Alvarez
#Python 3.3
#Demonstrate the creation of a class with getter setter and private methods.
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

class HighSchoolStudent(Student):
    def __init__(self, name, isVarsity):
        self.__varsity = isVarsity
        #calling parent constructor
        super().__init__(name)

    @property
    def IsVarsity(self):
        return self.__varsity
        
    



#Demonstrating use an execution of this code
#initializing the class.
a = Student("Johnson")
#Using the property
print(a.Name)
#Using the setter method
a._setName("Manuel")
print(a.Name)

#demonstrating use of a public method that calls a private one
a._addCompletedClass("Python 1" , 3.0)
print(a.Average)
a._addCompletedClass("Python 2" , 4.0)
print(a.Average)


#Demonstrating using the HighSchool Student
c = HighSchoolStudent("Thomas" , True)
print(c.IsVarsity)
print(c.Name)
#demoing i can do the same as in the other class                      
c._addCompletedClass("Python 1" , 3.0)
print(c.Average)
c._addCompletedClass("Python 2" , 4.0)
print(c.Average)


