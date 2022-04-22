from pdf2image import convert_from_path
from termcolor import colored
import os
import time

while True:
    path = input("Input PDF file path:")
    if path:
        ct = time.time()
        try:
            print(colored("> Pre-processing...","yellow"))
            images = convert_from_path(path,dpi=600,poppler_path="./poppler/bin")
        except:
            print(colored(f"The path \'{path}\' can\'t convert to image!","red"))
        
        filename =(path.split("\\")[-1]).replace(".pdf","")
        folder = os.path.join(path[0:-len(filename)-4],filename,"")
        
        if not os.path.exists(folder):
            os.mkdir(folder)
            
        totalpage = len(images)
        
        print(colored("> Saving...","yellow"))
        for p,image in enumerate(images):
            percent = round(20*(p)/totalpage)
            processed = '■'*percent
            pending = '□'*(20-percent)
            print(f"Page:{p}/{totalpage} | ["+colored(processed,"green")+colored(pending,"red")+"]",end="\r")
            image.save(f"{folder}{filename}_P{p+1}.png","PNG")
        print(f"Page:{totalpage}/{totalpage} | ["+colored('■'*20,"green")+"]")
        print(colored("> Done!","yellow"))
        print(f"Elapsed time:{round(time.time()-ct,2)} seconds.")
        os.startfile(folder)
        print("\n" + '-'*30 + '\n')