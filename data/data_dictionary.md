# Healthcare Data Dictionary

## Dataset Overview
- **Source**: Hospital Management System (2024-2025)
- **Total Records**: 800 patient records
- **Total Variables**: 16
- **Domain**: Healthcare/Hospital Operations

## Variable Definitions

| Variable Name | Data Type | Description | Business Importance |
|--------------|-----------|-------------|---------------------|
| Patient_ID | String | Unique patient identifier (format: PXXXXX) | Patient tracking and record management, ensures data integrity |
| Name | String | Patient name (anonymized for privacy) | Patient identification in reports |
| Age | Integer | Patient age in years (range: 18-85) | Demographics for risk stratification, treatment planning, and healthcare analytics |
| Gender | Categorical | Patient gender (Male/Female) | Demographics for health pattern analysis and resource planning |
| Blood_Type | Categorical | Blood type classification (A+, A-, B+, B-, AB+, AB-, O+, O-) | Critical for emergency preparedness and blood inventory management |
| Medical_Condition | Categorical | Primary medical diagnosis | Essential for treatment planning, resource allocation, and cost estimation |
| Admission_Type | Categorical | Type of hospital admission (Emergency, Elective, Urgent) | Critical for scheduling, resource optimization, and capacity planning |
| Admission_Date | Date | Date when patient was admitted to hospital | Used for length of stay calculation and trend analysis |
| Discharge_Date | Date | Date when patient was discharged from hospital | Turnover rate analysis and bed management |
| Length_of_Stay | Integer | Duration of hospital stay in days | Key efficiency metric for resource utilization and cost analysis |
| Doctor | String | Assigned treating physician | Workload distribution analysis and staffing optimization |
| Medication | String | Primary prescribed medication | Treatment protocol tracking and pharmacy management |
| Test_Results | Categorical | Medical test results category (Normal, Abnormal, Critical) | Quality of care indicator and clinical outcome tracking |
| Insurance_Provider | Categorical | Health insurance provider company | Billing optimization and financial planning |
| Billing_Amount | Float | Total hospital bill in USD | **PRIMARY METRIC**: Revenue analysis, cost optimization, financial forecasting |
| Room_Number | String | Assigned hospital room number (format: Floor + Room) | Bed management and occupancy tracking |

## Key Metrics for Analysis

### Primary Metrics
1. **Billing_Amount**: Main financial metric for revenue analysis
2. **Length_of_Stay**: Operational efficiency indicator
3. **Age**: Demographic variable for patient segmentation

### Categorical Segments
1. **Medical_Condition**: 10 categories (Diabetes, Hypertension, Asthma, Cancer, Arthritis, Obesity, Heart Disease, Kidney Disease, Pneumonia, Flu)
2. **Admission_Type**: 3 categories (Emergency, Elective, Urgent)
3. **Gender**: 2 categories (Male, Female)
4. **Test_Results**: 3 categories (Normal, Abnormal, Critical)
5. **Insurance_Provider**: 6 providers (Blue Cross, United Health, Medicare, Medicaid, Aetna, Cigna)

## Data Quality Notes

- **Missing Values**: 0 (100% complete dataset)
- **Duplicates**: 0 (all records verified unique)
- **Date Range**: January 1, 2024 - December 31, 2025
- **Data Types**: Properly formatted (dates as datetime, numerics as int/float)

## Business Applications

1. **Revenue Optimization**: Analyze billing patterns to identify high-value services
2. **Resource Planning**: Use admission patterns for staffing optimization  
3. **Quality Improvement**: Monitor test results and outcomes by condition  
4. **Cost Reduction**: Identify opportunities to reduce length of stay
5. **Patient Segmentation**: Target interventions based on demographics and conditions
6. **Insurance Negotiation**: Understand payer mix and billing by provider

## Statistical Characteristics

### Billing_Amount Distribution
- Right-skewed distribution indicating some high-cost cases
- Outliers present (complex medical conditions)  
- Strong correlation with Length_of_Stay

### Length_of_Stay Distribution
- Varies significantly by admission type and medical condition
- Emergency admissions show longer stays on average

### Age Distribution
- Near-normal distribution
- Adult patient population (18-85 years)

---

**Created**: January 2026  
**Purpose**: Complex Engineering Activity - Data Analytics  
**Course**: SE-417L Introduction to Data Analytics Lab
