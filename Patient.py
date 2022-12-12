from tabulate import tabulate

class Patient():
    def __init__(self, pid, name, disease, gender, age):
        self.pid = pid
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age

    def formatPatientInfo(self,patient_info):
        formatted_info = "_".join(patient_info)
        return formatted_info

    def enterPatientInfo(self):
        self.pid = input("Enter Patient id: \n")
        self.name = input("Enter Patient name: \n")
        self.disease = input("Enter Patient disease: \n")
        self.gender = input("Enter Patient gender: \n")
        self.age = input("Enter Patient age: \n")
        return [self.pid,self.name,self.disease,self.gender,self.age]

    def readPatientsFile(self):
       with open("../OOP Project/text_files/patients.txt",'r') as patient_file:
            patient_list = patient_file.read()
            patient_list = patient_list.splitlines()
            return patient_list

    def searchPatientById(self,id):
        patient_list = self.readPatientsFile()
        found_patient = False
        for patient in patient_list:
            patient = patient.split("_")
            if id == patient[0]:
                found_patient = True
                self.displayPatientInfo(id)
        if found_patient == False:
            print("Cant find doctor with the same ID on the system")

    def displayPatientInfo(self,id):
        patients_list = self.readPatientsFile()
        for patients in patients_list:
            top_list = patients_list[0].split("_")
            patients = patients.split("_")
            if id == patients[0]:
                print(tabulate([patients], headers = top_list))

    def editPatientsInfo(self):
        patients_list = self.readPatientsFile()
        self.pid = input("Please enter the id of the doctor that you want to edit their information: \n")
        for patients in patients_list:
            patients = patients.split("_")
            if self.pid == patients[0]:
                self.name = input("Enter new Name: \n")
                self.disease = input("Enter new Disease: \n")
                self.gender = input("Enter new Gender: \n")
                self.age = input("Enter new Age: \n")
                patient_info = [self.pid,self.name,self.disease,self.gender,self.age]
                formatted_info = self.formatPatientInfo(patient_info)
                patients_list.append(formatted_info)
                self.writeListOfPatientsToFile(patients_list)
                break

    def displayPatientsList(self):
        patients_list = self.readPatientsFile()
        patient = [patients.split("_") for patients in patients_list]
        print(tabulate(patient, headers = "firstrow"))


    def writeListOfPatientsToFile(self, patients_file):
       with open("../OOP Project/text_files/patients.txt", 'w') as file:
            for patients in patients_file:
                file.write(patients)
                file.write("\n")

    def addPatientToFile(self):
        new_patient = self.enterPatientInfo()
        new_patient = self.formatPatientInfo(new_patient)
        patient_list = self.readPatientsFile()
        patient_list.append(new_patient)
        self.writeListOfPatientsToFile(patient_list)

p1 = Patient('','','','','')
p1.searchPatientById('16')
p1.displayPatientsList()