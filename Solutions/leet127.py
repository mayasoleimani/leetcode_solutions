beginWord = "hit"
endWord = "cog"
wordList=["hot","dot","dog","lot","log","cog"]
from collections import deque
def ladderLength(beginWord, endWord, wordList):

    queue=deque()
    alpha="abcdefghijklmnopqrstuvwxyz"
    wordList=set(wordList)
    count=1
    queue.append(beginWord)

    if endWord not in wordList:
        return 0


    while queue:

        for _ in range(len(queue)):
            curr=queue.popleft()

            if curr==endWord:
                return count
            
            for i in range(len(curr)):
                for j in alpha:

                    guess=curr[:i]+j+curr[i+1:]

                    if guess in wordList:
                        queue.append(guess)
                        wordList.remove(guess)

        count+=1

    
    return 0



ladderLength(beginWord,endWord,wordList)