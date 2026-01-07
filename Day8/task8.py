def calculate_love_score(name1, name2):
    name = name1.upper()+name2.upper()
    count1=0
    count2=0
    for char in "TRUE":
        count1 += list(name).count(char)
        
    for char in "LOVE":
        count2 += list(name).count(char)
    
    count=str(count1)+str(count2)
    
    print(count)


calculate_love_score("Kanye West", "Kim Kardashian")       