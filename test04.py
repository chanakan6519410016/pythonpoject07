# -------------- List คือ ข้อมูลหลายข้อมูล คนละชนิด ซ้ำกันได้ และมีลำดับ อีกทัังแก้ไขได้ -----        
                                        # 0    1
           # 0  1   2     3    4          5
my_list1 = [10, 20, True, 10, 'SAU', [20, 'IoT']]
           # 6  5   4     3    2          1 ติด -
                                        # 2   1 ติด -
           
# การเข้าถึงข้อมูลใน Liat เพื่อเอาข้อมูลมาใช้ หรือแก้ไขค่าข้อมูลให้มันใหม่
# เขาถึงแต่ละข้อมูล
print(my_list1[4]) # SAU
print(my_list1[-2]) # SAU
print(my_list1[5]) #[20, 'IoT']
print(my_list1[-1]) # [20, 'IoT']
print(my_list1[5]) # IoT
print(my_list1[-1]) # IoT


# เข้าถึงทีละหลายข้อมูล เรียกกาาร Slicing ผลลัพธ์จะเป็น List
print(my_list1[1:4]) # 20, True, 10
print(my_list1[3:]) # 10, 'SAU', [20, 'IoT] 
print(my_list1[:3]) # 10, 20, True


# เข้าถึงทุกข้อมูล
for info in my_list1 :
    print(info, end=', ')
    
print()

print(my_list1)
my_list1[4] = 'Thailand'
print(my_list1)

# List Method
my_list2 = [10, 20, True, 10, 'SAU', [20, 'IoT']]
my_list2.append('wow')
print(my_list2)
my_list2.append([111,222,333])
print(my_list2)
my_list2.extend([444,555])
print(my_list2)
my_list2.remove(10)
my_list2.remove('SAU')
my_list2.remove([111,222,333])
print(my_list2)
my_list2.pop()
my_list2.pop()
my_list2.pop()
print(my_list2)
my_list2.pop(2) # 2 คือ index
print(my_list2)