import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
import mysql.connector

class DoctorUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Doctor Data Entry")
        self.setGeometry(200, 200, 400, 300)

        # Create labels and input fields
        self.name_label = QLabel("Name:")
        self.name_input = QLineEdit()
        self.age_label = QLabel("Age:")
        self.age_input = QLineEdit()
        self.address_label = QLabel("Address:")
        self.address_input = QLineEdit()
        self.phone_label = QLabel("Phone:")
        self.phone_input = QLineEdit()
        self.email_label = QLabel("Email:")
        self.email_input = QLineEdit()
        self.history_label = QLabel("Medical History:")
        self.history_input = QLineEdit()
        self.medication_label = QLabel("Medication Details:")
        self.medication_input = QLineEdit()
        self.appointment_label = QLabel("Appointment Date:")
        self.appointment_input = QLineEdit()

        # Create insert button
        self.insert_button = QPushButton("Insert Data")
        self.insert_button.clicked.connect(self.insert_data)

        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.age_label)
        layout.addWidget(self.age_input)
        layout.addWidget(self.address_label)
        layout.addWidget(self.address_input)
        layout.addWidget(self.phone_label)
        layout.addWidget(self.phone_input)
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)
        layout.addWidget(self.history_label)
        layout.addWidget(self.history_input)
        layout.addWidget(self.medication_label)
        layout.addWidget(self.medication_input)
        layout.addWidget(self.appointment_label)
        layout.addWidget(self.appointment_input)
        layout.addWidget(self.insert_button)

        # Set the central widget
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def insert_data(self):
        # Retrieve data from the input fields
        name = self.name_input.text()
        age = self.age_input.text()
        address = self.address_input.text()
        phone = self.phone_input.text()
        email = self.email_input.text()
        history = self.history_input.text()
        medication = self.medication_input.text()
        appointment = self.appointment_input.text()

        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Softwaredevelopmentfordigitalhealth",
            database="EHR_DATABASE"
        )
        cursor = connection.cursor()

        # Insert data into the Doctor table
        query = "INSERT INTO Doctor (Patient_Name, Patient_Age, Patient_Address, Patient_Phone, Patient_Email, Medical_History, Medication_Details, Appointment_Date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (name, age, address, phone, email, history, medication, appointment)
        cursor.execute(query, values)
        connection.commit()

        # Close the database connection
        cursor.close()
        connection.close()

        # Clear the input fields
        self.name_input.clear()
        self.age_input.clear()
        self.address_input.clear()
        self.phone_input.clear()
        self.email_input.clear()
        self.history_input.clear()
        self.medication_input.clear()
        self.appointment_input.clear()

        # Display a success message
        success_label = QLabel("Data inserted successfully!")
        layout = self.centralWidget().layout()
        layout.addWidget(success_label)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DoctorUI()
    window.show()
    sys.exit(app.exec_())








