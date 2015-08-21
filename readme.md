**This version is for the older MJPEG firmware on the 8918 series (11.22.X>X)**


py_foscam_labcam is a python script to control the PTZ cam at FamiLAB

v0.7 - 5/29/2015

fi8918w.py code has been modified from https://github.com/jasenmh/pyFoscamLib 

Dependencies:
    imgurpython - https://github.com/Imgur/imgurpython
    Pillow (PIL fork) - https://python-pillow.github.io/
    requests - http://docs.python-requests.org/en/latest/
    twitter - https://pypi.python.org/pypi/twitter

    Contact David@FamiLAB.org for file with API keys. 

    Main script is pan_and_tweet.py which will make the camera position itself 
    to take 7 consecutive images, panning to the right each time to make a 
    panorama. 

    It then concatenates all the images into a simple pano, and uploads that to 
    imgur, then tweets that imgur link.

ToDo:
    Make cam only upload images when it detects a change from last capture.
    Make cam progress through panning and taking the images faster.
    Make pano actually stitch together rather than just side by side images.

Done:
    Authenticate to cam
    Move and tilt
    Capture images and save to file
    Cat images together side by side
    Upload to imgur anonymously
    Make api keys, config and credentials load from environment variables.
    Make imgur link automatically tweet on Famduino acct.
