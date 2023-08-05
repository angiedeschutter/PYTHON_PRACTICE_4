def multi_list(num_list):
    if len(num_list)==0:
        return 0
    else:
        total=1
        for i in num_list:
            total=total*(i)
        print(total)

multi_list([2,6,3])