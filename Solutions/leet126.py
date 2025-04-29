beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
# Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
from collections import deque
def findLadders(beginWord, endWord, wordList):

    visited=set()
    queue=deque()
    result=[]
    alpha="abcdefghijklmnopqrstuvwxyz"
    word_list=set(wordList)
    queue.append((beginWord,[beginWord]))
    found= False

    if endWord not in word_list:
        return []

    while queue and not found:
        levels=set()

        for _ in range(len(queue)):
            curr,path=queue.popleft()

            if curr==endWord:
                result.append(path)
                found=True
            

            for i in range(len(curr)):
                for j in alpha:
                    guess=curr[:i]+j+curr[i+1:]

                    if guess in word_list and guess not in visited:
                        queue.append((guess,path + [guess]))
                        levels.add(guess)
        word_list=(word_list-levels)
    return result


findLadders(beginWord,endWord,wordList)
