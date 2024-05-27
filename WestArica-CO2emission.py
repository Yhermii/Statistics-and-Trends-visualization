import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import stats
import seaborn as sns

def readcsv(filename):
    """
    Read the CSV file into a DataFrame, setting countries as the index,
    and transpose the DataFrame.
    """
    df_data = pd.read_csv(filename, index_col= "Country Name")
    df_trans = df_data.T
    return df_data,df_trans

filename = "/Users/babayhermi/Downloads/indicator_Data.csv"
df_data,df_trans = readcsv(filename)

# Printing the head of df_data
print(df_data.head())


# Printing the head of df_data
print (df_trans.head())

# Drop columns ("Country Code" and "Series Code") from the dataframe
df_data = df_data.drop(columns= ["Country Code", "Series Code"])

# Printing few of df_data
print(df_data.head())

#rows that should be dropped
drop_row = ["Country Code", "Series Code"]

#drop the selected rows in the transposed dataframe
df_trans = df_trans.drop(drop_row)

#print few of the data
print(df_trans.head())

#checking for NAN values
df_data.isna().sum()

#summary statistics
summ_stat = df_data.describe()
#print the summary statistics
print(summ_stat)

#calculate the skewness of the columns 
skewness = df_data.skew()
#prints the skewness
print(skewness)

#calculate the kurtosis of the columns 
kurtosis = df_data.kurtosis()
#prints the skewness
print(kurtosis)

#Filter the DataFrame to extract rows and make 'Series Name' the 'Population growth (annual %)'
df_pop = df_data[df_data.loc[:, "Series Name"]== "Population growth (annual %)"]
#print the df_pop
print(df_pop.head())

#Filter the DataFrame to extract rows and make 'Series Name' the 'GDP growth (annual %)'
df_gdp = df_data[df_data.loc[:, "Series Name"]== "GDP growth (annual %)"]
#print the df_gdp
print(df_gdp.head())

#Filter the DataFrame to extract rows and make "Urban population growth (annual %)'
df_urbanpop = df_data[df_data.loc[:, "Series Name"]== "Urban population growth (annual %)"]

#print df_urbanpop
print(df_urbanpop.head())

#Filter the DataFrame to extract rows and make 'Rural population growth (annual %)'
df_ruralpop = df_data[df_data.loc[:, "Series Name"]== "Rural population growth (annual %)"]
#print df_ruralpop
print(df_ruralpop.head())

# Selected columns (four year interval ) ('2001', '2004', '2008','2012' '2016', '2020') from df_pop
df_pop = df_pop.loc[:, ['2001','2004','2008','2012', '2016','2020']]

# Setting the figure size
plt.figure(figsize= (10,10))
#bar plot using df_pop data
df_pop.plot(kind = "bar",title = "Population growth in 4yrs interval")
#Adding a legend, with it position outside the plot area
plt.legend(title = "Years" , loc = "upper left", bbox_to_anchor=(1.05, 1))
# Save figure as a PNG file  "population.png", bboc tight for the outer lenged to be fitted 
plt.savefig('population.png', bbox_inches='tight')  
plt.show()

# Filter df_data to extract rows where 'Series Name' is 'CO2 emissions (kt)'
df_coemiss = df_data[df_data.loc[:, "Series Name"]== "CO2 emissions (kt)"]
# Transpose the DataFrame, slicing the first column
df_coemiss = df_coemiss.iloc[:, 1:].T
#print few df_coemiss data
print(df_coemiss.head())

#set the figure size to default
plt.figure()
plotco = df_coemiss.plot(title = "CO2 emissions (kt)", xlabel ="year")
# Get the twelve line in the plot
line = plotco.findobj(plt.Line2D)[12]  
# Set line style to dashed ('--')for the twelve plot due to similar colors
line.set_linestyle('--') 

plt.legend (title = "Country",loc = "upper left", bbox_to_anchor=(1.05, 1))
# Save figure as a PNG file  "coemiss.png", bboc tight for the outer lenged to be fitted 
plt.savefig('coemiss.png', bbox_inches='tight')  # Save the figure
plt.show()

# Selected columns (four year interval ) ('2001', '2004', '2008','2012' '2016', '2020') from df_urbanpop
df_urbanpop = df_urbanpop.loc[:, ['2001','2004','2008','2012', '2016','2020']]

#set the figure size 
plt.figure(figsize= (10,10))
#bar plot using df_urbanpop data
df_urbanpop.plot(kind = "bar",title = "Urban population growth in 4yrs interval")
#setting the legend 
plt.legend(loc = "upper left", bbox_to_anchor=(1.05, 1))
# Save figure as a PNG file  "urbanpop.png", bboc tight for the outer lenged to be fitted 
plt.savefig('urbanpop.png', bbox_inches='tight')  # Save the figure
plt.show()


# Selected columns (four year interval ) ('2001', '2004', '2008','2012' '2016', '2020') from df_ruralpop
df_ruralpop = df_ruralpop.loc[:, ['2001','2004','2008','2012','2016','2020']]

#set figure size to default 
plt.figure()
#bar plot using df_ruralpop data
df_ruralpop.plot(kind = "bar",title = "Rural population growth in 4yrs interval", xlabel = "Country")
#set the legends 
plt.legend (title = "year",loc = "upper left", bbox_to_anchor=(1.05, 1))
# Save figure as a PNG file  "ruralpop.png", bboc tight for the outer lenged to be fitted 
plt.savefig('ruralpop.png', bbox_inches='tight')  # Save the figure
plt.show()

# Extracting the data for Nigeria from the DataFrame and set 'Series Name' as index
df_nigeria = df_data.loc['Nigeria'].set_index('Series Name')
# Transpose the DataFrame for indicators to be columns and years to be  rows
df_nigeria = df_nigeria.T
# Print  DataFrame of Nigeria data
print(df_nigeria)

# Calculate the correlation matrix for Nigeria data
correlation_matrix_nigeria = df_nigeria.corr()

# Set fig size
plt.figure(figsize=(8, 6))

# Create heatmap with seaborn for Nigeria data
sns.heatmap(correlation_matrix_nigeria, annot=True, cmap='coolwarm', fmt=".2f")

# set title
plt.title('Correlation Heatmap for Nigeria (Series)')

plt.savefig('ngheatmap.png', bbox_inches='tight')  # Save the figure

# Show plot
plt.show()

# Extracting the data for Sierra Leone from the DataFrame and set 'Series Name' as index
df_sl = df_data.loc['Sierra Leone'].set_index('Series Name')
# Transpose the DataFrame for indicators to be columns and years to be  rows
df_sl = df_sl.T
#Print  DataFrame of Sierra Leone data
print(df_sl)

# Calculate the correlation matrix for Sierra Leone data
correlation_matrix_sl = df_sl.corr()

# Set figure size
plt.figure(figsize=(8, 6))

# Create heatmap using seaborn for Sierra Leone data
sns.heatmap(correlation_matrix_sl, annot=True, cmap='coolwarm', fmt=".2f")

# set title
plt.title('Correlation Heatmap for Sierra Leone (Series)')

plt.savefig('slheatmap.png', bbox_inches='tight')  # Save the figure
# Show plot
plt.show()


