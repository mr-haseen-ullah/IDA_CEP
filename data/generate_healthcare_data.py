import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)

# Generate 800 patient records
n_patients = 800

# Patient demographics
patient_ids = [f"P{str(i).zfill(5)}" for i in range(1, n_patients + 1)]
names = [f"Patient_{i}" for i in range(1, n_patients + 1)]
ages = np.random.randint(18, 85, n_patients)
genders = np.random.choice(['Male', 'Female'], n_patients, p=[0.48, 0.52])
blood_types = np.random.choice(['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'], 
                              n_patients, p=[0.34, 0.06, 0.09, 0.02, 0.03, 0.01, 0.38, 0.07])

# Medical conditions
conditions = [
    'Diabetes', 'Hypertension', 'Asthma', 'Cancer', 'Arthritis',
    'Obesity', 'Heart Disease', 'Kidney Disease', 'Pneumonia', 'Flu'
]
medical_conditions = np.random.choice(conditions, n_patients)

# Admission details
admission_types = np.random.choice(['Emergency', 'Elective', 'Urgent'], 
                                  n_patients, p=[0.35, 0.50, 0.15])

# Generate admission dates (last 2 years)
start_date = datetime(2024, 1, 1)
end_date = datetime(2025, 12, 31)
date_diff = (end_date - start_date).days
admission_dates = [start_date + timedelta(days=int(np.random.randint(0, date_diff))) 
                  for _ in range(n_patients)]

# Length of stay (days) - influenced by admission type and condition
base_los = np.random.randint(1, 15, n_patients)
los = []
for i in range(n_patients):
    if admission_types[i] == 'Emergency':
        stay = base_los[i] + np.random.randint(0, 5)
    elif medical_conditions[i] in ['Cancer', 'Heart Disease', 'Kidney Disease']:
        stay = base_los[i] + np.random.randint(2, 8)
    else:
        stay = base_los[i]
    los.append(min(stay, 30))  # Cap at 30 days

# Discharge dates
discharge_dates = [admission_dates[i] + timedelta(days=int(los[i])) for i in range(n_patients)]

# Doctors
doctors = [f"Dr. {surname}" for surname in ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones',
                                             'Garcia', 'Miller', 'Davis', 'Martinez', 'Hernandez']]
assigned_doctors = np.random.choice(doctors, n_patients)

# Medications
medications_list = [
    'Metformin', 'Lisinopril', 'Atorvastatin', 'Albuterol', 'Omeprazole',
    'Metoprolol', 'Losartan', 'Gabapentin', 'Hydrochlorothiazide', 'Levothyroxine'
]
medications = np.random.choice(medications_list, n_patients)

# Test results (simplified - normal, abnormal, critical)
test_results = np.random.choice(['Normal', 'Abnormal', 'Critical'], 
                               n_patients, p=[0.60, 0.30, 0.10])

# Insurance providers
insurance_providers = np.random.choice(['Blue Cross', 'United Health', 'Medicare', 
                                       'Medicaid', 'Aetna', 'Cigna'], n_patients)

# Billing amounts (in USD) - influenced by length of stay, condition, and admission type
base_billing = np.random.uniform(5000, 25000, n_patients)
billing_amounts = []
for i in range(n_patients):
    bill = base_billing[i]
    bill += los[i] * np.random.uniform(500, 1500)  # Daily charges
    
    if admission_types[i] == 'Emergency':
        bill *= 1.3  # Emergency premium
    
    if medical_conditions[i] in ['Cancer', 'Heart Disease', 'Kidney Disease']:
        bill *= 1.5  # Complex condition multiplier
    
    if test_results[i] == 'Critical':
        bill *= 1.2  # Additional tests/treatments
    
    billing_amounts.append(round(bill, 2))

# Room numbers
room_numbers = [f"{floor}{str(room).zfill(2)}" 
               for floor, room in zip(np.random.randint(1, 6, n_patients),
                                     np.random.randint(1, 51, n_patients))]

# Create DataFrame
df = pd.DataFrame({
    'Patient_ID': patient_ids,
    'Name': names,
    'Age': ages,
    'Gender': genders,
    'Blood_Type': blood_types,
    'Medical_Condition': medical_conditions,
    'Admission_Type': admission_types,
    'Admission_Date': admission_dates,
    'Discharge_Date': discharge_dates,
    'Length_of_Stay': los,
    'Doctor': assigned_doctors,
    'Medication': medications,
    'Test_Results': test_results,
    'Insurance_Provider': insurance_providers,
    'Billing_Amount': billing_amounts,
    'Room_Number': room_numbers
})

# Save to CSV
df.to_csv('healthcare_data.csv', index=False)
print(f"Healthcare dataset created successfully!")
print(f"Total records: {len(df)}")
print(f"Total variables: {len(df.columns)}")
print(f"\nDataset preview:")
print(df.head())
print(f"\nDataset info:")
print(df.info())
