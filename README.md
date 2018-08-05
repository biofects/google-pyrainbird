### Google-pyRainbird

Allow voice control of Rainbird Sprinkler Wifi. This will allow you to start a program and stop the irrigation.
Biofects, is not affiliated with Rainbird corperation or its affailites.  This application relies to be run in Docker with a simple build and run. I run this from my Raspberry pi along my other Docker applications.

If you like this and want continous development or want other developed you can dontate here
#### Donate to get geek stuff(sorry no beer here)

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=TWRQVYJWC77E6)

#### Set up Application
1. Clone ths repo
2. Edit config.cfg (do not use quotes)
```
[apikey]
key = Add Key here*
[rainbird]
ip = IP of your Rainbird Link Module
pass = Passworf of yout Rainbird Link Module*
[programs]
a = Program a Name (use only single word i.e. (all - to run all zones)
b = Program b Name (use only single word i.e. (back - 	to run all zones in backyard)
c = Program c Name (use only single word i.e. (front - 	to run all zones in front yard)
d = Program d Name (use only single word i.e. (flowers  to run flowers drip)*
```
3. docker build -t sprinkler:latest
4. docker run -d -p `port`:5000 sprinkler:latest
5. Ensure you have port forward set up for the port you want open from ifttt

#### Set up IFTTT
Create a new Applet
##### If This
Google Assistant with simpe phrase with text ingredient.
Start water in $
##### Then That
**Webhook**
**URL**
http:// `your public IP:port`/sprinkler/<Textfiled>
**Method** 
GET
**Content Type**
applcation/json
**Body** 
{'apikey':'`key for application`'}

#### Test / Troubleshoot
Once the Docker is running you can do a simple Curl call to test
`curl -X GET local-ip:port/sprinkler/front -d {'apikey':''key you created'} -H "Content-type: Application/json"`
if you login to your running docker image, you can look at the pypython.log file for send and reply call-backs




