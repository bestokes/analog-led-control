# Introduction

A quick and dirty web page with buttons to manage an LED strip. 

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
* put the buttons.css into /css/ and the buttons.js into /js/ - from here http://unicorn-ui.com/buttons/builder/ 
