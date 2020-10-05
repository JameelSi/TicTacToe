def Board(arr):
    print('''
    {0}  | {1} |  {2}
    -------------
    {3}  | {4} |  {5}
    -------------
    {6}  | {7} |  {8} '''.format(*arr))

def Winner(arr):
    i=0
    while i<len(arr):
        #check columns
        if i<3:
            if arr[i]== arr[i+3] and arr[i]==arr[i+6]:
                return arr[i]
        #check rows
        if i in {0,3,6}:
            if arr[i]==arr[i+1] and arr[i]== arr[i+2]:
                return arr[i]
        if i==0:
            if arr[i]==arr[i+4] and arr[i]== arr[i+8]:
                return arr[i]
        if i==2:
            if arr[i]==arr[i+2] and arr[i]== arr[i+4]:
                return arr[i]
        i+=1
    return ' '

def pcMove(arr,player,computer):
    import random
    #define and fill the array with possible moves
    possibleMoves=[]
    corners=[]
    edges=[]
    mid=False
    for i in arr:
        if type(i)==int:
            possibleMoves.append(i)
    #try different position to check if theres a way to win
    for i in {computer,player}:
        for j in possibleMoves:
            arrcpy=arr[:]
            arrcpy[j-1]=i
            if Winner(arrcpy)!=' ':
                return j

    for j in possibleMoves:
        if j in {1,3,7,9}:
            corners.append(j)
        elif 5 in possibleMoves:
            mid=True
        elif j in {2,4,6,8}:
            edges.append(j)
    if len(corners)>0:
        return corners[random.randrange(0,len(corners))]
    elif mid==True:
        return 5
    elif len(edges)>0:
        return edges[random.randrange(0,len(edges))]
def main():
    player=input('What do you prefer , X or O ?\n')
    while player.upper() not in {'X', 'O'}:
        player=input('Wrong input please choose X or O ?')
    player=player.upper()
    if player=='X':
        computer='O'
    else:
        computer='X'
    arr=[1,2,3,4,5,6,7,8,9]

    while 1:
        Board(arr)
        try:
            pos=int(input('Your turn,choose (1-9) to place your %s \n'%player))
        except ValueError:
            print('Please insert a number ')
            continue
        while int(pos) not in arr:
            pos=input('Please choose an available number between 1-9 on the board ')
        arr[int(pos)-1]=player
        winner=Winner(arr)
        if winner !=' ':
            Board(arr)
            print('%s Won !'%winner)
            break
        if arr.count('X') + arr.count('O')==9:
            Board(arr)
            print("it's a Tie !!")
            break
        arr[int(pcMove(arr,player,computer))-1]=computer
        print('Computer has made its move\n')
        winner=Winner(arr)
        if winner !=' ':
            Board(arr)
            print('%s Won !'%winner)
            break
        elif arr.count('X') + arr.count('O')==9:
            print("it's a Tie !!")
            break
    global newGame
    newGame=input('Do you want to play again ? insert Y\n')

newGame='Y'
while newGame=='Y':
    main()
