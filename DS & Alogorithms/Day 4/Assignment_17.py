#DSA-Assgn-17

def find_matches(country_name):
    #Remove pass and write your logic here
    temp_lst = []
    for data in match_list:
        lst = data.split(":")
        if lst[0] == country_name:
            temp_lst.append(data)
            
    return temp_lst

def max_wins():
    #Remove pass and write your logic here
    dic = {}
    temp = []
    for data in match_list:
        lst = data.split(":")
        if lst[1] not in dic.keys():
            dic[lst[1]] = []
        dic[lst[1]].append(int(lst[3]))
    
    for key in dic.keys():
        mx = max(dic[key])
        dic[key].append(mx)
    
    dic2 = {}
    for key in dic.keys():
        for data in match_list:
            lst = data.split(":")
            if lst[1] not in dic2.keys():
                dic2[lst[1]] = []
            if lst[1] == str(key):
                if int(lst[3]) == dic[key][-1]:
                    dic2[lst[1]].append(lst[0])
        
    return (dic2)
        

def find_winner(country1,country2):
    #Remove pass and write your logic here
    dic = {}
    dic[country1] = 0
    dic[country2] = 0
    
    for data in match_list:
        lst = data.split(":")
        if lst[0] == country1:
            dic[country1] += int(lst[3])
        elif lst[0] == country2:
            dic[country2] += int(lst[3])
        
    if dic[country1] > dic[country2]:
        return country1
    elif dic[country1] < dic[country2]:
        return country2
    elif dic[country1] == dic[country2]:
        return "Tie"

#Consider match_list to be a global variable
match_list=["AUS:CHAM:5:2","AUS:WOR:2:1","ENG:WOR:2:0","IND:T20:5:3","IND:WOR:2:1","PAK:WOR:2:0","PAK:T20:5:1","SA:WOR:2:0","SA:CHAM:5:1","SA:T20:5:0"]

#Pass different values to each function and test your program
print("The match status list details are:")
print(match_list)
print()
print(find_winner("IND", "AUS"))