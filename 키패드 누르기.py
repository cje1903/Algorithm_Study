numbers=[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand="right"    # 왼손잡이 or 오른손잡이
result=""

keypad=[[-1,7,4,1],[0,8,5,2],[-1,9,6,3]]
L_hand=[0,0]; R_hand=[2,0]
length=len(numbers)
i=0
while(i<length):
    j=0;k=0
    J=0;K=0
    for j in range(0,3):
        for k in range(0,4):
            if numbers[i]==keypad[j][k]:
                J=j; K=k
                break
    
    if numbers[i] in keypad[0]:
        result+="L"
        L_hand=[J,K]
    
    elif numbers[i] in keypad[2]:
        result+="R"
        R_hand=[J,K]
    
    else:
        distance=0
        L_dis=0; R_dis=0
        L_dis=abs(L_hand[0]-J)+abs(L_hand[1]-K)
        R_dis=abs(R_hand[0]-J)+abs(R_hand[1]-K)

        if L_dis<R_dis:
            result+="L"
            L_hand=[J,K]

        elif L_dis>R_dis:
            result+="R"
            R_hand=[J,K]

        else:
            if hand=="left":
                result+="L"
                L_hand=[J,K]
            elif hand=="right":
                result+="R"
                R_hand=[J,K]

    i+=1


print(result)