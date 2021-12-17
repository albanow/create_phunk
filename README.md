
# Create Phunk image

Tool to create a Phunk image with a custom background

## Installation
Clone the repo
```
git clone https://github.com/albanow/etherscan_sales_bot.git
```
Move to a virtual environment (pipenv used for the example)
```
pipenv shell
```

Install dependencies
```
pip install -r requirements.txt
```
Default parameters, will create an image of size 240x240 (default) with the original backgound color
```
python -m app.create_phunk -id=7017
```
![phunk org](https://raw.githubusercontent.com/albanow/phunk-images/main/Phunk_7017.png)

Custom size, will create an image of size wxhe with the original backgound color
```
python -m app.create_phunk -id=7017 -w=500 -he=500
```
![phunk bigger](https://raw.githubusercontent.com/albanow/phunk-images/main/Phunk_7017_500x500.png)

Custom background color, will create an image of default size with a custom background color
```
python -m app.create_phunk -id=7017 -c="38, 199, 20"
```
![phunk color](https://raw.githubusercontent.com/albanow/phunk-images/main/Phunk_7017_green.png)

Custom background image, will create an image of default size with a custom background image
```
python -m app.create_phunk -id=7017 -img="example.png"
```
![phunk image](https://raw.githubusercontent.com/albanow/phunk-images/main/Phunk_7017_image.png)

Custom background image and custom size, will create an image of custom size with a custom background image
```
python -m app.create_phunk -id=7017 -w=500 -he=500 -img="images.jpg"
```
![phunk beach](https://raw.githubusercontent.com/albanow/phunk-images/main/Phunk_7017_beach.png)

Run the following code to see all the available parameters
```
python -m app.create_phunk -h
```

### Donations
ETH: 0x8143978e687066F635515BD28E0d9D070FAcEb4B


Twitter: [albanow](https://twitter.com/albanow10)