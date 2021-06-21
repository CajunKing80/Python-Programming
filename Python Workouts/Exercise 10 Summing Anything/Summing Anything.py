
def my_sum(*items):
    if not items:
        return items

    output = items[0]
    for ITEM in items[1:]:
        output += ITEM
    return output


print(my_sum())
print(my_sum(10,20,30,40))
print(my_sum('a', 'b', 'c', 'd'))
print(my_sum([10,20,30], [40,50,60], [70,80]))