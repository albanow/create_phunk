#!/usr/bin/env python

import json
from web3 import Web3
import common.utilities as ut
from dotenv import load_dotenv
import argparse
import os
from cairosvg import svg2png

load_dotenv()


def tuple_type(strings):
    strings = strings.replace("(", "").replace(")", "")
    mapped_int = map(int, strings.split(","))
    return tuple(mapped_int)


parser = argparse.ArgumentParser(
    description='Image downlader from smartcontract')

parser.add_argument('-id', '--phunk_id', type=int,
                    required=True, help='ID of your Phunk pham')

parser.add_argument('-w', '--width', type=int, default=240,
                    required=False, help='Width size for final image')

parser.add_argument('-he', '--height', type=int, default=240,
                    required=False, help='Height size for final image')

parser.add_argument(
    '-b', '--bid', type=str, default='false', required=False,
    help="bid = 'true' = purple background color")

parser.add_argument(
    '-c', '--color', type=tuple_type, default="(96, 131, 151)", required=False,
    help="Background color for the final phunk image i.e '254, 278. 123' ")

parser.add_argument(
    '-img', '--image', type=str, default="none", required=False,
    help="Path of the image to use as background")

args = parser.parse_args()

phunk_id = args.phunk_id
width = args.width
height = args.height
bid = args.bid

image_back = args.image
if image_back == "none":
    rgb_color = args.color
    rgb_color = (152, 87, 183) if bid == "true" else rgb_color
else:
    rgb_color = image_back


image_name = "Phunk_"+str(phunk_id) + ".png"

# web3 API configuration (need an INFURA_URL on .env file setted)
infura_url = os.getenv("INFURA_ENDPOINT") + os.getenv("INFURA_KEY")
web3 = Web3(Web3.HTTPProvider(infura_url))

# Load ABI from smartcontract (need the json on abi.json file)
with open("common/abi.json", 'r') as openfile:
    json_abi = json.load(openfile)

# Set the smarcontract address to interact with
address = os.getenv("PUNK_ADDY")

# Create contract object to interect in the eth blockchain
contract = web3.eth.contract(address=address, abi=json_abi)

# Call punkImageSvg() from contract to download SVG image
phunk_svg = contract.functions.punkImageSvg(
    phunk_id).call().replace("data:image/svg+xml;utf8,", "")

svg2png(bytestring=phunk_svg, write_to=image_name,
        output_width=width, output_height=height)

# Flips image to the oppositive position on the y axis
ut.flip_image(image_name, "right")

ut.create_background(image_name, rgb_color)
