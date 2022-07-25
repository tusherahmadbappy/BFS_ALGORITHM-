def BFSAlgorithm(graph,root):
    queue=[]
    visited=[]


    visited.append(root)
    queue.append(root)

    while queue :#creatting loop to vist each root
        result = queue.pop(0)
        print(result, end=" ")

        for i in graph[result]:
            if i not in visited:
                visited.append(i)
                queue.append(i)


if __name__ == '__main__':
    graph = {
        5: [3, 7],
        3: [2, 4],
        7: [8],
        2: [],
        4: [8],
        8: []

    }

    BFSAlgorithm(graph, 5)


    """
    total_num = int(input("Enter the total number of key: "))
    for i in range(total_num):
        chose = input("Enter your chose number for input multivalue= Y/y or single value= n/N: ")
        if(chose=='y' or chose=='Y'):
            key1 = int(input("Enter key1: "))
            num1 = int(input("Enter num1: "))
            num2 = int(input("Enter num2: "))
            graph[i]= [num1,num2]
        else:
            chosenum1 = input("Enter chose for num1=y/Y or num2= n/N: ")
            if(chosenum1=='y' or chosenum1=='Y'):
                key2 = int(input("Enter key2: "))
                num1 = int(input("Enter num1: "))
                graph[i] = [num1]
            else:
                key3 = int(input("Enter key3: "))
                num2 = int(input("Enter num2: "))
                graph[i]= [num2]
"""




