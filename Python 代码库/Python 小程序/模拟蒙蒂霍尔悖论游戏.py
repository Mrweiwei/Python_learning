def startGame():
    #获取本次游戏中每个门的情况
    doors=init()
    #获取玩家选择的门号
    while True:
        try:
            firstDoorNum=int(input('Chosse a door to open:'))
            assert 0<=firstDoorNum<=2
            break
        except:
            print('Door number must be between {} and {}'.format(0,2))
    #主持人查看另外两个门后的物品情况
    for door in doors.keys()-{firstDoorNum}:
        #打开其中一个后面为羊的门
        if doors[door]=='goat':
            print('"goat behind the door"',door)
            #获取第三个门号，让玩家纠结
            thirdDoor=(doors.keys()-{door,firstDoorNum}).pop()
            change=input('Do you want to swtich to {}?(y/n)'.format(thirdDoor))
            firstDoorNum=thirdDoor if change=='y' else firstDoorNum
            if doors[firstDoorNum]=='goat':
                return 'I win!'
            else:
                return 'you win!'

while True:
    print('='*30)
    print(startGame())
    r=input('Do you want to try once more?(y/n)')
    if r == 'n':
        break
            
