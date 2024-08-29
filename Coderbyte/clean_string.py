# Your program will take in a string and clean out all numeric characters, and return a string with spacing and special characters ~#$%^&!@*():;"'.,? all intact.


def string_clean(s):
    st_list = s.split(' ')
    print(st_list)
    res_list = []
    for word in st_list:
            res = ''
            for char in word:
                if  not char.isnumeric():
                    res += f'{char}'
            res_list.append(res)
            print(res_list)
            result = ' '.join(res_list)
            print(result)
    return result
    
        
print(string_clean('This looks5 grea8t!'))