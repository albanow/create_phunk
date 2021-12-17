import requests
import utilities as ut

phunk_id = "1"
bid = False

if len(phunk_id) == 1:
    phunk_id = "00" + phunk_id
elif len(phunk_id) == 2:
    phunk_id = "0" + phunk_id

image_name = "phunk"+phunk_id+".png"

link_nft_image = "https://phunks.s3.us-east-2.amazonaws.com/images/"+image_name

response = requests.get(link_nft_image)
file = open(image_name, "wb")
file.write(response.content)
file.close()

file.close()
if bid:
    ut.create_background(image_name, (152, 87, 183))
else:
    ut.create_background(image_name, (96, 131, 151))
