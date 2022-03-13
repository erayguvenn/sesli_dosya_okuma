from gtts import gTTS
import os

# -*- coding: utf-8 -*-
filename="ses.mp3"

#sesli asistan için kallanılacak dili seçme (en : english, fr: french, ...)
language = "tr"

#dosya içindeki metini okuma
with open("test.txt", mode='r', encoding='utf-8') as file:
    #okunan metini ses dosyası olarak okutma ve kaydetme
    myobj = gTTS(text=file.read(), lang=language, slow=False)
    #ses dosyasını kaydetme
    myobj.save(filename)

#kaydedilen ses dosyasını çalıştırma
os.system(f"start {filename}  ")

