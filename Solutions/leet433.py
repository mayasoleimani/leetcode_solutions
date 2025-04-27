# startGene = "AACCGGTT"
# endGene = "AAACGGTA"
# bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]

from collections import deque
# def minMutation(startGene,endGene,bank):

#     visited=set()
#     queue=deque()
#     gene=0
#     options=["A","C","G","T"]
#     count=0

#     queue.append(startGene)
#     visited.add(startGene)
    
#     while queue:

#         for i in range(len(queue)):
#             curr=queue.popleft()

#             if curr==endGene:
#                 return count


#             for x in range(len(list(startGene))):
#                 for y in range(len(options)):
#                     gene=curr[:x]+str(options[y])+curr[x+1:]
#                     if gene not in visited and gene in bank:
#                         queue.append(gene)
#                         visited.add(gene)
#         count+=1

#     return -1

# minMutation(startGene,endGene,bank)


allowed = ["aab", "abb", "abc", "aac"]

start="aaa"
end="abc"

def starting(start,end,allowed):

    visited=set()
    queue=deque()
    count=0
    direct=["a","b","c"]
    word=0

    visited.add(start)
    queue.append(start)

    while queue:

        for _ in range(len(queue)):
            curr=queue.popleft()

            if curr == end:
                return count
            
            for i in range(len(list(start))):
                for j in range(len(direct)):
                    word=curr[:i]+direct[j]+curr[i+1:]

                    if word not in visited and word in allowed:
                        queue.append(word)
                        visited.add(word)
        count+=1
    return -1


    

starting(start,end,allowed)