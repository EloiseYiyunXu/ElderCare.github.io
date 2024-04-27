import os
import openai
import json
import time

openai.api_key = "sk-proj-IdwhTgMVcgQpbIvsQLjnT3BlbkFJKlMtRMA8EbjZfkm3qTAV"

class Profile:
    def __init__(self, prompt):
        self.prompt = prompt
        self.key = os.getenv("sk-proj-IdwhTgMVcgQpbIvsQLjnT3BlbkFJKlMtRMA8EbjZfkm3qTAV")
        self.max_try = 0
        self.model = "gpt-3.5-turbo"

    def Answering(self, question, answer_format):
        completion = openai.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages = [
                {"role": "system", "content": "You are a chatbot, please answer the question based on the user profile information"},
                {"role": "system", "content": f"You should answer the question based on the user input in prompt {question}"},
                {"role": "system", "content": f"You answer should be in {answer_format} format"},
                {"role": "user", "content": f"{self.prompt}"}
            ]
        )
        return completion.choices[0].message.content
    
    def getName(self):
        question = "What is your name?"
        answer_format = "Name should be only first name and last name."
        name = self.Answering(question, answer_format)
        return name

    def getAge(self):
        question = "What is your age?"
        answer_format = "Age should be an integer, please enter integer only"
        age = self.Answering(question, answer_format)
        try:
            age = int(age)
            self.max_try = 0
            return age
        except ValueError:
            self.max_try += 1
            if self.max_try == 3:
                return "unknown"
            
    def getGender(self):
        question = "What is your gender?"
        answer_format = "Only enter 'male', 'female', 'non-binary"
        gender = self.Answering(question, answer_format)
        if gender in ['male', 'female','non-binary']:
            self.max_try = 0
            return gender
        else:
            self.max_try += 1
            if self.max_try == 3:
                return "unknown"
            
    def getEthcity(self):
        question ="What is your ethcity?"
        answer_format = "Only enter 'white', 'black', 'asain', 'mix'"
        ethcity = self.Answering(question, answer_format)
        if ethcity in ['white', 'black', 'asain', 'mix']:
            self.max_try = 0
            return ethcity
        else:
            self.max_try += 1
            if self.max_try == 3:
                return "unknown"
            
    def getSmokeStatus(self):
        question ="How often do you smoke? Only enter 'often', 'sometimes', 'none'"
        answer_format = "Only enter 'often', 'sometimes', 'none'"
        smoke_status = self.Answering(question, answer_format)
        if smoke_status in ['often', 'sometimes', 'none']:
            self.max_try = 0
            return smoke_status
        else:
            self.max_try += 1
            if self.max_try == 3:
                return "unknown"
    
    def getBMI(self):
        question = "What is your BMI? Integer only"
        answer_format = "BMI should be an integer, please enter integer only"
        BMI = self.Answering(question, answer_format)
        try:
            BMI = int(BMI)
            self.max_try = 0
            return BMI
        except ValueError:
            self.max_try += 1
            if self.max_try == 3:
                return "unknown"
            
    def getBloodPressure(self):
        question = "What is your blood pressure? Integer only"
        answer_format = "blood pressure should be an integer, please enter integer only"
        blood_pressure = self.Answering(question, answer_format)
        try:
            blood_pressure = int(blood_pressure)
            self.max_try = 0
            return blood_pressure
        except ValueError:
            self.max_try += 1
            if self.max_try == 3:
                return "unknown"
            
    def getBloodGlucose(self):
        question = "What is your blood glucose? Integer only"
        answer_format = "blood glucose should be an integer, please enter integer only"
        blood_glucose = self.Answering(question, answer_format)
        try:
            blood_glucose = int(blood_glucose)
            self.max_try = 0
            return blood_glucose
        except ValueError:
            self.max_try += 1
            if self.max_try == 3:
                return "unknown"
            
    def getDiabetes(self):
        question = "Do you have diabetes? Enter 1 for 'Yes', 0 for 'No'"
        answer_format = "diabetes can only be 1 or 0, 1 for 'Yes', 0 for 'No'"
        diabetes = self.Answering(question, answer_format)
        if diabetes == 1:
            return "Yes, the user have diabetes"
        elif diabetes == 0:
            return "No, the user doesn't have diabetes"
        else:
            self.max_try += 1
            if self.max_try == 3:
                return "unknown"

    def getHeartDisease(self):
        question ="Do you have any heart disease? Only enter 'none', 'coronary artery disease', 'hypertension', 'heart failure', 'arrhythmias', 'valvular heart disease', 'cardiomyopathy', 'peripheral artery disease', 'congenital heart defects'"
        answer_format = "Only enter 'none', 'coronary artery disease', 'hypertension', 'heart failure', 'arrhythmias', 'valvular heart disease', 'cardiomyopathy', 'peripheral artery disease', 'congenital heart defects'"
        heart_disease = self.Answering(question, answer_format)
        if heart_disease in ['none', 'coronary artery disease', 'hypertension', 'heart failure', 'arrhythmias', 'valvular heart disease', 'cardiomyopathy', 'peripheral artery disease', 'congenital heart defects']:
            self.max_try = 0
            return heart_disease
        else:
            self.max_try += 1
            if self.max_try == 5:
                return "unknow"
            
    """def finalInfo(self):
        name = self.getName()
        age = self.getAge()
        gender = self.getGender()
        ethcity = self.getEthcity()
        smoke_status = self.getSmokeStatus()
        BMI = self.getBMI()
        blood_pressure = self.getBloodPressure()
        blood_glucose = self.getBloodGlucose()
        diabetes = self.getDiabetes()
        heart_disease = self.getHeartDisease()
        return (name, age, gender, ethcity, smoke_status, BMI, blood_pressure, blood_glucose, diabetes, heart_disease)"""
    

    def finalInfo(self):
        name = self.getName()
        age = self.getAge()
        gender = self.getGender()
        ethcity = self.getEthcity()
        smoke_status = self.getSmokeStatus()
        BMI = self.getBMI()
        blood_pressure = self.getBloodPressure()
        blood_glucose = self.getBloodGlucose()
        diabetes = self.getDiabetes()
        heart_disease = self.getHeartDisease()
        return {"name": name, "age": age, "gender": gender, "ethcity": ethcity, "smoke_status": smoke_status, "BMI": BMI, "blood_pressure": blood_pressure, "blood_glucose": blood_glucose, "diabetes": diabetes, "heart_disease": heart_disease}
    






            

            
    
            
    

    

