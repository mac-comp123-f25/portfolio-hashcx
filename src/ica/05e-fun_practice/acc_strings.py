def copy_str(string, num_times):
    ans_str = ""
    for x in range(num_times):
        ans_str += string
        print(ans_str)
    return ans_str


print(copy_str("Amin", 20))
