import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('C:/Users/ocn/OneDrive/Desktop/gfg_DA/List of Countries by Sugarcane Production (1).csv')

# DATA WRNGLING 

print(df.describe())
#checking null/missing  value
print(df.isnull().sum())

#there are few missing value so that we can drop
df.dropna(inplace=True)
print(df.isnull().sum())

#displaying all columns
pd.reset_option('max_columns')

#dropping column that is useless durind anlysis
df.drop('Unnamed: 0',axis=1,inplace=True)

#something wrong with dataset as here is dot instead of comma
#to remove this we will replace it with space
# change the value of dataset
df['Production (Tons)'] = df['Production (Tons)'].str.replace('.', '')
df['Production per Person (Kg)'] = df['Production per Person (Kg)'].str.replace('.', '').str.replace(',', '.')
df['Acreage (Hectare)'] = df['Acreage (Hectare)'].str.replace('.', "")
df['Yield (Kg / Hectare)'] = df['Yield (Kg / Hectare)'].str.replace('.','').str.replace(',', '.')


#converting the datatype of columns from object to float
df['Production (Tons)'] = df['Production (Tons)'].astype(float)
df['Production per Person (Kg)'] = df['Production per Person (Kg)'].str.replace('.', '').astype(float)
df['Acreage (Hectare)'] = df['Acreage (Hectare)'].astype(float)
df['Yield (Kg / Hectare)'] = df['Yield (Kg / Hectare)'].str.replace('.','').astype(float)

print(df.dtypes)

# EXPLORATORY DATA ANALYSIS(EDA)
#looking into the data
print(df.head(10))
pd.reset_option('max_column')
print(df.describe())



#hom many countries are producing sugarcane

df['Continent'].value_counts()

print(df['Continent'].value_counts().plot(kind="bar"))
plt.figure(figsize= (10,10))
plt.subplot(2,2,1)
sns.distplot(df['Production (Tons)'])
plt.subplot(2,2,2)
sns.distplot(df['Yield (Kg / Hectare)'])
plt.subplot(2,2,3)
sns.distplot(df['Production per Person (Kg)'])
plt.subplot(2,2,4)
sns.distplot(df['Acreage (Hectare)'])

#using box plot to check the outliers in the dataset
#finding outliers in the dataset
plt.figure(figsize= (10,10))
plt.subplot(2,2,1)
sns.boxplot(df['Production (Tons)'])
plt.subplot(2,2,2)
sns.boxplot(df['Yield (Kg / Hectare)'])
plt.subplot(2,2,3)
sns.boxplot(df['Production per Person (Kg)'])
plt.subplot(2,2,4)
sns.boxplot(df['Acreage (Hectare)'])



#using describe to check the ststs of the numerical data
m=df.describe()
print(m)

# which country produces maximum sugarcane 
# to do that we generate a new dataset
#we are doing bivariate analysis of column country and production(tons)
df_new = df[['Country','Production (Tons)']].set_index('Country')

df_new['production(tons)_percent']=df_new['Production (Tons)']*100/df_new['Production (Tons)'].sum()
plt.subplot(3,1,1)
df_new['production(tons)_percent'].head(10).plot(kind='pie',autopct='%.2f')
plt.subplot(3,1,2)
df_new['Production (Tons)'].head(10).plot(kind="bar")
plt.subplot(3,1,3)
#which country has highest prodction :: Brazil
df_acr = df.sort_values("Acreage (Hectare)",ascending=False)
ax=sns.barplot(data=df_acr.head(10),x="Country",y='Production (Tons)')
plt.show()
#which country has highest yield per hectare::
plt.subplot(1,1,1 )
df_yield = df.sort_values("Yield (Kg / Hectare)",ascending=False)
bx=sns.barplot(data=df_yield.head(10),x="Country",y='Yield (Kg / Hectare)')
plt.show()
df_num= df[['Production (Tons)','Production per Person (Kg)','Acreage (Hectare)','Yield (Kg / Hectare)']]
cor=df_num.corr()
sns.heatmap(cor,annot=True)

#do countries with highest land produce more sugarcane
plt.subplot(1,1,1 )
sns.scatterplot(data=df,x='Acreage (Hectare)',y='Production (Tons)')

#do countries with yield more sugarcane per hectare more sugarcane in total
plt.subplot(1,1,1 )
sns.scatterplot(data=df,x='Yield (Kg / Hectare)',y='Production (Tons)')

#analysis of continent
df_con=df.groupby('Continent').sum()
df_con["number_of_countries"]=df.groupby('Continent').count()['Country']
print(df_con)
    #which country has highest production ? ::South America
plt.subplot(1,1,1 )
df_con['Production (Tons)'].sort_values(ascending=False).plot(kind='bar')

#do number of countries effect the production of sugarcane
plt.subplot(1,1,1 )
con_names=df_con.index.to_list()
sns.lineplot(data=df_con,x='number_of_countries',y="Production (Tons)")
plt.xticks(df_con['number_of_countries'],con_names,rotation=90)
plt.show()

#production distribution by tons
df_con["Production (Tons)"].plot(kind="pie",autopct='%.2f')