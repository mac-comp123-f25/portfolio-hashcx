def change_start(val: str, lst: list[str]):
    lst[0] = val

t_lst = ['a', 'b', 'c', 'd', 'e', 'd']
change_start('99', t_lst)
print(t_lst)


new_t_lst = [item.center(20, "*") for item in t_lst]
print(new_t_lst)
