#
# from pyspark.sql import SparkSession
#
# spark = SparkSession\
#         .builder\
#         .appName("project")\
#         .getOrCreate()
#
# my_data = [(1, 1),
#  (1,  2),
#  (5,  3),
#  (2,  1),
#  (2,  4)]
#
# my_schema = ['id', 'rank']
#
# df = spark.createDataFrame(data=my_data, schema=my_schema)
#
# print("DataFrame content:")
# df.show()

import pandas as pd

# Create a DataFrame with the given data
data = {
    'id': [1, 2, 3, 4, 5],
    'name': ['Manish', 'Nikita', 'Pritam', 'Prantosh', 'Vikash'],
    'age': [26, 23, 22, 17, 31],
    'salary': [75000, 100000, 150000, 200000, 300000],
    'address': ['bihar', 'uttarpradesh', 'Bangalore', 'Kolkata', None],
    'nominee': ['nominee1', 'nominee2', 'India', 'India', 'nominee5']
}

df = pd.DataFrame(data)

# Convert the DataFrame to a CSV file
df.to_csv('employeeData.csv', index=False)

print("DataFrame converted to CSV successfully.")


