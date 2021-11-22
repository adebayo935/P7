import pandas as pd
import csv
import operator

file = []
f = open(r"C:\Users\33676\Desktop\Taff\P7/dataset1_Python+P7 - Copie.csv")
myReader = csv.reader(f)
length = 0
for row in myReader:
    length += 1
    file.append(row)

actions = {'Name': [file[i][0] for i in range(1, length - 1)],
           'Cost': [float(file[i][1]) for i in range(1, length - 1)],
           'Profit': [float(file[i][2]) for i in range(1, length - 1)]}

df_actions = pd.DataFrame(actions, columns=['Name', 'Cost', 'Profit'])

print(df_actions)
print(df_actions['Profit'].max())
print(df_actions.iloc[0]['Name'])
print(df_actions.iloc[0])
print(df_actions.iloc[0]['Cost'])

account = 500
n = length - 1

tab_numb = pd.Series([i for i in range(2 ** n)])
tab_binary = pd.Series([bin(i)[2:] for i in tab_numb])
combinations = pd.Series(['0' * (n - len(k)) + k for k in tab_binary])
s = 0
combinations_valid = {}
for combination in combinations:
    cost_combi = 0
    profit_combi = 0
    for p in range(n):
        if combination[p] == "1":
            cost_combi += df_actions.iloc[p]['Cost']
            profit_combi += df_actions.iloc[p]['Profit']
    if account >= cost_combi:
        combinations_valid = {
            'Code': combination,
            'Cost': cost_combi,
            'Profit': profit_combi
        }

combinations_valid_sorted = sorted(combinations_valid, key=operator.itemgetter(2), reverse=True)

df_combinations_valid = pd.DataFrame(combinations_valid_sorted, columns=['Code', 'Cost', 'Profit'])

entry = input("Afficher combien de résultats ?")

print(df_combinations_valid)

best_one = df_combinations_valid[(df_combinations_valid['Profit'].max())]

for h in range(1, len(df_combinations_valid)):
    if df_combinations_valid.iloc[h]['Profit'] >= best_one.profit and df_combinations_valid.iloc[h]['Cost'] < \
            best_one.cost:
        best_one = df_combinations_valid.iloc[h]

print("The best solution is: " + str(best_one.code) + " " + str(best_one.cost) + " " + str(best_one.profit))
