from rich.console import Console
from rich.text import Text
import pyfiglet
import os
os.system("clear") 
console = Console()

# إنشاء نص كبير باستخدام pyfiglet
figlet_text = pyfiglet.figlet_format("mklnjkln", font="standard")

# إعداد النص الملون
colored_text = Text(figlet_text)
colored_text.stylize("bold blue")

# طباعة النص في الـ terminal
console.print(colored_text)

import time
import sys
from termcolor import colored

def mkln(text,delay=0.2 ,color='green'):
    """هذه الوظيفة تطبع نصًا ملونًا، حرفًا حرفًا، مع تأخير محدد بين كل حرف."""
    print("\n")
    for char in text:
        colored_char = colored(char, color)  # تلوين الحرف
        sys.stdout.write(colored_char)  # طباعة الحرف الملون
        sys.stdout.flush()  # تأكد من ظهور الحرف مباشرة في الواجهة
        time.sleep(delay)  # انتظر للتأخير المحدد
    sys.stdout.write('')  # انتهاء السطر بعد الانتهاء من ال
import random

def code():
    # توليد رقم عشوائي مكون من 6 أرقام
    code = random.randint(100000, 999999)
    return str(code)

# استدعاء الوظيفة وطباعة الرقم
mkln("♕enter the number: ",0.2)
mklnh=input("")

mkln("♕check number: "+ mklnh+"♕ ,")
time.sleep(1)
mkln("♕check bypass whatsapp♕ ,")
time.sleep(4)
mkln("♕Successful bypass whatsapp♕ , ")
time.sleep(1)
mkln("♕Get verification code♕ ,")
time.sleep(4)
mkln("♕Successful Get verification♕ : " +code()+ " .") 
print("\n") 
