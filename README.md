# Introduction

A simple web page with buttons to manage an LED strip. 

This is a very quick and dirty project. I wrote it with cgi/bash because I wanted to do something quickly and see what could be done with pigs and a few for loops, my other reqirement was something that could be used with a touchscreen on the pi. You could also use this to remote control lights from another device on the network, like a mobile phone. The html is pretty raw, the idea is someone could take this and make something that actually looks nice. 

![ScreenShot](/screenshots/screen.jpg)

# Requirements

This tutorial will get you up and running with a RGB LED strip: http://popoklopsi.github.io/RaspberryPi-LedStrip/#/ 
You need to be running pigpiod for the cgi script to do anything.

**Then:**
```
sudo mkdir /lockfiles && sudo chown www-data /lockfiles -R
```
* install apache2 webserver and enable cgi
* put the cgi script into your cgi-bin
* put the index.html into your DocumentRoot
* download jquery into /js/ in your DocumentRoot
* the buttons came from here http://unicorn-ui.com/buttons/builder/ - put the buttons.css into /css/ in DocumentRoot
* not sure if I'm allowed to redistribute jqery and the buttons css which is why they aren't hosted here.
