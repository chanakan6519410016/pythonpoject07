# Non-Primitive Data Type 
#Number , Boolean , string 

# Non-Primitive Data Type / collection / Data Structure ข้อมูลชนิดไม่พื้นฐาน
# List , Tuple , set , Dictionary

# Data Type จะเอามาใช้กับการเขียนโปรแกรมในเรื่องของ ตัวแปร พารามิเตอร์ ฟังก์ชัน เมธอด

# -------------- List คือ ข้อมูลหลายข้อมูล คนละชนิด ซ้ำกันได้ และมีลำดับ อีกทัังแก้ไขได้ -----
           # 0  1   2     3    4          5
my_list1 = [10, 20, True, 10, 'SAU', [20, 'IoT']]
           # 6  5   4     3    2          1 ติด -

# -------------- Tuple คือ ข้อมูลหลายข้อมูล คนละชนิด ซ้ำกันได้ และมีลำดับ แต่แก้ไขไม่ได้ -----           
           # 0   1    2     3    4          5
my_tuple1 = (10, 20, True, 10, 'SAU', (20, 'IoT'))
           # 6   5    4     3    2          1 ติด -
           
# -------------- set คือ ข้อมูลหลายข้อมูล คนละชนิด ซ้ำกันไม่ได้(ถ้าซ้ำถือว่าเป็นตัวเดียวกัน) และไม่มีลำดับ และแก้ไขไม่ได้ แต่เพิ่ม ลบได้ -----  
my_set1 = {10, 20, True, 10, 'SAU', (20, 'IoT')}

# -------------- Dictionary คือ ข้อมูลหลายข้อมูล ที่เป็น key:value แก้ไขได้ ไม่มีลำดับ ซ้ำได้ -----
# key เป็น String/Integer ส่วน value เป็นอิหยังก็ได้ (number,string ,booleean,list tuple,set dictionary)
my_diction1 = {'name':'mod', 'age':30, 555:999, 'flag':True, 'wow':[10,20,30,]}