class Pet:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species
        self.vaccinated = False
        self.appointments = {}

    def add_appointment(self, date, reason):
        if date not in self.appointments:
            self.appointments[date] = reason
            print(f"Appointment added for {self.name} on {date} for {reason}")
        else:
            print(f"{self.name} already has an appointment on {date}")

    def mark_vaccinated(self):
        self.vaccinated = True
        print(f"{self.name} has been marked as vaccinated")

    def view_appointments(self):
        if self.appointments:
            print(f"{self.name}'s appointments:")
            for date, reason in self.appointments.items():
                print(f"Date: {date}, Reason: {reason}")
        else:
            print(f"{self.name} has no upcoming appointments")

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Species: {self.species}")
        print(f"Vaccinated: {'Yes' if self.vaccinated else 'No'}")


# Example usage with user input:
if __name__ == "__main__":
    name = input("Enter pet's name: ")
    age = input("Enter pet's age: ")
    species = input("Enter pet's species: ")

    pet = Pet(name, age, species)

    while True:
        print("\n1. Add appointment")
        print("2. Mark as vaccinated")
        print("3. View appointments")
        print("4. Display pet information")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            date = input("Enter appointment date (YYYY-MM-DD): ")
            reason = input("Enter appointment reason: ")
            pet.add_appointment(date, reason)
        elif choice == '2':
            pet.mark_vaccinated()
        elif choice == '3':
            pet.view_appointments()
        elif choice == '4':
            pet.display_info()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option (1-5).")


