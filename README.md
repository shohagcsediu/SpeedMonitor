# SpeedMonitor
SpeedMonitor always monitor and update your internet live usage speed.
Version 0.0.1

  ![SpeedMonitor](https://imgur.com/fvQXRil.png "SpeedMonitor")

  ![SpeedMonitor](https://imgur.com/v62XXy3.png "SpeedMonitor")

### Required to install
1. First clone this repo using this command:  
    `$ git clone https://github.com/shohagcsediu/SpeedMonitor`
2. Now install the required packages:  
    `$ pip install psutil` and 
    `$ pip install pyinstaller`
4. Run to see the preview
5. Want to make it exe file?  let's build it. Run this command:
 `$ pyinstaller --onefile --windowed --icon=speed.ico speedMonitor.py`

Note: here speed.ico is the icon file that you want to use as your file icon, and speedMonitor.py file that you have clone from this repo, keep both file together, and run the command.
You will see the exe file generated on your dist folder on the same directory. Now you can use it anywhere or share with other people.
