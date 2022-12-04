def f(player1,player2):
    sum1=0
    sum2=0
    for letter in player1: 
        if letter in ['A','K','Q','J','T']: 
            sum1=sum1+10
        elif letter.isdigit():
            sum1=sum1+int(letter)

    for letter in player2: 
        if letter in ['A','K','Q','J','T']:
           sum2=sum2+10
        elif letter.isdigit():
            sum2=sum2+int(letter)
    return sum1 > sum2 
       
print(f("AJ972", "AQT72")) 
print(f("9532", "K8")) 
print(f("987", "AT4"))