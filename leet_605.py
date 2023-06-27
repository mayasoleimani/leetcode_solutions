flowerbed=[1,0,0,0,1]
n=1

def canPlaceFlowers():
    count=0
    flowerbed.insert(0,0)
    flowerbed.append(0)

    for x in range(1,len(flowerbed)-1):

        if (flowerbed[x] == flowerbed[x-1] == flowerbed[x+1] == 0):
            flowerbed[x]=1

            count+=1

    return count >=n


        
canPlaceFlowers()
