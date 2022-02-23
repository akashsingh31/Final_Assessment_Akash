import pandas as pd

FILE_PATH = "/Users/akashsingh/akash_assessment/data.xlsx"
# add your file path here
df = pd.read_excel(FILE_PATH , header= None)

df.columns = ['Student_Name' , 'Marks']

df = df.sort_values('Marks' , ascending=False)

writer = pd.ExcelWriter('output.xlsx' , engine='xlsxwriter')

write = df.head(3)
write = write.reset_index(drop = True)
write = write.set_index('Student_Name')
write.to_excel(writer)

writer.save()

print("Writing to file done")