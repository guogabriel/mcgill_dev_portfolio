
import time

from tkinter import*

 
fenetre=Tk() 
fenetre.geometry("400x610") 
fenetre.title("Sudoku solver")  
fenetre['background']='LightSlateGray'


columnA = [None, None, None, None] 
columnB = [None, None, None, None]
columnC = [None, None, None, None] 
columnD = [None, None, None, None]

coordsValue = {'A1': None,
               'A2': None,
               'A3': None,
               'A4': None,
               'B1': None,
               'B2': None,
               'B3': None,
               'B4': None,
               'C1': None,
               'C2': None,
               'C3': None,
               'C4': None,
               'D1': None,
               'D2': None,
               'D3': None,
               'D4': None} 

listOfCoords = ['A1','A2','A3','A4','B1','B2','B3','B4','C1','C2','C3','C4','D1','D2','D3','D4']
potentialCoords = listOfCoords.copy()

S1 = ['A1','A2','B1','B2'] 
S2 = ['C1','C2','D1','D2'] 
S3 = ['A3','A4','B3','B4'] 
S4 = ['C3','C4','D3','D4']

allYCoords = [['A1', 'B1', 'C1', 'D1'], ['A2', 'B2', 'C2', 'D2'], ['A3', 'B3', 'C3', 'D3'], ['A4', 'B4', 'C4', 'D4']]
allXCoords = [['A1', 'A2', 'A3', 'A4'], ['B1', 'B2', 'B3', 'B4'], ['C1', 'C2', 'C3', 'C4'], ['D1', 'D2', 'D3', 'D4']]

def GetValue(): 
    Coords = askvalueEntry.get() 
    if Coords == "A1": 
        ValueA1 = askvalueEntry2.get() 
        ValueA1 = int(ValueA1)
        columnA[0] = ValueA1
        coordsValue['A1'] = ValueA1
        
    elif Coords == "A2": 
        ValueA2 = askvalueEntry2.get() 
        ValueA2 = int(ValueA2)
        columnA[1] = ValueA2
        coordsValue['A2'] = ValueA2
        
    elif Coords == "A3": 
        ValueA3 = askvalueEntry2.get() 
        ValueA3 = int(ValueA3)
        columnA[2] = ValueA3
        coordsValue['A3'] = ValueA3
        
    elif Coords == "A4": 
        ValueA4 = askvalueEntry2.get() 
        ValueA4 = int(ValueA4)
        columnA[3] = ValueA4
        coordsValue['A4'] = ValueA4
        
    elif Coords == "B1": 
        ValueB1 = askvalueEntry2.get() 
        ValueB1 = int(ValueB1)
        columnB[0] = ValueB1
        coordsValue['B1'] = ValueB1
        
    elif Coords == "B2": 
        ValueB2 = askvalueEntry2.get() 
        ValueB2 = int(ValueB2)
        columnB[1] = ValueB2
        coordsValue['B2'] = ValueB2
        
    elif Coords == "B3": 
        ValueB3 = askvalueEntry2.get() 
        ValueB3 = int(ValueB3)
        columnB[2] = ValueB3
        coordsValue['B3'] = ValueB3
        
    elif Coords == "B4": 
        ValueB4 = askvalueEntry2.get() 
        ValueB4 = int(ValueB4)
        columnB[3] = ValueB4
        coordsValue['B4'] = ValueB4
        
    elif Coords == "C1": 
        ValueC1 = askvalueEntry2.get() 
        ValueC1 = int(ValueC1)
        columnC[0] = ValueC1
        coordsValue['C1'] = ValueC1
        
    elif Coords == "C2": 
        ValueC2 = askvalueEntry2.get() 
        ValueC2 = int(ValueC2)
        columnC[1] = ValueC2
        coordsValue['A1'] = ValueC2
        
    elif Coords == "C3": 
        ValueC3 = askvalueEntry2.get() 
        ValueC3 = int(ValueC3)
        columnC[2] = ValueC3
        coordsValue['C3'] = ValueC3
        
    elif Coords == "C4": 
        ValueC4 = askvalueEntry2.get() 
        ValueC4 = int(ValueC4)
        columnC[3] = ValueC4
        coordsValue['C4'] = ValueC4
        
    elif Coords == "D1": 
        ValueD1 = askvalueEntry2.get() 
        ValueD1 = int(ValueD1)
        columnD[0] = ValueD1
        coordsValue['D1'] = ValueD1
        
    elif Coords == "D2": 
        ValueD2 = askvalueEntry2.get() 
        ValueD2 = int(ValueD2)
        columnD[1] = ValueD2
        coordsValue['D2'] = ValueD2
        
    elif Coords == "D3": 
        ValueD3 = askvalueEntry2.get() 
        ValueD3 = int(ValueD3)
        columnD[2] = ValueD3
        coordsValue['D3'] = ValueD3
        
    elif Coords == "D4": 
        ValueD4 = askvalueEntry2.get() 
        ValueD4 = int(ValueD4)
        columnD[3] = ValueD4
        coordsValue['D4'] = ValueD4
    else: 
        print("I Can't read what you put")

    print("Updating...")
    print(columnA)
    print(columnB)
    print(columnC)
    print(columnD)
                

def search(searchingValue): 
    searchingPos = 0 
    wantedKeys = []
    listOfValues = list(coordsValue.values()) 
    listOfKeys = list(coordsValue.keys()) 
    for i in listOfValues: 
        if listOfValues[searchingPos] == searchingValue: 
            wantedKeys.append(listOfKeys[searchingPos])
            searchingPos = searchingPos + 1 
        else: 
            searchingPos = searchingPos + 1 
    return wantedKeys

def locate(*coords):
    print('start')
    tupleLength = len(coords)
    print(tupleLength)
    potentialCoords = listOfCoords.copy()
    for i in range(0, tupleLength):
        collisionCheckAgain = []
        searchingCoords = coords[i]
        letters = ['A', 'B', 'C', 'D']
        print("current coord:", coords[i])
        for b in potentialCoords:
            print("collision checking:", b)
            if coordsValue[b] != None:
                print("collision found:", b, coordsValue[b])
                potentialCoords.remove(b)
                print("potential coords:", potentialCoords)
                if listOfCoords.index(b) != 15:
                    collisionCheckAgain.append(listOfCoords[listOfCoords.index(b) + 1])
        for o in collisionCheckAgain:
            if coordsValue[o] != None:
                potentialCoords.remove(o)
        
        for a in range(0, 4):
            if searchingCoords in allXCoords[a]:
                for b in range(0, 4):
                    if allXCoords[a][b] in potentialCoords:
                        potentialCoords.remove(allXCoords[a][b])
            if searchingCoords in allYCoords[a]:
                for c in range(0, 4):
                    if allYCoords[a][c] in potentialCoords:
                        potentialCoords.remove(allYCoords[a][c])

        #for a in letters:
            #if a in searchingCoords:
                #for b in potentialCoords:
                   #if a in b:
                        #potentialCoords.remove(b)
        #for z in range(1, 5):
            #z = str(z)
            #if z in searchingCoords:
                #for y in potentialCoords:
                    #if z in y:
                        #potentialCoords.remove(y)
        if searchingCoords in S1:
            print("S1 correspondance")
            for element1 in S1:
                if element1 in potentialCoords:
                    print("removed:", element1)
                    potentialCoords.remove(element1)
                    print("potential coords:", potentialCoords)
        if searchingCoords in S2:
            print("S2 correspondance")
            for element2 in S2:
                if element2 in potentialCoords:
                    print("removed:", element2)
                    potentialCoords.remove(element2)
                    print("potential coords:", potentialCoords)
        if searchingCoords in S3:
            print("S3 correspondance")
            for element3 in S3:
                if element3 in potentialCoords:
                    print("removed:", element3)
                    potentialCoords.remove(element3)
                    print("potential coords:", potentialCoords)
        if searchingCoords in S4:
            print("S4 correspondance")
            for element4 in S4:
                if element4 in potentialCoords:
                    print("removed:", element4)
                    potentialCoords.remove(element4)
                    print("potential coords:", potentialCoords)
        print("end")
    return potentialCoords

def placeNum(value, *potentialCoords):
    coordsList = []
    for h in potentialCoords:
        coordsList.append(h)
    
    holdNum = []
    for a in S1:
        if a in coordsList:
            holdNum.append(a)
    if len(holdNum) == 1:
        coordsValue[holdNum[0]] = value
        #coordsList.remove(holdNum[0])
    holdNum = []
    
    for b in S2:
        if b in coordsList:
            holdNum.append(b)
    if len(holdNum) == 1:
        coordsValue[holdNum[0]] = value
        #coordsList.remove(holdNum[0])
    holdNum = []
    
    for c in S3:
        if c in coordsList:
            holdNum.append(c)
    if len(holdNum) == 1:
        coordsValue[holdNum[0]] = value
        #coordsList.remove(holdNum[0])
    holdNum = []
    
    for d in S4:
        if d in coordsList:
            holdNum.append(d)
    if len(holdNum) == 1:
        coordsValue[holdNum[0]] = value
        #coordsList.remove(holdNum[0])
    holdNum = []
                   
    for i in coordsList:
        if i.startswith("A"):
            holdNum.append(i)
    if len(holdNum) == 1:
        coordsValue[holdNum[0]] = value
        #coordsList.remove(holdNum[0])
    holdNum = []
    
    for i in coordsList:
        if i.startswith("B"):
            holdNum.append(i)
    if len(holdNum) == 1:
        coordsValue[holdNum[0]] = value
        #coordsList.remove(holdNum[0])
    holdNum = []
    
    for i in coordsList:
        if i.startswith("C"):
            holdNum.append(i)
    if len(holdNum) == 1:
        coordsValue[holdNum[0]] = value
        #coordsList.remove(holdNum[0])
    holdNum = []
    
    for i in coordsList:
        if i.startswith("D"):
            holdNum.append(i)
    if len(holdNum) == 1:
        coordsValue[holdNum[0]] = value
        #coordsList.remove(holdNum[0])
    holdNum = []
    
    for i in coordsList:
        if i.endswith("1"):
            holdNum.append(i)
    if len(holdNum) == 1:
        coordsValue[holdNum[0]] = value
        #coordsList.remove(holdNum[0])
    holdNum = []
    
    for i in coordsList:
        if i.endswith("2"):
            holdNum.append(i)
    if len(holdNum) == 1:
        coordsValue[holdNum[0]] = value
        #coordsList.remove(holdNum[0])
    holdNum = []

    for i in coordsList:
        if i.endswith("3"):
            holdNum.append(i)
    if len(holdNum) == 1:
        coordsValue[holdNum[0]] = value
        #coordsList.remove(holdNum[0])
    holdNum = []

    for i in coordsList:
        if i.endswith("4"):
            holdNum.append(i)
    if len(holdNum) == 1:
        coordsValue[holdNum[0]] = value
        #coordsList.remove(holdNum[0])
    holdNum = []

def Solve():
    fenetre.destroy()
    while any(x is None for x in coordsValue.values()):
        values = []
        for o in coordsValue.values():
            values.append(o)
        print(values)
        for i in range(1,5):
            print('attempting:', i)
            print("nbr of values found:", values.count(i))
            if values.count(i) < 4 and values.count(i) > 0:
                print("initiating program for:", i)
                searched = search(i)
                print("search output:", searched)
                located = locate(*searched)
                print("locate ourput:", located)
                placeNum(i, *located)
                print("coordsValue:", coordsValue)
                #time.sleep(25)
            elif values.count(i) == 0:
                print("nbr of values found: 0")
                PotCoords0 = listOfCoords.copy()
                collisionCheckAgain = []
                for b in PotCoords0:
                    print("0 collision checking:", b)
                    if coordsValue[b] != None:
                        print("0 collision found:", b, coordsValue[b])
                        PotCoords0.remove(b)
                        print("0 potential coords:", PotCoords0)
                        if listOfCoords.index(b) != 15:
                            collisionCheckAgain.append(listOfCoords[listOfCoords.index(b) + 1])
                for p in collisionCheckAgain:
                    if coordsValue[p] != None:
                        PotCoords0.remove(p)
                placeNum(i, *PotCoords0)
                print("coordsValue:", coordsValue)
                #time.sleep(25)
            
askvalueLabel=Label(fenetre,text="Please enter the coordinate of",font=("ComicSansMS",20),width=60) 
askvalueLabel.pack(pady=0) 


askvalueLabel2=Label(fenetre,text="the square (ex: A1, A2, B4, D3)",font=("ComicSansMS",20),width=60) 
askvalueLabel2.pack(pady=0) 


A1button=Button(fenetre,width=3,text="A1",font=("ComicSansMS",20))  
A1button.place(x=80,y=90)   

A2button=Button(fenetre,width=3,text="A2",font=("ComicSansMS",20))  
A2button.place(x=140,y=90)  

A3button=Button(fenetre,width=3,text="A3",font=("ComicSansMS",20))  
A3button.place(x=200,y=90) 

A4button=Button(fenetre,width=3,text="A4",font=("ComicSansMS",20))  
A4button.place(x=260,y=90) 

B1button=Button(fenetre,width=3,text="B1",font=("ComicSansMS",20))  
B1button.place(x=80,y=150) 

B2button=Button(fenetre,width=3,text="B2",font=("ComicSansMS",20))  
B2button.place(x=140,y=150) 

B3button=Button(fenetre,width=3,text="B3",font=("ComicSansMS",20))  
B3button.place(x=200,y=150) 

B4button=Button(fenetre,width=3,text="B4",font=("ComicSansMS",20))  
B4button.place(x=260,y=150) 
  
C1button=Button(fenetre,width=3,text="C1",font=("ComicSansMS",20))  
C1button.place(x=80,y=210) 

C2button=Button(fenetre,width=3,text="C2",font=("ComicSansMS",20))  
C2button.place(x=140,y=210) 

C3button=Button(fenetre,width=3,text="C3",font=("ComicSansMS",20))  
C3button.place(x=200,y=210) 

C4button=Button(fenetre,width=3,text="C4",font=("ComicSansMS",20))  
C4button.place(x=260,y=210) 

D1button=Button(fenetre,width=3,text="D1",font=("ComicSansMS",20))  
D1button.place(x=80,y=270) 

D2button=Button(fenetre,width=3,text="D2",font=("ComicSansMS",20))  
D2button.place(x=140,y=270) 

D3button=Button(fenetre,width=3,text="D3",font=("ComicSansMS",20))  
D3button.place(x=200,y=270) 

D4button=Button(fenetre,width=3,text="D4",font=("ComicSansMS",20))  
D4button.place(x=260,y=270) 

askvalueEntry=Entry(fenetre,width=57) 
askvalueEntry.place(x=0,y=340) 

askvalueLabel3=Label(fenetre,text="Please enter the value",font=("ComicSansMS",20)) 
askvalueLabel3.place(x=60,y=370) 

askvalueLabel4=Label(fenetre,text="of this square",font=("ComicSansMS",20)) 
askvalueLabel4.place(x=110,y=408) 

askvalueEntry2=Entry(fenetre,width=57) 
askvalueEntry2.place(x=0,y=450) 
    
askvalueButton=Button(fenetre,text="Enter",font=("ComicSansMS",20),width=25,command=GetValue) 
askvalueButton.place(x=0,y=480)

finishButton=Button(fenetre,text="Solve",font=("ComicSansMS",20),width=25,command=Solve)
finishButton.place(x=0,y=550)

fenetre.mainloop() 

 
