# Clicks count

The present script - ```clicks_count.py``` could create the shorter website link than you have.
Also, if the short link already exist, you could count total clicks quantity for this link. The
getting clicks amount where for all time of using this link.

### How to install

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### How to use

Before using this script, you need to login to Bitly service for this link: [bitly.com](https://app.bitly.com/)
After that, you have to get token on Bitly site. Token has name ```GENERIC_ACCESS_TOKEN```.
It's look like this string: ```17c09e20ad155405123ac1977542fecf00231da7```.
For script work correctly, you must create ```.env``` file in the script directory.
This file have to consider one line with bitly servise token. The example of this line below:
```
GENERIC_ACCESS_TOKEN=17c09e20ad155405123ac1977542fecf00231da7
```
For script running you have to start the command line and change directory to the code containing.
The next step is start the script for this template:
```
[full_dir_path] python click_count.py [full_link]
```
For example: 
```
d:\CODING\DEVMAN\Click_Count>python main.py https://dvmn.org/modules/web-api
```

### Output results

As results you get shorten link, as name is bitlink. For example: ```Bitlink :  https://bit.ly/3pDYRyx```.
Count clicks are outputs as for next example: ```Bitlinks clicks count: 0```
If you want to count clicks amount on short link, you must start script for this template: 
```
[full_dir_path] python click_count.py [bitlink]
```
If you make mistake in link input, script get the following message: ```Incorrect link inputed. Please restart script```
In this case, you need to restart script.

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).