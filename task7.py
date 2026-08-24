class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


class Patient(Person):
    def __init__(self, name, age, gender, patient_id, ailment):
        super().__init__(name, age, gender)
        self.patient_id = patient_id
        self.ailment = ailment

    def get_details(self):
        base_details = super().get_details()
        return f"{base_details}, Patient ID: {self.patient_id}, Ailment: {self.ailment}"


class Doctor(Person):
    def __init__(self, name, age, gender, doctor_id, specialization):
        super().__init__(name, age, gender)
        self.doctor_id = doctor_id
        self.specialization = specialization
        self.assigned_patients = []

    def assign_patient(self, patient):
        self.assigned_patients.append(patient)

    def get_details(self):
        base_details = super().get_details()
        return f"{base_details}, Doctor ID: {self.doctor_id}, Specialization: {self.specialization}"


class Appointment:
    def __init__(self, appointment_id, patient, doctor, date, time):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time

    def get_appointment_info(self):
        return f"Appointment ID: {self.appointment_id} | Date: {self.date} {self.time} | Patient: {self.patient.name} | Doctor: {self.doctor.name}"


class Hospital:
    def __init__(self, name):
        self.name = name
        self.patients = []
        self.doctors = []
        self.appointments = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def schedule_appointment(self, appointment_id, patient, doctor, date, time):
        appointment = Appointment(appointment_id, patient, doctor, date, time)
        doctor.assign_patient(patient)
        self.appointments.append(appointment)
        return appointment