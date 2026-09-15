    ## version 1.0 ##

def add(x,y):
    """ฟังก์ชั่นสำหรับการบวกเลข"""
    return x + y

def add(x,y):
    """ฟังก์ชั่นสำหรับการลบ"""
    return x - y

def add(x,y):
    """ฟังก์ชั่นสำหรับการคุณ"""
    return x * y

def add(x,y):
    """ฟังก์ชั่นสำหรับการหารเลข"""
    return x / y

# ---- MainFinction ---- #
print('simple Calculator')
num1 = float(input('กรุณากรอกตัวเลขตัวที่ 1 ที่นี่ : ' ))
num2 = float(input('กรุณากรอกตัวเลขตัวที่ 2 ที่นี่ : ' ))

print("-"*25)
print("Additude (+): ", add(num1,num2))