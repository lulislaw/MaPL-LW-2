skidka = 0.6
costs = [99,199,299,399,499]
print("Без скидки | Сумма скидки | Новая цена")
for i in range(5):
    print(i+1, ".", format(costs[i],'0.0f'), "|", format(costs[i] * skidka, '0.2f'), "|", format(costs[i] * (1-skidka),'0.2f'))
