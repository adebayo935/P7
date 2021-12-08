import csv


file = []
f = open(r"C:\Users\33676\Desktop\Taff\P7/dataset2_Python+P7.csv")
myReader = csv.reader(f)
account = 500

actions = []
length = 0
for row in myReader: # O(n)
    length += 1
    file.append(row)

for i in range(1, length-1): # O(n)
    if float(file[i][1]) < 0 or float(file[i][2]) < 0:
        continue
    else:
        actions.append((file[i][0], int(round(float(file[i][1]), 0)), int(round(float(file[i][2]), 0))))


def solution(account, actions):
    results = [[0 for x in range(account+1)] for x in range(len(actions)+1)]

    for o in range(1, len(actions)+1):
        for w in range(1, account+1):
            if actions[o-1][1] <= w:
                results[o][w] = max(actions[o-1][2]+results[o-1][w-actions[o-1][1]], results[o-1][w])
            else:
                results[o][w] = results[o-1][w]

    w = account
    n = len(actions)
    combination = []

    while w >= 0 and n >= 0:
        e = actions[n-1]
        if results[n][w] == results[n-1][w-e[1]] + e[2]:
            combination.append(e)
            w -= e[1]
        n -= 1

    total_cost = 0
    for action in combination:
        total_cost += action[1]

    return results[-1][-1], combination,total_cost


solution = solution(account, actions)
print("Valeur bénéfice maximal : " + str(solution[0]))
print("Valeur coût total : " + str(solution[2]))
print("Liste des actions récupérées :\n" + str(solution[1]))
