# Dofus Bot 1.29 Retro.

Welcome to the repository.

Libraries used and purpose.

- Pyautogui. Imitate mouse movements, moving cursor to desired location given X and Y parameters.
- OpenCV. Detect specific parts on the image and retrieve its coordinates.

With combination pyautogui library that helps us imitate mouse movements and clicks and with open-cv image detection, we are able to create a bot that based on currently displayed image will be able to response and take action accordingly.

Core Components:

- image_detector.py - We can create an instance of image_detector, which is responsible for comparing the screenshot with specific looked up image (monster, tree, etc.).
- detection.py - instance of this class from which we will start and manage specific detection thread. We can stop the detection, or pause it if we are in different Bot modes. Detector will take image_detection instance.
- main.py - infinite while loop, starting the detectors threads, and updating their screenshot. Updating bot detectors results.

![alt text](https://github.com/Lisciowsky/Dofus-1.29-Bot/blob/main/diagram.png?raw=true)
