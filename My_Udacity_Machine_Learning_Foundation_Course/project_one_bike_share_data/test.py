import pandas as pd
grades_df = pd.DataFrame(
    data={'exam0': ['Sanjeev', "Sankar", "Jethan", "Veeru", "Vara", "Shikha", "Vasavi", None, None, None, None],
          'exam1': [43, 81, 43, 81, 89, 70, 91, 81, 81, 81, 43],
          'exam2': [24, 63, 24, 63, 67, 51, 79, 63, 72, 63, 60],
          'exam3': [15, 610, 17, 630, 670, 510, 790, 620, 720, 905, 600]},
    index=['Andre', 'Barry', 'Chris', 'Dan', 'Emilio',
           'Fred', 'Greta', 'Humbert', 'Ivan', 'James', 'Klaus']
)

#print(grades_df)
# gpby = grades_df.groupby(['exam1', 'exam2'], as_index=False)
# print(type(gpby.count()))
#
# x = gpby.size()
# print(x)
# print(type(x))
# print(x.keys()[3])
# print((x.get_values()))
# print((x.values))
# print((x.data))
# print((x.shape))
# print((x.ndim))
# print((x.tolist()))
#
# #print(gpby.count())
#
# print(x.idxmax())

print(grades_df['exam1'].value_counts().idxmax())

#print(type(gpby.count()))
#print(gpby.head().count(axis=1))
#print(type(gpby.count()))
#print(gpby.count())
#crt = pd.DataFrame(gpby.groups, columns=['exam1', 'exam2'])
#xyz = grades_df.set_index(['exam1', 'exam2']).count(axis=1)
#print(type(xyz),"------")
#print(xyz)
