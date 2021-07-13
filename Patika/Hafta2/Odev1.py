#Birden çok katmanlı listeyi düzleştirme
NewList=[]
def flat_list(MyList):
    for i in MyList:
        if type(i) is list:
            flat_list(i)
        else:
            NewList.append(i)
    return NewList

List1=[1,[2,3],[["Turkey","Iraq"],78],"United Kingdom",[[[81]]],[[15,25,[8,"Barcelona"]],17]]
List2=flat_list(List1)
print(List2)
