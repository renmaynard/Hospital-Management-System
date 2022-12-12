from tabulate import tabulate

class Doctor():

    def __init__(self, id, name, specialist, timing, qualification, roomNb):
        self.id = id
        self.name = name
        self.specialist = specialist
        self.timing = timing
        self.qualification = qualification
        self.roomNb = roomNb

    def formatDrinfo(self,dr_info):
        formatted_info = "_".join(dr_info)
        return formatted_info

    def enterDRinfo(self):
        self.id = input("Enter the doctor's ID: \n")
        self.name = input("Enter the doctor's name: \n")
        self.specialist = input("Enter the doctor's specialty: \n")
        self.timing = input("Enter the doctor's timing(e.g., 7am-10pm): \n")
        self.qualification = input("Enter the doctor's qualification: \n")
        self.roomNb = input("Enter the doctor's room number: \n")
        return [self.id,self.name,self.specialist,self.timing,self.qualification,self.roomNb]


    def readDoctorsFile(self):
        with open("../OOP Project/text_files/doctors.txt",'r') as doctors_file:
            doctors_list = doctors_file.read()
            doctors_list = doctors_list.splitlines()
            return doctors_list

    def searchDoctorById(self,id):
        doctors_list = self.readDoctorsFile()
        found_doctor = False
        for doctors in doctors_list:
            doctors = doctors.split("_")
            if id == doctors[0]:
                found_doctor = True
                self.displayDoctorInfo(id)
        if found_doctor == False:
            print("Cant find doctor with the same ID on the system")

    def searchDoctorByName(self,name):
        doctors_list = self.readDoctorsFile()
        found_doctors = False
        for doctors in doctors_list:
            doctors = doctors.split("_")
            if name == doctors[1]:
               found_doctors = True
               self.displayDoctorInfo(doctors[0])
        if found_doctors == False:
            print("Cant find doctor with the same ID on the system")
        
    def displayDoctorInfo(self,id):
        doctors_list = self.readDoctorsFile()
        for doctors in doctors_list:
            top_list = doctors_list[0].split("_")
            doctors = doctors.split("_")
            if id == doctors[0]:
                print(tabulate([doctors], headers = top_list))

    def editDoctorInfo(self):
        doctors_list = self.readDoctorsFile()
        self.id = input("Please enter the id of the doctor that you want to edit their information: \n")
        for doctor in doctors_list:
            doctor = doctor.split("_")
            if self.id == doctor[0]:
                doctor.clear()
                self.name= input("Enter new Name: \n")
                self.specialist= input("Enter new Specilist in: \n")
                self.timing= input("Enter new Timing: \n")
                self.qualification = input("Enter new Qualification: \n")
                self.roomNb = input("Enter new Room Number: \n")
                dr_info = [self.id,self.name,self.specialist,self.timing,self.qualification,self.roomNb]
                formatted_doctor = self.formatDrinfo(dr_info)
                doctors_list.append(formatted_doctor)
                self.writeListOfDoctorsToFile(doctors_list)
                break

    def displayDoctorsList(self):
        doctors_list = self.readDoctorsFile()
        doctor = [doctors.split("_") for doctors in doctors_list]
        print(tabulate(doctor, headers="firstrow"))

    def writeListOfDoctorsToFile(self,doctor_file):
        with open("../OOP Project/text_files/doctors.txt", 'w') as file:
            for doctors in doctor_file:
                file.write(doctors)
                file.write("\n")

    def addDrToFile(self):
        new_doctor = self.enterDRinfo()
        new_doctor = self.formatDrinfo(new_doctor)
        doctor_list = self.readDoctorsFile()
        doctor_list.append(new_doctor)
        self.writeListOfDoctorsToFile(doctor_list)

d1 = Doctor('33','','','','','')
d1.editDoctorInfo()
