from arabic_reshaper import ArabicReshaper
import os
from pathlib import Path
import time
reshaper = ArabicReshaper(configuration={'delete_harakat': False})
def assassins_creed(a):
        a=a.replace("‌\u200c"," ")
        a=a.replace('‌'," ")
        a=reshaper.reshape(a)
        a=a.replace("ﻻ","ﻟﺎ").replace("ﻼ","ﻠﺎ")
        alefBakola=["آ","ﺁ","ﺂ"] #
        alefBikola=["ا","ﺍ","ﺎ"] # 
        be=["ب","ﺏ","ﺐ","ﺒ","ﺑ"] #
        pe=["پ","ﭖ","ﭗ","ﭙ","ﭘ"] #
        te=["ت","ﺕ","ﺖ","ﺘ","ﺗ"] #
        se=["ث","ﺙ","ﺚ","ﺜ","ﺛ"] #
        jim=["ج","ﺝ","ﺞ","ﺠ","ﺟ"] #
        che=["چ","ﭺ","ﭻ","ﭽ","ﭼ"] #
        he=["ح","ﺡ","ﺢ","ﺤ","ﺣ"] #
        khe=["خ","ﺥ","ﺦ","ﺨ","ﺧ"] #
        dal=["د","ﺩ","ﺪ"] #
        zal=["ذ","ﺫ","ﺬ"] #
        re=["ر","ﺭ","ﺮ"] #
        ze=["ز","ﺯ","ﺰ"] #
        zhe=["ژ","ﮊ","ﮋ"] #
        sin=["س","ﺱ","ﺲ","ﺴ","ﺳ"] #
        shin=["ش","ﺵ","ﺶ","ﺸ","ﺷ"] #
        sad=["ص","ﺹ","ﺺ","ﺼ","ﺻ"] #
        zad=["ض","ﺽ","ﺾ","ﻀ","ﺿ"] #
        ta=["ط","ﻁ","ﻂ","ﻄ","ﻃ"] #
        za=["ظ","ﻅ","ﻆ","ﻈ","ﻇ"] #
        ein=["ع","ﻉ","ﻊ","ﻌ","ﻋ"] #
        ghein=["غ","ﻍ","ﻎ","ﻐ","ﻏ"] #
        fe=["ف","ﻑ","ﻒ","ﻔ","ﻓ"] #
        qaf=["ق","ﻕ","ﻖ","ﻘ","ﻗ"] #
        kaf=["ک","ﮎ","ﮏ","ﮑ","ﮐ","ﻙ","ﻚ","ﻜ","ﻛ"] #
        gaf=["گ","ﮒ","ﮓ","ﮕ","ﮔ"] #
        lam=["ل","ﻝ","ﻞ","ﻠ","ﻟ"] #
        mim=["م","ﻡ","ﻢ","ﻤ","ﻣ"] #
        nun=["ن","ﻥ","ﻦ","ﻨ","ﻧ"] #
        vav=["و","ﻭ","ﻮ"] #
        ha=["ه","ﻩ","ﻪ","ﻬ","ﻫ"] #
        ye=["ی","ﯼ","ﯽ","ﯿ","ﯾ","ﻱ","ﻲ","ﻴ","ﻳ","ﻯ","ﻰ"] #
        hamze=["ئ","ﺉ","ﺊ","ﺌ","ﺋ"] #
        vavhamze=["ؤ","ﺅ","ﺆ"] #
        listAlefba=[alefBakola,alefBikola,be,pe,te,se,jim,che,he,khe,dal,zal,re,ze,zhe,sin,shin,sad,zad,ta,za,ein,ghein,fe,qaf,kaf,gaf,lam,mim,nun,vav,ha,ye,hamze,vavhamze]
        for i in listAlefba:
                a=a.replace(i[1],i[0])
        a=a.replace('ﮐ','ﻛ')
        a=a.replace('ﭙ','ﭘ')
        return a

Address=input("Drag and Drop the txt file: ")
if "& " in Address:
    Address=Address.replace("& ",'')
Address=Address.replace("'",'')
Address=Address.replace('"','')
print("-----------------------------------------\nStart Procress")
text_file = open(Address,'r',encoding="utf8")
text = text_file.read()
text_file.close()
text1= assassins_creed(text)
Path(Address).stem
new_adrress = Address.replace(os.path.basename(Address),Path(Address).stem+"_new"+".txt")
output_file = open(new_adrress , 'w', encoding='utf-8')
output_file.write(text1)
output_file.close()
print(f"-----------------------------------------\nNew File Created in {new_adrress}\n-----------------------------------------\n CLI Closed After 4 Sec")
time.sleep(4)
