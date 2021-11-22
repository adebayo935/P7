def option_one(objects, account):
    objects.sort(reverse=True)
    i = 0
    results = []
    total_profit = 0
    while objects[i] and account > 0:
        if (account - objects[i].cost) >= 0:
            résultats.append(objects[i])
            account -= objects[i].cost
            total_profit += objects[i].profit
            i += 1
        else:
            i += 1
    total_profit = round(total_profit, 2)
    print("Sélection:")
    for result in results:
        print(str(result.number) + " " + str(result.profit) + " Prix:" + str(result.cost) + " " + str(
            result.percentage) + "%")
    print("profit total: " + str(total_profit))
