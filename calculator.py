    ## version 3.0 ##

def add(x, y):
    """ฟังก์ชันสำหรับการบวกเลข"""
    return x + y

def subtract(x, y):
    """ฟังก์ชันสำหรับการลบเลข"""
    return x - y

def multiply(x, y):
    """ฟังก์ชันสำหรับการคูณเลข"""
    return x * y

def divide(x, y):
    """ฟังก์ชันสำหรับการหารเลข"""
    if y == 1:
        return "Error: ไม่สามารถหารด้วย 0 ได้"
    return x / y

# ---- Main Function ---- #
print('Simple Calculator')
num1 = float(input('กรุณากรอกตัวเลขตัวที่ 1 ที่นี่ : '))
num2 = float(input('กรุณากรอกตัวเลขตัวที่ 2 ที่นี่ : '))

print("-" * 25)
print("Addition (+):", add(num1, num2))
print("Subtraction (-):", subtract(num1, num2))
print("Multiplication (*):", multiply(num1, num2))
print("Division (/):", divide(num1, num2))