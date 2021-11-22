
def option_two(objects, account):
    n = len(objects)
    tab_numb = [i for i in range(2 ** n)]
    tab_binary = [bin(i)[2:] for i in tab_numb]
    combinations = ['0' * (n - len(k)) + k for k in tab_binary]
    combinations_valid = []
    for combination in combinations:
        cost_combi = 0
        profit_combi = 0
        for p in range(n):
            if combination[p] == "1":
                cost_combi += objects[p].cost
                profit_combi += objects[p].profit
        if account >= cost_combi:
            combinations_valid.append(Combination(combination, cost_combi, profit_combi))

    combinations_valid.sort(reverse=True)
    for combination in combinations_valid:
        print(str(combination.code) + " " + str(combination.cost) + " " +
              str(combination.profit))

    entry = input("Afficher combien de résultats ?")

    for j in range(int(entry)):
        print(str(combinations_valid[j].code) + " " + str(combinations_valid[j].cost) + " " +
              str(combinations_valid[j].profit))

    best_one = combinations_valid[0]
    for h in range(len(combinations_valid)):
        if combinations_valid[h + 1] is True:
            if combinations_valid[h + 1].profit >= combinations_valid[h].profit and combinations_valid[h + 1].cost < \
                    combinations_valid[h].cost:
                best_one = combinations_valid[h + 1]
        else:
            break

    print("The best solution is: " + str(best_one.code) + " " + str(best_one.cost) + " " + str(best_one.profit))
