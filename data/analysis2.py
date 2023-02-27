# read csv file
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data2 = pd.read_csv("static/data2.csv")
print("CSV read")
# create DataFrame
df = pd.DataFrame(data2)

def print_gender_family_data():
    # maleTotal = df.loc[df['Sex'] == 'm', "Sex"].sum()
    maleTotal = (df['Sex'].value_counts())
    print(maleTotal)
    autismFamily = df[["FamilyASD", "Class"]].describe()
    print(autismFamily)
    age = df.agg(
    {
        "Age": ["min", "max", "median", "mean"]

    }
    )
    print(age)
    score = df.agg(
        {
            "Score": ["min", "max", "median", "mean"]
        }
    )
    print(score)
    
print_gender_family_data()    

def draw_age_bar_chart():
    plt.figure(figsize=(15, 10))
    values, bins, bars = plt.hist(df['Age'], edgecolor='white')
    plt.xlabel("Age at Diagnosis in Months")
    plt.ylabel("Number of Children Diagnosed")
    plt.suptitle('Age Distribution', fontsize=30)
    plt.bar_label(bars, fontsize=20, color='black')
    plt.margins(x=0.01, y=0.1)
    plt.show()

draw_age_bar_chart()

def analyze_family():
    autWithFam = len(df[(df['FamilyASD'] == 'yes') & (df['Class'] == 'Yes')])
    autWithoutFam = len(df[(df['FamilyASD'] == 'no') & (df['Class'] == 'Yes')])
    notAutWithFam = len(df[(df['FamilyASD'] == 'yes') & (df['Class'] == 'No')])
    notAutWithoutFam = len(df[(df['FamilyASD'] == 'no') & (df['Class'] == 'No')])
    print(autWithFam)
    print(autWithoutFam)
    print(notAutWithFam)
    print(notAutWithoutFam)
    totalAut = len(df[(df['Class'] == 'Yes')])
    totalNotAut = len(df[(df['Class'] == 'No')])
    percentAutWithFam = autWithFam / totalAut
    percentNotAutWithFam = notAutWithFam / totalNotAut
    print("Percent autistic with family", percentAutWithFam)
    print("Percent not autistic with family", percentNotAutWithFam)
analyze_family()

def analyze_questions():
    #frequency each queston earned a point
    freq1 = len(df[df['A1'] == 1])
    freq2 = len(df[df['A2'] == 1])
    freq3 = len(df[df['A3'] == 1])
    freq4 = len(df[df['A4'] == 1])
    freq5 = len(df[df['A5'] == 1])
    freq6 = len(df[df['A6'] == 1])
    freq7 = len(df[df['A7'] == 1])
    freq8 = len(df[df['A8'] == 1])
    freq9 = len(df[df['A9'] == 1])
    freq10 = len(df[df['A10'] == 1])
    answerFreqArray = np.array([(freq1, freq2, freq3, freq4, freq5, freq6, freq7, freq8, freq9, freq10)])
    print("Number of times a point was earned on each question: ", answerFreqArray)
    freqLabels = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10']
    #number of times each question earned a point by someone with autism diagnosis
    afreq1 = len(df[df['A1'] == 1]) & len(df[df['Class'] == "Yes"])
    afreq2 = len(df[df['A2'] == 1]) & len(df[df['Class'] == "Yes"])
    afreq3 = len(df[df['A3'] == 1]) & len(df[df['Class'] == "Yes"])
    afreq4 = len(df[df['A4'] == 1]) & len(df[df['Class'] == "Yes"])
    afreq5 = len(df[df['A5'] == 1]) & len(df[df['Class'] == "Yes"])
    afreq6 = len(df[df['A6'] == 1]) & len(df[df['Class'] == "Yes"])
    afreq7 = len(df[df['A7'] == 1]) & len(df[df['Class'] == "Yes"])
    afreq8 = len(df[df['A8'] == 1]) & len(df[df['Class'] == "Yes"])
    afreq9 = len(df[df['A9'] == 1]) & len(df[df['Class'] == "Yes"])
    afreq10 = len(df[df['A10'] == 1]) & len(df[df['Class'] == "Yes"])
    autismFrequencyArray = np.array([(afreq1, afreq2, afreq3, afreq4, afreq5, afreq6, afreq7, afreq8, afreq9, afreq10)])
    print("True positive: ", autismFrequencyArray)
    #number of times each question earned a point by someone without diagnosis
    nafreq1 = len(df[df['A1'] == 1]) & len(df[df['Class'] == "No"])
    nafreq2 = len(df[df['A2'] == 1]) & len(df[df['Class'] == "No"])
    nafreq3 = len(df[df['A3'] == 1]) & len(df[df['Class'] == "No"])
    nafreq4 = len(df[df['A4'] == 1]) & len(df[df['Class'] == "No"])
    nafreq5 = len(df[df['A5'] == 1]) & len(df[df['Class'] == "No"])
    nafreq6 = len(df[df['A6'] == 1]) & len(df[df['Class'] == "No"])
    nafreq7 = len(df[df['A7'] == 1]) & len(df[df['Class'] == "No"])
    nafreq8 = len(df[df['A8'] == 1]) & len(df[df['Class'] == "No"])
    nafreq9 = len(df[df['A9'] == 1]) & len(df[df['Class'] == "No"])
    nafreq10 = len(df[df['A10'] == 1]) & len(df[df['Class'] == "No"])
    nFrequencyArray = np.array(
        [(nafreq1, nafreq2, nafreq3, nafreq4, nafreq5, nafreq6, nafreq7, nafreq8, nafreq9, nafreq10)])
    print("False positive: ", nFrequencyArray)
    #number of times each question did not earn a point from someone with diagnosis
    fnafreq1 = len(df[df['A1'] == 0]) & len(df[df['Class'] == "Yes"])
    fnafreq2 = len(df[df['A2'] == 0]) & len(df[df['Class'] == "Yes"])
    fnafreq3 = len(df[df['A3'] == 0]) & len(df[df['Class'] == "Yes"])
    fnafreq4 = len(df[df['A4'] == 0]) & len(df[df['Class'] == "Yes"])
    fnafreq5 = len(df[df['A5'] == 0]) & len(df[df['Class'] == "Yes"])
    fnafreq6 = len(df[df['A6'] == 0]) & len(df[df['Class'] == "Yes"])
    fnafreq7 = len(df[df['A7'] == 0]) & len(df[df['Class'] == "Yes"])
    fnafreq8 = len(df[df['A8'] == 0]) & len(df[df['Class'] == "Yes"])
    fnafreq9 = len(df[df['A9'] == 0]) & len(df[df['Class'] == "Yes"])
    fnafreq10 = len(df[df['A10'] == 0]) & len(df[df['Class'] == "Yes"])
    fnFrequencyArray = np.array(
        [(fnafreq1, fnafreq2, fnafreq3, fnafreq4, fnafreq5, fnafreq6, fnafreq7, fnafreq8, fnafreq9, fnafreq10)])
    print("False negative: ", fnFrequencyArray)
    #number of times each question did not earn a point by someone without diagnosis
    tnfreq1 = len(df[df['A1'] == 0]) & len(df[df['Class'] == "No"])
    tnfreq2 = len(df[df['A2'] == 0]) & len(df[df['Class'] == "No"])
    tnfreq3 = len(df[df['A3'] == 0]) & len(df[df['Class'] == "No"])
    tnfreq4 = len(df[df['A4'] == 0]) & len(df[df['Class'] == "No"])
    tnfreq5 = len(df[df['A5'] == 0]) & len(df[df['Class'] == "No"])
    tnfreq6 = len(df[df['A6'] == 0]) & len(df[df['Class'] == "No"])
    tnfreq7 = len(df[df['A7'] == 0]) & len(df[df['Class'] == "No"])
    tnfreq8 = len(df[df['A8'] == 0]) & len(df[df['Class'] == "No"])
    tnfreq9 = len(df[df['A9'] == 0]) & len(df[df['Class'] == "No"])
    tnfreq10 = len(df[df['A10'] == 0]) & len(df[df['Class'] == "No"])
    tnFrequencyArray = np.array(
        [(tnfreq1, tnfreq2, tnfreq3, tnfreq4, tnfreq5, tnfreq6, tnfreq7, tnfreq8, tnfreq9, tnfreq10)])
    print("True negative: ", tnFrequencyArray)
    ppv = (100 * (autismFrequencyArray) / (autismFrequencyArray + nFrequencyArray))
    #posititve and negative predictive values
    print("Positive predictive values are: ", ppv)
    npv = (100 * (tnFrequencyArray) / (tnFrequencyArray + fnFrequencyArray))
    print("Negative predictive values: ", npv)
    sens = ((autismFrequencyArray) / (autismFrequencyArray + fnFrequencyArray))
    #sensitivity and specificity
    print("Sensitivity: ", sens)
    spec = ((tnFrequencyArray) / (tnFrequencyArray + nFrequencyArray))
    print("Specificity: ", spec)
    use = sens + spec
    print("Sensitivity + Specificity: ", use)
    #false positive rate
    fpr = (100 * (nFrequencyArray) / (nFrequencyArray + tnFrequencyArray))
    print("False positive rate: ", fpr)
analyze_questions()    


sens = [0.7474, 0.2727, 0.1778, 0.5115, 0.7143, 0.7912, 0.8901, 0.2637, 0.4885, 0.8022]
spec = [0.8308, 0.1753, 0.2108, 0.3333, 1, 0.8037, 0.9877, 0.0061, 0.3333, .7975]

def draw_sens_spec_plot():
    plt.figure()
    plt.grid(True)
    plt.scatter(sens, spec)

    for i in range(len(sens)):
        plt.text(sens[i], spec[i], f'{i + 1}')
    plt.suptitle("Sensitivity and Specificity of Test Questions")
    plt.xlabel("Sensitivity")
    plt.ylabel("Specificity")
    plt.show()
draw_sens_spec_plot()

ppv = [90, 40, 33, 99, 100, 90, 99, 37, 99, 90]
npv = [62, 11, 11, .4, 61, 63, 80, .37, .37, 64]

def draw_ppv_npv_plot():
    plt.figure()
    plt.grid(True)
    plt.scatter(ppv, npv)

    for i in range(len(ppv)):
        plt.text(ppv[i], npv[i], f'{i + 1}')
    plt.suptitle("Positive and Negative Predictive Values of Test Questions")
    plt.xlabel("Positive Predictive Value")
    plt.ylabel("Negative Predictive Value")
    plt.show()

draw_ppv_npv_plot()

def draw_gender_pie():
    male = 735
    female = 319
    labels = ['Male', 'Female']

    # The values of each section of the pie chart
    sizes = [male, female]

    # Plotting the pie chart
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')

    # Adding a title
    plt.suptitle("Autism Gender Distribution")

    # Show the plot
    plt.show()

draw_gender_pie()