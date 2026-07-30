import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


if 'df' not in st.session_state:
    st.session_state.df = pd.read_csv("Train.csv")

df = st.session_state.df 

st.set_page_config(page_title="Income Prediction Explorer", layout="wide")


st.sidebar.header("Choose a Function")

buttons = [
    "Read Rows", "DataFrame Info", "Describe Data", "Check Duplicates",
    "Null Check", "Column Names", "Drop Columns", "Remove Space",
    "Replace '?' with NaN", "Fill Missing Values", "Replace Marital Status",
    "Income Distribution", "Income vs Gender", "Income vs Marital Status",
    "Income vs Gender & Marital Status", "Education Distribution",
    "Education vs Gender & Age", "Age vs Gender & Marital Status",
    "Employment Commitment", "Age Histogram", "Old Residence Reg",
    "Importance of Record", "Gains & Losses"
]

selected = st.sidebar.radio("Select Operation", buttons)


if selected == "Read Rows":
    st.title("Income Prediction Data Explorer")
    row_count = st.number_input("Enter number of rows", 5, 100, 10)
    st.dataframe(df.head(row_count))

elif selected == "DataFrame Info":
    info_df = pd.DataFrame({
        "Column": df.columns,
        "Non-Null Count": df.notnull().sum(),
        "Dtype": df.dtypes
    }).reset_index(drop=True)
    st.dataframe(info_df)
    st.write(f"Rows: {len(df)}, Columns: {len(df.columns)}")

elif selected == "Describe Data":
    st.dataframe(df.describe())

elif selected == "Check Duplicates":
    dup = df.duplicated().sum()
    st.write(f"Total duplicate rows: **{dup}**")

elif selected == "Null Check":
    st.dataframe(df.isnull().sum().to_frame(name="Missing Values"))

elif selected == "Column Names":
    st.write(f"Total Columns: **{len(df.columns)}**")
    st.dataframe(pd.DataFrame(df.columns, columns=["Column Names"]))

elif selected == "Drop Columns":
    cols_to_drop = [
        'race', 'is_labor_union', 'country_of_birth_father',
        'veterans_admin_questionnaire', 'country_of_birth_mother',
        'migration_prev_sunbelt', 'migration_code_move_within_reg',
        'migration_code_change_in_reg', 'migration_code_change_in_msa',
        'old_residence_state'
    ]
    
    existing_cols = [col for col in cols_to_drop if col in df.columns]

    df.drop(columns=existing_cols, inplace=True)

    st.success("Unnecessary columns dropped.")
    
    st.markdown("### Dropped Columns:")
    st.write(existing_cols if existing_cols else "No matching columns found in the dataset.")

elif selected == "Remove Space":
    for col in df.select_dtypes(include='object'):
        df[col] = df[col].str.strip()
    st.success("Whitespace removed from object columns.")

elif selected == "Replace '?' with NaN":
    quest_mark = (df == '?').sum()
    df.replace('?', np.nan, inplace=True)
    st.dataframe(quest_mark.to_frame(name="Question Mark Count"))

elif selected == "Fill Missing Values":
    try:
        df['education_institute'] = df.groupby('education')['education_institute'].transform(lambda x: x.fillna(x.mode()[0]) if not x.mode().empty else 'High school graduate')
        df['class'] = df.groupby('education')['class'].transform(lambda x: x.fillna(x.mode()[0]) if not x.mode().empty else 'High school graduate')
        df['unemployment_reason'] = df.groupby('employment_commitment')['unemployment_reason'].transform(lambda x: x.fillna(x.mode()[0]) if not x.mode().empty else 'Children or Armed Forces')
        df['occupation_code_main'] = df.groupby('occupation_code')['occupation_code_main'].transform(lambda x: x.fillna(x.mode()[0]) if not x.mode().empty else 'Adm support including clerical')
        df['under_18_family'] = df.groupby('household_summary')['under_18_family'].transform(lambda x: x.fillna(x.mode()[0]) if not x.mode().empty else 'Both parents present')
        df['country_of_birth_own'] = df.groupby('citizenship')['country_of_birth_own'].transform(lambda x: x.fillna(x.mode()[0]) if not x.mode().empty else "US")
        df['old_residence_reg'] = df.groupby('country_of_birth_own')['old_residence_reg'].transform(lambda x: x.fillna(x.mode()[0]) if not x.mode().empty else 'US')
        df['residence_1_year_ago'] = df.groupby('old_residence_reg')['residence_1_year_ago'].transform(lambda x: x.fillna(x.mode()[0]) if not x.mode().empty else 'Same')
        
        st.success("Missing values filled using grouped mode.")
        st.markdown("### ✅ Columns where missing values were filled:")
        st.write(["education_institute", "class", "unemployment_reason", "occupation_code_main", "under_18_family", "country_of_birth_own", "old_residence_reg", "residence_1_year_ago"])
    except Exception as e:
        st.error(f"Error: {e}")

elif selected == "Replace Marital Status":
    df['marital_status'] = df['marital_status'].replace({
        'Widowed': 'married',
        'Married-civilian spouse present': 'married',
        'Married-A F spouse present': 'married',
        'Never married': 'single',
        'Divorced': 'single',
        'Married-spouse absent': 'single',
        'Separated': 'single',
    })

    df['citizenship'] = df['citizenship'].replace({
        'Native': 'Native',
        'Native- Born in Puerto Rico or U S Outlying': 'Native',
        'Native- Born abroad of American Parent(s)': 'Native',
        'Foreign born- Not a citizen of U S': 'Foreign',
        'Foreign born- U S citizen by naturalization': 'Naturalized'
    })

    st.success("Marital status and citizenship normalized.")
    



elif selected == "Income Distribution":
    st.markdown("<h4>This plot shows the number of above limit and below limit.</h4>",unsafe_allow_html=True)
    
    x = df['income_above_limit'].unique()
    y = df['income_above_limit'].value_counts()
    income = df.groupby('income_above_limit')['income_above_limit'].value_counts()
    st.dataframe(income)
    plt.figure(figsize=(8,8))
   
    fig, ax = plt.subplots()
    plt.bar(x,y,color=["lightblue", "coral"],data=df,label=['Below limit','Above limit'])
    plt.title('Income Class',fontsize=20)
    plt.xlabel('Income Limit',fontsize=15)
    plt.ylabel('Count',fontsize=15)
    plt.legend(loc=1)
    st.pyplot(fig)

elif selected == "Income vs Gender":
    st.markdown("<h4>This Plot shows the number of Upper and Lower Limits in Women and the number of Upper and Lower Limits in Men.</h4>",unsafe_allow_html=True)

    gender = df.groupby('gender')['income_above_limit'].value_counts()
    st.dataframe(gender)
    fig, ax = plt.subplots()
    sns.countplot(x='gender', hue='income_above_limit',palette=['lightblue', 'lightgrey'], data=df)
    plt.title('Income Class with Gender',fontsize=20)
    plt.xlabel('gender',fontsize=15)
    plt.ylabel('Count',fontsize=15)
    st.pyplot(fig)

elif selected == "Income vs Marital Status":
    st.markdown("<h4>This Plot shows the number of Upper and Lower Limits in Married and the number of Upper and Lower Limits in Single.</h4>",unsafe_allow_html=True)
    marr= df.groupby('marital_status')['income_above_limit'].value_counts()
    st.dataframe(marr)
    fig, ax = plt.subplots(figsize=(12,6))
    sns.countplot(x='marital_status', hue='income_above_limit', data=df)
    plt.xticks(rotation=45)
    st.pyplot(fig)

elif selected == "Income vs Gender & Marital Status":
    st.markdown("<h4>This plot shows the percentage of Above limit and Below limit of the column containing incom_above_limit.</h4>",unsafe_allow_html=True)
    inc = df.groupby('income_above_limit')['income_above_limit'].value_counts()
    st.dataframe(inc)
    st.markdown("<h4>This plot shows the percentage of male and female of the column containing gender.</h4>",unsafe_allow_html=True)
    gndr = df.groupby('gender')['gender'].value_counts()
    st.dataframe(gndr)
    st.markdown("<h4>This plot shows the percentage of married and single of the column containing marital_status.</h4>",unsafe_allow_html=True)
    mar = df.groupby('marital_status')['marital_status'].value_counts()
    st.dataframe(mar)
    fig, axs = plt.subplots(1, 3, figsize=(20, 6))
    e= [0.05, 0]
    
    income = df['income_above_limit'].unique()
    income_val = df['income_above_limit'].value_counts()
    axs[0].pie(income_val, labels=income,explode=e, autopct='%0.2f%%', shadow=True, startangle=30, colors=['SkyBlue','HotPink'])
    axs[0].set_title('Income Class Percentage')

    gender = df['gender'].unique()
    gender_val = df['gender'].value_counts()
    axs[1].pie(gender_val, labels=gender, explode=e, autopct='%0.2f%%', shadow=True, startangle=30, colors=['Tomato','lightblue'])
    axs[1].set_title('Gender Class Percentage')

    marriad = df['marital_status'].unique()
    marriad_val = df['marital_status'].value_counts()
    axs[2].pie(marriad_val, labels=marriad,explode=e, autopct='%0.2f%%', shadow=True, startangle=30, colors=['lightgrey','orange'])
    axs[2].set_title('Marital Status Percentage')

    st.pyplot(fig)

elif selected == "Education Distribution":
    st.markdown("<h4>This plot shows the values of the education column in terms of courses.</h4>",unsafe_allow_html=True)
  
    edu = df.groupby('education')['education'].value_counts()
    st.dataframe(edu)
    fig, ax = plt.subplots(figsize=(10,6))

    x = df['education'].value_counts().index
    y = df['education'].value_counts().values

    sns.barplot(x=x, y=y, palette='plasma', ax=ax)

    ax.set_title('Education Info', fontsize=20)
    ax.set_xlabel('Education', fontsize=15)
    ax.set_ylabel('Count', fontsize=15)
    plt.xticks(rotation=60, ha='right')
    
    for bars in ax.containers:
         ax.bar_label(bars)
    st.pyplot(fig)

elif selected == "Education vs Gender & Age":
    st.markdown("<h4>This plot shows the average age of female and male with of education.</h4>",unsafe_allow_html=True)
    
    edu_age = df.groupby(['education','gender'])['age'].mean()
    st.dataframe(edu_age)
    fig, ax = plt.subplots(figsize=(14,6))
    sns.barplot(x='education',y='age',data=df,hue='gender',width=0.9,palette='cool')
    plt.xlabel('Educatin',fontsize=15)
    plt.ylabel('Age',fontsize=15)
    plt.title('Education by Gender with Age',fontsize=20)
    plt.xticks(rotation=60,ha='right')
    st.pyplot(fig)

elif selected == "Age vs Gender & Marital Status":
    st.markdown("<h4>This both different via plot shows the number of married and single males and the mean of married and single females.</h4>",unsafe_allow_html=True)
    
    age_mean = df.groupby(['gender','marital_status'])['age'].mean()
    st.dataframe(age_mean)
    fig, axs = plt.subplots(1, 2, figsize=(16,6))
    sns.barplot(x='gender',y='age',hue='marital_status',data=df,palette="hot",estimator='mean',capsize=0.1,errorbar=('ci', 100), ax=axs[0])
    axs[0].set_title('marital_status',fontsize=20)

    # plt.subplot(1,2,2)
    axs[1].set_title('Marital Status - Age Distribution by Gender', fontsize=20)
    sns.boxplot(x='gender',y='age',hue='marital_status',data=df,palette="plasma",orient='vertical',ax = axs[1])
    st.pyplot(fig)

elif selected == "Employment Commitment":
    st.markdown("<h4>This plot shows the average of female and male with the values of employment_commitment.</h4>",unsafe_allow_html=True)

    employ_commit = df.groupby(['employment_commitment','gender'])['age'].mean()
    st.dataframe(employ_commit)
    fig, ax = plt.subplots(figsize=(12,6))
    sns.barplot(x='employment_commitment',y='age',hue='gender',data=df,palette=['lightblue','Tomato'])
    plt.title('employment_commitment',fontsize=20)
    plt.xlabel('employment_commitment',fontsize=15)
    plt.ylabel('age',fontsize=15)
    plt.xticks(rotation=60,ha='right')
    st.pyplot(fig)

elif selected == "Age Histogram":
    st.markdown("<h4>This plot show the number based on the continued values of the age.</h4>",unsafe_allow_html=True)
   
    agg = df.groupby('age')['age'].agg(['min','max','mean'])
    st.dataframe(agg)
    fig, ax = plt.subplots()
    sns.histplot(df['age'],binwidth=5,kde=True)
    plt.title('Age Count',fontsize=20)
    plt.xlabel('Age',fontsize=13)
    plt.ylabel('count',fontsize=13)
    plt.xticks(np.arange(0,91,5))
    st.pyplot(fig)

elif selected == "Old Residence Reg":
    st.markdown("<h4>This plot shows that the shows age according to old_residence_state based on male and female.</h4>",unsafe_allow_html=True)
 
    state = df.groupby(['old_residence_reg','gender'])['age'].mean()
    st.dataframe(state)
    
    fig, ax = plt.subplots(figsize=(18,6))
    sns.barplot(x='old_residence_reg',y='age',hue='gender',data=df)
    plt.title('old_residence_rege with gender and age',fontsize=20)
    plt.xlabel('old_residence_reg',fontsize=15)
    plt.ylabel('age',fontsize=15)
    plt.xticks(rotation=90)
    st.pyplot(fig)

elif selected == "Importance of Record":
    st.markdown("<h4>This plot shows how many importance records there are by age, based on the above limit and below limit, for males and females.</h4>",unsafe_allow_html=True)
    
    record = df.groupby(['age','gender','income_above_limit'])['importance_of_record'].sum()
    st.dataframe(record)
    fig, ax = plt.subplots(figsize=(12,10))
    sns.scatterplot(x='age',y='importance_of_record',hue='income_above_limit',style='gender',data=df, size='importance_of_record', sizes=(40, 400),alpha=0.8)
    plt.xticks(np.arange(0,91,5))
    plt.yticks(np.arange(0,20001,2000))
    plt.title('Income_Above_Limit with Age And Gender',fontsize = 20)
    plt.xlabel('age',fontsize = 15)
    plt.ylabel('importance_of_record',fontsize = 15)
    st.pyplot(fig)
    

elif selected == "Gains & Losses":
    st.markdown("<h4>This plot shows the different between the Gains and Loss</h4>",unsafe_allow_html=True)
    gl = pd.DataFrame({"Gains & Losses ": ['Gains', 'Losses'] , "Total Amount": [df['gains'].sum(),df['losses'].sum()]})
    st.dataframe(gl)
    fig, ax = plt.subplots(figsize=(10, 6))

    gains = df['gains'].sum()
    losses = df['losses'].sum()
    values = [gains, losses]
    labels = ['Gains', 'Loss'] 

    sns.set(style='darkgrid')
    ax.bar(labels, values, color=["lightblue", "coral"])
    ax.set_title('Gains & Loss', fontsize=20)
    ax.set_ylabel('Total Amount', fontsize=15)

    st.pyplot(fig)
