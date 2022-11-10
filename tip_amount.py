def score(total,correct,wrong):
    #total :number of quizzes
    #correct:number of quizzes you correctly answered 
    #wrog: number of quizzes you answered incorrectly

    finalscore = ((correct * 2) + (wrong * 1)) / total * 2 
    
    return finalscore


print(score(20,20,0))
# 100.0 because you got a perfect score 
