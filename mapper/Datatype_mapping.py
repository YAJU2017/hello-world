import pandas as pd

df1 = pd.read_csv("column_info.csv")
df2 = pd.read_csv("data_type_mapper.csv")
x=''

#print(df1)

#print(df2)

#print(df1.set_index('data_type').join(df2.set_index('source_data_type')) )

final_set = pd.merge(df1, df2, left_on='data_type' , right_on='source_data_type')
#final_set['script'] = final_set['column_name'],' ',final_set['target_data_type'], '(' ,
final_set['script'] = final_set['column_name']+' '+ final_set['target_data_type'] +'('+final_set['data_length'].astype(str)+')'

#print(final_set)

#for index,row in final_set.iterrows():
#  row['column_name'],' ',row['target_data_type'], '(' ,row['data_length'], '),'
table_name ='create table abc ( '
final = ' , '.join(final_set.script)
table_end = '  )'
print table_name + final +table_end