{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "4262c989-ae14-4e2d-b784-9c46e75eaaf0",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Employee Management System \n",
    "\n",
    "# Step 1 : Initialize the dictionary with some sample employee data for testing\n",
    "\n",
    "employees =  {101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000},\n",
    "             102: {'name': 'Ajay' , 'age': 20, 'department':'AI/ML', 'salary':90000}\n",
    "             }"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "51bfe73a-435e-4136-b7e7-1ef2472c6653",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Step 3: Add Employee\n",
    "def add_employee():\n",
    "    try:\n",
    "        emp_id = int(input(\"Enter Employee ID: \"))\n",
    "        if emp_id in employees:\n",
    "            print(\"❌ Employee ID already exists. Try again.\")\n",
    "            return\n",
    "\n",
    "        name = input(\"Enter Employee Name: \")\n",
    "        age = int(input(\"Enter Employee Age: \"))\n",
    "        department = input(\"Enter Employee Department: \")\n",
    "        salary = float(input(\"Enter Employee Salary: \"))\n",
    "\n",
    "        employees[emp_id] = {\n",
    "            'name': name,\n",
    "            'age': age,\n",
    "            'department': department,\n",
    "            'salary': salary\n",
    "        }\n",
    "        print(f\"✅ Employee {name} added successfully!\")\n",
    "\n",
    "    except ValueError:\n",
    "        print(\"⚠ Invalid input. Please enter correct details.\")\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "dd045bac-408c-48c5-aa55-9ac5fc1b7ee9",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "# Step 4: View All Employees\n",
    "def view_employees():\n",
    "    if not employees:\n",
    "        print(\"⚠ No employees available.\")\n",
    "        return\n",
    "\n",
    "    print(\"\\n--- Employee List ---\")\n",
    "    print(f\"{'ID':<10}{'Name':<15}{'Age':<10}{'Department':<15}{'Salary':<10}\")\n",
    "    print(\"-\" * 60)\n",
    "    for emp_id, details in employees.items():\n",
    "        print(f\"{emp_id:<10}{details['name']:<15}{details['age']:<10}{details['department']:<15}{details['salary']:<10}\")\n",
    "    print(\"-\" * 60)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "0a843022-92dc-407b-91ff-8346265c55d5",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Step 5: Search Employee by ID\n",
    "\n",
    "def search_employee():\n",
    "    try:\n",
    "        emp_id = int(input(\"Enter Employee ID to search :\"))\n",
    "        if emp_id in employees:\n",
    "            details = employees[emp_id]\n",
    "            print(\"\\n--- Employee Found ---\")\n",
    "            print(\"\\n--- Employee Found ---\")\n",
    "            print(f\"ID: {emp_id}\")\n",
    "            print(f\"Name: {details['name']}\")\n",
    "            print(f\"Age: {details['age']}\")\n",
    "            print(f\"Department: {details['department']}\")\n",
    "            print(f\"Salary: {details['salary']}\")\n",
    "        else:\n",
    "           print(\"❌ Employee not found.\")\n",
    "    except ValueError:\n",
    "         print(\"⚠ Please enter a valid numeric Employee ID.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "61b5a1b1-e797-450a-912e-9e09066bef44",
   "metadata": {},
   "outputs": [],
   "source": [
    "# step 2 and 6 : Menu System & Exit \n",
    "\n",
    "def main_menu():\n",
    "    while True :\n",
    "        print(\"\\n===== Employee Management System =====\")\n",
    "        print(\"1. Add Employee\")\n",
    "        print(\"2. View All Employees\")\n",
    "        print(\"3. Search for Employee\")\n",
    "        print(\"4. Exit\")\n",
    "        choice = input(\"enter your choice (1-4) : \")\n",
    "\n",
    "        if choice == '1':\n",
    "            add_employee()\n",
    "        elif choice == '2':\n",
    "            view_employees()\n",
    "        elif choice == '3':\n",
    "            search_employee()\n",
    "        elif choice == '4' :\n",
    "            print(\"🙏 Thank you for using EMS. Goodbye!\")\n",
    "            break\n",
    "        else:\n",
    "            print(\"⚠ Invalid choice. Please try again.\")\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "d273a66f-f9d6-4482-a036-bbd149196223",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "===== Employee Management System =====\n",
      "1. Add Employee\n",
      "2. View All Employees\n",
      "3. Search for Employee\n",
      "4. Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter your choice (1-4) :  1\n",
      "Enter Employee ID:  103\n",
      "Enter Employee Name:  ritesh\n",
      "Enter Employee Age:  26\n",
      "Enter Employee Department:  devloper\n",
      "Enter Employee Salary:  60000\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Employee ritesh added successfully!\n",
      "\n",
      "===== Employee Management System =====\n",
      "1. Add Employee\n",
      "2. View All Employees\n",
      "3. Search for Employee\n",
      "4. Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter your choice (1-4) :  2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "--- Employee List ---\n",
      "ID        Name           Age       Department     Salary    \n",
      "------------------------------------------------------------\n",
      "101       Satya          27        HR             50000     \n",
      "102       Ajay           20        AI/ML          90000     \n",
      "103       ritesh         26        devloper       60000.0   \n",
      "------------------------------------------------------------\n",
      "\n",
      "===== Employee Management System =====\n",
      "1. Add Employee\n",
      "2. View All Employees\n",
      "3. Search for Employee\n",
      "4. Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter your choice (1-4) :  3\n",
      "Enter Employee ID to search : 103\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "--- Employee Found ---\n",
      "\n",
      "--- Employee Found ---\n",
      "ID: 103\n",
      "Name: ritesh\n",
      "Age: 26\n",
      "Department: devloper\n",
      "Salary: 60000.0\n",
      "\n",
      "===== Employee Management System =====\n",
      "1. Add Employee\n",
      "2. View All Employees\n",
      "3. Search for Employee\n",
      "4. Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter your choice (1-4) :  4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "🙏 Thank you for using EMS. Goodbye!\n"
     ]
    }
   ],
   "source": [
    "# Run the Program\n",
    "if __name__ == \"__main__\":\n",
    "    main_menu()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9b00a2e6-56f4-4d28-9381-e604982de8a7",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
