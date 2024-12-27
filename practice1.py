def friends_in_trouble(j_angry,s_angry):
    if j_angry == True and s_angry == True:
        return True
    elif j_angry == False and s_angry == False:
        return True
    else:
        return False
    
print(friends_in_trouble(True,True))
print(friends_in_trouble(False,False))
print(friends_in_trouble(True,False))
print(friends_in_trouble(False,True))