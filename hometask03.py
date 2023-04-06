# Sample Input
# ["eat", "tea", "tan", "ate", "nat", “bat"]
# Sample Output
# [ ["ate", "eat", "tea"], ["nat", "tan"], ["bat"] ]
# Т.е. сгруппировать слова по "общим буквам"

input_list = []
list_len = int(input("Введите сколько слов будет в вашем списке: "))
for i in range(list_len):
    input_list.append(input(f"Введите слово {i+1}: "))
print(input_list)

new_dict={}
for p in input_list:
    new_dict[p]=sorted(list(p))
print(new_dict)
list_keys=list(new_dict.keys())
list_values=list(new_dict.values())
temp_list=[]
last_list=[]
temp=0
for u in list_values:
    count_index=0
    if u not in temp_list: 
        temp_list.append(u)
        last_list.append([list_keys[temp]])
    else:
        for z in range(len(temp_list)):
            if temp_list[z]==list(u):
                last_list[count_index]+=[list_keys[temp]]    
            count_index+=1
    temp+=1
print(last_list)