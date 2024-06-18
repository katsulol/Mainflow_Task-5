import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("heart.csv")

#What percentage of patients in the dataset have chest pain (cp > 0)?
#Is there a relationship between resting blood pressure (trestbps) and the presence of exercise-induced angina (exang)?
#How does the distribution of the number of major vessels (ca) differ between patients with and without heart disease (target)?
#Are there any potential outliers in the maximum heart rate (thalach) data?
#What is the correlation between the sex and the heart disease presence?

print("Missing values summary:")
#print(df.isnull())

#Explore the percentage of patients with chest pain (cp > 0)
cp = sum(df['cp'] > 0) / len(df) * 100
print(f"Percentage of Patients with Chest Pain: {int(cp)}%")


#Analyze the relationship between resting blood pressure and exercise-induced angina
sns.boxplot(x = "exang", y = "trestbps", data=df)
plt.xlabel('Exercise-induced Angina (exang)')
plt.ylabel('Resting Blood Pressure (trestbps)')
plt.title('Resting Blood Pressure by Exercise-induced Angina')
plt.show()

#Analyze the distribution of the number of major vessels (ca) across target groups
sns.countplot(x = "ca", hue="target", data=df)
plt.xlabel('Number of Major Vessels (ca)')
plt.ylabel('Count')
plt.title('Number of Major Vessels Distribution by Heart Disease Presence')
plt.show()


#Identify potential outliers in a specific feature (replace 'thalach' with your desired feature)
sns.boxplot(df['thalach'])
plt.title('Distribution of Maximum Heart Rate (thalach) with Potential Outliers')
plt.show()


#What is the correlation between the sex and the heart disease presence?
plt.scatter(df['sex'], df['target'])
plt.xlabel('Sex (1: Male, 0: Female)')
plt.ylabel('Heart Disease Presence (1: Yes, 0: No)')
plt.title('Correlation Between Sex and Heart Disease Presence')
plt.show()

