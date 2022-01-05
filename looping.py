list  = [1,2,3]

stringstring = "STRINGY"

dic  = {'key':123, "kets2": 456}


for i in dic:
    print(i)

#instance of a class iterable  ? 

class User:
    def __init__(self) -> None:
        self.name  = "me"


me = User()
#instance of the class cannot be iterable  
# there is nothing item that comes next in line  
#and the methoths are functions and there is not order.. no one would really do it. 

for i in me.__dict__:
    print(i, me.__dict__[i])

    



