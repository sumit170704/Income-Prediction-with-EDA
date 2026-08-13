import streamlit as st
import pickle 
import numpy as np

# Load models and scaler

#model = pickle.load(open(f'rendam_model.pkl','rb'))
from huggingface_hub import hf_hub_download
import pickle

model_path = hf_hub_download(
    repo_id="sumit1707/income-prediction-model",
    filename="rendam_model.pkl"
)

with open(model_path, "rb") as f:
    model = pickle.load(f)
scaler = pickle.load(open(f'randam_scaler.pkl','rb'))

# Category lists
education = ['Select'] + ['1st 2nd 3rd or 4th grade', '10th grade', '11th grade', '12th grade no diploma', 
             '5th or 6th grade', '7th and 8th grade', '9th grade', 'Associates degree-academic program', 
             'Associates degree-occup /vocational', 'Bachelors degree(BA AB BS)', 'Children', 
             'Doctorate degree(PhD EdD)', 'High school graduate', 'Less than 1st grade', 
             'Masters degree(MA MS MEng MEd MSW MBA)', 'Prof school degree (MD DDS DVM LLB JD)', 
             'Some college but no degree']

class_worker = ['Select'] + ['Federal government', 'Local government', 
                   'Never worked', 'Private', 'Self-employed-incorporated', 
                   'Self-employed-not incorporated', 'State government', 'Without pay']

education_institute = ['Select'] + ['College or university', 'High school']

employment_commitment = ['Select'] + ['Children or Armed Forces', 'Full-time schedules', 'Not in labor force', 
                         'PT for econ reasons usually FT', 'PT for econ reasons usually PT', 
                         'PT for non-econ reasons usually FT', 'Unemployed full-time', 
                         'Unemployed part- time']

unemployment_reason = ['Select'] + ['Job leaver', 'Job loser - on layoff', 
                       'New entrant', 'Other job loser', 'Re-entrant']

industry_code_main = ['Select'] + ['Agriculture', 'Armed Forces', 'Business and repair services', 'Communications', 
                 'Construction', 'Education', 'Entertainment', 'Finance insurance and real estate', 
                 'Forestry and fisheries', 'Hospital services', 'Manufacturing-durable goods', 
                 'Manufacturing-nondurable goods', 'Medical except hospital', 'Mining', 
                 'Not in universe or children', 'Other professional services', 
                 'Personal services except private HH', 'Private household services', 
                 'Public administration', 'Retail trade', 'Social services', 'Transportation', 
                 'Utilities and sanitary services', 'Wholesale trade']

occupation_code_main = ['Select'] + ['Adm support including clerical', 'Armed Forces', 
                   'Executive admin and managerial', 'Farming forestry and fishing', 
                   'Handlers equip cleaners etc', 'Machine operators assmblrs & inspctrs', 
                   'Other service', 'Precision production craft & repair', 
                   'Private household services', 'Professional specialty', 
                   'Protective services', 'Sales', 'Technicians and related support', 
                   'Transportation and material moving']

household_stat = ['Select'] + ['Child <18 ever marr RP of subfamily',
                    'Child <18 ever marr not in subfamily',
                    'Child <18 never marr RP of subfamily',
                    'Child <18 never marr not in subfamily',
                    'Child <18 spouse of subfamily RP',
                    'Child 18+ ever marr Not in a subfamily',
                    'Child 18+ ever marr RP of subfamily',
                    'Child 18+ never marr Not in a subfamily',
                    'Child 18+ never marr RP of subfamily',
                    'Child 18+ spouse of subfamily RP',
                    'Child under 18 of RP of unrel subfamily',
                    'Grandchild <18 ever marr not in subfamily',
                    'Grandchild <18 never marr RP of subfamily',
                    'Grandchild <18 never marr RP of subfamily'
                    'Grandchild <18 never marr child of subfamily RP',
                    'Grandchild 18+ ever marr RP of subfamily',
                    'Grandchild 18+ ever marr not in subfamily',
                    'Grandchild 18+ never marr RP of subfamily',
                    'Grandchild 18+ never marr not in subfamily',
                    'Grandchild 18+ spouse of subfamily RP',
                    'Householder',
                    'In group quarters',
                    'Nonfamily householder',
                    'Other Rel <18 ever marr RP of subfamily',
                    'Other Rel <18 ever marr not in subfamily',
                    'Other Rel <18 never married RP of subfamily',
                    'Other Rel <18 never marr not in subfamily',
                    'Other Rel <18 spouse of subfamily RP',
                    'Other Rel 18+ ever marr RP of subfamily',
                    'Other Rel 18+ ever marr not in subfamily',
                    'Other Rel 18+ never marr RP of subfamily',
                    'Other Rel 18+ never marr not in subfamily',
                    'Other Rel 18+ spouse of subfamily RP',
                    'RP of unrelated subfamily',
                    'Secondary individual',
                    'Spouse of RP of unrelated subfamily',
                    'Spouse of householder']

household_summary = ['Select'] + ['Child 18 or older',
                     'Child under 18 ever married',
                     'Child under 18 never married',
                     'Group Quarters- Secondary individual',
                     'Householder',
                     'Nonrelative of householder',
                     'Other relative of householder',
                     'Spouse of householder']

under_18_family = ['Select'] + ['Both parents present',
                   'Father only present',
                   'Mother only present',
                   'Neither parent present']

tax_status = ['Select'] + ['Head of household',
              'Joint both 65+',
              'Joint both under 65',
              'Joint one under 65 & one 65+',
              'Nonfiler',
              'Single']

citizenship = ['Select'] + ['Foreign', 'Native', 'Naturalized']

country_of_birth_own = ['Select'] + ['Cambodia', 'Canada', 'China', 'Columbia', 'Cuba', 'Dominican-Republic', 
                    'Ecuador', 'El-Salvador', 'England', 'France', 'Germany', 'Greece', 
                    'Guatemala', 'Haiti', 'Holand-Netherlands', 'Honduras', 'HongKong', 
                    'Hungary', 'India', 'Iran', 'Ireland', 'Italy', 'Jamaica', 'Japan', 
                    'Laos', 'Mexico', 'Nicaragua', 'Outlying-U S (Guam USVI etc)', 'Panama', 
                    'Peru', 'Philippines', 'Poland', 'Portugal', 'Puerto-Rico', 'Scotland', 
                    'South Korea', 'Taiwan', 'Thailand', 'Trinadad&Tobago', 'US', 'Vietnam', 
                    'Yugoslavia']

old_residence_reg = ['Select'] + ['Abroad', 'Midwest', 'Northeast', 'South', 'West']

# Mapping
education_map = {v: i for i, v in enumerate(education) if v != 'Select'}
class_worker_map = {v: i for i, v in enumerate(class_worker) if v != 'Select'}
education_institute_map = {v: i for i, v in enumerate(education_institute) if v != 'Select'}
employment_commitment_map = {v: i for i, v in enumerate(employment_commitment) if v != 'Select'}
unemployment_reason_map = {v: i for i, v in enumerate(unemployment_reason) if v != 'Select'}
industry_code_main_map = {v: i for i, v in enumerate(industry_code_main) if v != 'Select'}
occupation_code_main_map = {v: i for i, v in enumerate(occupation_code_main) if v != 'Select'}
household_stat_map = {v: i for i, v in enumerate(household_stat) if v != 'Select'}
household_summary_map = {v: i for i, v in enumerate(household_summary) if v != 'Select'}
under_18_family_map = {v: i for i, v in enumerate(under_18_family) if v != 'Select'}
tax_status_map = {v: i for i, v in enumerate(tax_status) if v != 'Select'}
citizenship_map = {v: i for i, v in enumerate(citizenship) if v != 'Select'}
country_of_birth_own_map = {v: i for i, v in enumerate(country_of_birth_own) if v != 'Select'}
old_residence_reg_map = {v: i for i, v in enumerate(old_residence_reg) if v != 'Select'}

# UI
st.set_page_config(page_title="User Data Form", layout="wide")

st.title("📋 Income Prediction Information Form")

with st.form("income_form"):
    st.subheader("🧑 Personal Information")
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input("Age", min_value=0)
        gender = st.radio("Gender", ["Male", "Female"])
        marital_status = st.radio("Marital Status", ["Single", "Married"])
        
    with col2:
        education = st.selectbox("Education", education, index=0)
        class_worker = st.selectbox("Class of Worker", class_worker, index=0)
        education_institute = st.selectbox("Education Institute", education_institute, index=0)
        
    with col3:
        citizenship = st.selectbox("Citizenship", citizenship, index=0)
        country_of_birth_own = st.selectbox("Country of Birth", country_of_birth_own, index=0)
        mig_year = st.number_input("Migration Year")
    
    st.subheader("💼 Employment Details")
    col4, col5, col6 = st.columns(3)
    with col4:
        
        employment_commitment = st.selectbox("Employment Commitment", employment_commitment, index=0)
        unemployment_reason = st.selectbox("Unemployment Reason", unemployment_reason, index=0)
        
    with col5:
        wage_per_hour = st.number_input("Wage Per Hour", min_value=0)
        working_week_per_year = st.number_input("Working Weeks Per Year", min_value=0)
        total_employed = st.number_input("Total Employed", min_value=0)
    
    with col6:
        
        industry_code_main = st.selectbox("Industry Code", industry_code_main, index=0)
        occupation_code_main = st.selectbox("Occupation Code", occupation_code_main, index=0)
        
    st.subheader("🏡 Household Details")
    col7, col8 = st.columns(2)
    with col7:
        household_stat = st.selectbox("Household Status", household_stat, index=0)
        household_summary = st.selectbox("Household Summary", household_summary, index=0)
        under_18_family = st.selectbox("Under 18 Family", under_18_family, index=0)
        
    with col8:
        tax_status = st.selectbox("Tax Status", tax_status)
        vet_benefit = st.number_input("Veterans Benefit", min_value=0)
        stocks_status = st.number_input("Stocks status")
        
    st.subheader("📦 Other Details")
    col9, col10 = st.columns(2)
    with col9:
        gains = st.number_input("Capital Gains", min_value=0)
        losses = st.number_input("Capital Losses", min_value=0)
        importance_of_record = st.number_input("Importance of Record", min_value=0)
    with col10:
        residence_1_year = st.radio("Residence 1 Year Ago", ["Same", "No"])
        old_residence_reg = st.selectbox("Old Residence Region", old_residence_reg, index=0)
        
   
    submitted = st.form_submit_button("Predict Income")
    
if submitted:
    # Validate that all selectboxes are not left on default "Select"
    if 'Select' in [
        education, class_worker, education_institute, employment_commitment, unemployment_reason,
        industry_code_main, occupation_code_main, household_stat, household_summary,
        under_18_family, tax_status, citizenship, country_of_birth_own, old_residence_reg
    ]:
        st.error("❌ Please make sure to select a valid option in all dropdown menus.")
    else:
        gender = 1 if "Male" in gender else 0
        marital_status = 1 if "Single" in marital_status else 0
        residence_1_year = 1 if "Same" in residence_1_year else 0
        
        input_data = [
            float(age), gender,
            education_map[education],
            class_worker_map[class_worker],
            education_institute_map[education_institute],
            marital_status,
            employment_commitment_map[employment_commitment],
            unemployment_reason_map[unemployment_reason],
            wage_per_hour, working_week_per_year,
            industry_code_main_map[industry_code_main],
            occupation_code_main_map[occupation_code_main],
            float(total_employed),
            household_stat_map[household_stat],
            household_summary_map[household_summary],
            under_18_family_map[under_18_family],
            float(vet_benefit),
            tax_status_map[tax_status],
            float(gains), float(losses), float(stocks_status),
            citizenship_map[citizenship],
            mig_year,
            country_of_birth_own_map[country_of_birth_own],
            residence_1_year,
            old_residence_reg_map[old_residence_reg],
            float(importance_of_record)
        ]
        
        input_np = np.array(input_data).reshape(1, -1)
        scaled_input = scaler.transform(input_np)
        prediction = model.predict(scaled_input)
        
        st.success("✅ Income Prediction: " + ("Above Limit" if prediction[0] == 1 else "Below Limit"))

    
