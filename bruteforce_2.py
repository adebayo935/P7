import csv


class Action:
    def __init__(self, name, cost, profit):
        self.name = name
        self.cost = float(cost)
        self.profit = float(profit)

    def __lt__(self, other):
        return self.profit < other.profit


class Combination:
    def __init__(self, code, cost, profit):
        self.code = code
        self.cost = round(cost, 2)
        self.profit = round(profit, 2)

    def __lt__(self, other):
        return self.profit < other.profit


file = []
f = open(r"C:\Users\33676\Desktop\Taff\P7/dataset1_Python+P7 - Copie (2).csv")
myReader = csv.reader(f)
account = 500


def make_actions(myReader):
    actions = []
    length = 0
    for row in myReader: # O(n)
        length += 1
        file.append(row)

    for i in range(1, length-1): # O(n)
        actions.append(Action(file[i][0], file[i][1], file[i][2]))
    return actions


def combi_valid(actions, account):
    n = len(actions)
    tab_numb = [i for i in range(2 ** n)] # O(2^n)
    tab_binary = [bin(i)[2:] for i in tab_numb] # O(2^n)
    combinations = ['0' * (n - len(k)) + k for k in tab_binary] # O(2^n)
    combinations_valid = []
    for combination in combinations: # O(2^n)
        cost_combi = 0
        profit_combi = 0
        for p in range(n):
            if combination[p] == "1":
                cost_combi += actions[p].cost
                profit_combi += actions[p].profit
        if account >= cost_combi:
            combinations_valid.append(Combination(combination, cost_combi, profit_combi))
    return combinations_valid


def results(combinations_valid):
    entry = input("Afficher combien de résultats ?")
    for j in range(int(entry)): # O(n)
        print(str(combinations_valid[j].code) + " " + str(combinations_valid[j].cost) + " " +
              str(combinations_valid[j].profit))


def best_combi(combinations_valid):
    best_one = combinations_valid[-1] # O(1)
    for h in range(len(combinations_valid)+1): # O(n)
        if combinations_valid[h + 1] is True:
            if combinations_valid[h + 1].profit >= combinations_valid[h].profit and combinations_valid[h + 1].cost < \
                    combinations_valid[h].cost:
                best_one = combinations_valid[h + 1]
        else:
            break
    print("The best solution is: " + str(best_one.code) + " " + str(best_one.cost) + " " + str(best_one.profit))


actions = make_actions(myReader)
combinations_valid = combi_valid(actions, account)
results(combinations_valid)
best_combi(combinations_valid)
