# character in string has index number 
        # 01234567890123
infoA = 'Hello SAU 2023'
        # 43240987654321 ติด -
        
print(infoA[6]) # S 
print(infoA[-8]) # S

# เข้าถึงตัวอักษรหลายๆ ตัวใน string เราจะใช้วิธี Slicing ด้วย index number

print(infoA[6:9])
print(infoA[-8:-5])

# o SAU 20
print(infoA[4:12])

# String Method
print(infoA.upper() )
print(infoA.lower() )
print(infoA.capitalize() )
print(infoA.count('l') )
print(infoA.isdigit() )
print(infoA.islower() )
infoB = infoA.replace('SAU' , 'IOT')
print(infoA)
print(infoB)
print(infoB.replace('Hello' , 'Hi...'))

# String String
print( len(infoA) )

print('SAU',35,end='') # SAU 35
print('SAU'+str(35)) #SAU35
print('SAU',35,sep='') #SAU35
print('20','02','2023,',sep='/')
print(20,'มกราคม',2023,sep='-')
