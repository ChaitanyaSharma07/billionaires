from ntpath import join
import tkinter
from cv2 import bitwise_or, sort
import requests
import json
import urllib.request
from PIL import ImageTk, Image
#-----------------------------------------

request = requests.get("https://forbes400.herokuapp.com/api/forbes400/getAllBillionaires")

data = request.json()

top_10 = []

for i in range(10):
    person = data[i]["person"]["name"]
    rank = data[i]["rank"]
    image_url = data[i]["person"]["squareImage"]
    net_worth = data[i]["finalWorth"]
    bios_list = data[i]["bios"]

    bios = ""

    for i in range(0, 1):
        bios += bios_list[i]

    details = [person, rank, net_worth, bios, image_url]
    
    top_10.append(details)
    


#saving images
img_name = ""
img_url = ""

for i in range(len(top_10)):
    img_name = top_10[i][0]
    img_url = top_10[i][4]
    rank = top_10[i][1]

    for i in img_url:
        if "https:" in img_url:
            urllib.request.urlretrieve(img_url, img_name + "_" +  str(rank) + ".jpg")
        else:
            img_url = "https:" + img_url


#-----------------------------------------------

for i in range(len(top_10)):
    print("RANK " + str(top_10[i][1]) + ".")
    print("NAME: " + str(top_10[i][0]))

    print("--------------------------------")

print("To see more details type out the rank of the person")
print("---------------------")

print(top_10[0])


person = ""
net_worth = 0
bios = ""
#-----------------------------------------

while 1:
    inp = int(input(""))
    
    rank = inp

    for i in range(len(top_10)):
        if top_10[i][1] == rank:
            person = top_10[i][0]
            net_worth = top_10[i][2]
            bios_list = top_10[i][3]

            root = tkinter.Tk()

            rank_label = tkinter.Label(root, text="RANK " + str(rank))
            rank_label.pack()

            person_label = tkinter.Label(root, text=person)
            person_label.pack()

            net_label = tkinter.Label(root, text="Net Worth: " + str(net_worth))
            net_label.pack()


            img = ImageTk.PhotoImage(Image.open(person + "_" + str(rank) + ".jpg"))
            panel = tkinter.Label(root, image = img)
            panel.pack()
            
            bios_label = tkinter.Label(root, text=bios_list)
            bios_label.pack()
            

            #for j in range(len(bios_list)):
             #   bio = bios_list[j]
              #  bios_label = tkinter.Label(root, text=bio)

            root.mainloop()