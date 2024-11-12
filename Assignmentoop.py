#Assignment OOP

# a)Add a constructor to the cohort class

class cohort:
    def _init_(self,name,description,start_date,end_date):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
p=cohort("Sandra","witu student","20/8/2024","20/6/2026")
print(p.name) 
print(p.description) 
print(p.start_date)  
print(p.end_date)


# b)Add a method to the class that prints the cohort name and the total number of students


class cohort:
    def _init_(self,cohort_name,total_number_of_students):
        self.cohort_name = cohort_name
        self.total_number_of_students = total_number_of_students
    def myfunc(self):
        print("The chort name is " + self.cohort_name + "and the total number of students is" + self.total_number_of_students)
p = cohort("chort4",60)
p.myfunc()



#Create a new instance of the cohort class

class cohort:
    def __init__(self,name,description,start_date,end_date):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
cohortfive=cohort("Nairuba","Diploma in computer science","20/8/2024","20/6/2026")
print(cohortfive.name)
print(cohortfive.description)
print(cohortfive.start_date) 
print(cohortfive.end_date)       
            