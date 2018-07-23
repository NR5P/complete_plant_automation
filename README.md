# Complete Plant Automation
A project to be able allow complete automation of growing plants using the raspberry pi. Irrigation, grow lights, temperature control, and more. Multi platform apps to allow control over wifi network. Temperature, humidity, and other feedback to allow monitoring.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## control of 
* irrigation valves
* grow lights
* temperature control
* more later

## flexibility
* multi platform apps for any device
* able to control from anywhere over wifi network
* able to attach display directly to raspberry pi for direct operation
* monitor temperature, humidity, and more via feedback sensors from any app

## why
I decided to pursue this project because I was propagating plants and was using other products that didn't provided the settings I needed. There actually aren't very many options for timers to control valves for irrigating plants. Plant misting systems need quick short bursts of water for just a few seconds every few minutes. The products I was using had odd user interfaces that I found myself needing a manual to use, they were also expensive for what they offered I felt. 

I also wanted greater functionality as I had normal garden irrigation needs and I had tropical plants that needed to grow in doors with grow lights. I wanted a do it all timer that I could continue to add options to and was a single unit. I also wanted to build something open source that anyone could modify according to their needs. 

## gui
I'm using flask for the gui. User will be able to access raspbery pi by typing in the IP address of the pi,
which will return the gui in the web browser.

## progress
- [x] general program finished
- [x] plant irrigation valve timers
- [ ] lights timer
- [ ] gui 
- [x] network socket control over terminal
- [ ] temperature sensor capability
- [ ] humidity sensor capability

##problems
I'm thinking about the best way for a user to add the controller to their network, I can only think of two ways
of doing this
- by adding an lcd or touchscreen to the raspberry pi to add wifi password
- for the user to temporarily plug in an hdmi monitor to add the wifi password.  

I don't like either of these methods. I don't think using a small screen connected to the device is a very 
efficient way of setting the timers, not nearly as easy as using a web browser. Also it's another point of failure.

If anyone has a better idea or something I haven't thought about please let me know.

## Contact
Name: Nathan Rigg  
Email: [orangev8zcar@gmail.com](orangev8zcar@gmail.com)  
Website: [nr5p.com](nr5p.com)

