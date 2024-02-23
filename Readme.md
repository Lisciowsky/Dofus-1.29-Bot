# Dofus Bot 1.29 Retro - Educational Project

## Introduction

Welcome to the Dofus Bot 1.29 Retro repository. This project is an exploratory venture into the realm of image processing and automation within the context of MMORPGs, specifically designed for educational purposes. The motivation behind sharing this code is to fill a gap found during research on GitHub related to image processing bots in gaming environments. It's a testament to curiosity and learning about automated interactions in a controlled setting.

Disclaimer: This software is strictly for educational insight and should not be utilized within Dofus or any other MMORPG to gain an unfair advantage. The project is shared to inspire and educate on the possibilities within programming and image processing, not to encourage misuse against game policies.

---

### Development Background
This project was developed during my spare time over a few days, reflecting a passion-driven exploration rather than a polished product. The rapid development cycle means the software is in an early stage, serving more as a proof of concept and learning tool rather than a finished utility.

### Libraries and Their Purposes
In the creation of this bot, two primary libraries were utilized to simulate user interaction and analyze visual data:

- PyAutoGUI: This library is instrumental in simulating mouse movements and clicks, allowing the bot to interact with the game environment through cursor manipulation based on specified X and Y coordinates.

- OpenCV (Open Source Computer Vision Library): A pivotal tool for image detection, OpenCV enables the bot to identify specific elements within the game's visuals and retrieve their coordinates. This capability forms the foundation for responsive actions based on the game's current state.

By integrating PyAutoGUI's simulation capabilities with OpenCV's image detection, the bot can autonomously perform actions in response to visual cues, mimicking player interactions.

### Core Components
The bot's architecture is comprised of several key components:

image_detector.py: This module houses the ImageDetector class, responsible for comparing screenshots against predefined images (e.g., monsters, trees) to identify game elements.

detection.py: Contains the Detection class, which manages the lifecycle of detection threads. Through this class, detection processes can be initiated, paused, or stopped, accommodating various bot operation modes. The Detection class utilizes instances of ImageDetector to perform its tasks.

main.py: The entry point of the bot, featuring an infinite loop that orchestrates the detection threads. This script continuously updates screenshots for analysis and adjusts the bot's behavior based on detection outcomes.

Conclusion
This project is shared with the hope that it will serve as a valuable resource for those interested in the intersection of gaming, automation, and image processing. It showcases a basic yet effective approach to creating a bot that can navigate and interact with a game environment in a meaningful way.

As a creator, I encourage responsible use and adherence to the educational purpose of this software. The exploration of such technologies opens doors to understanding complex systems and the potential for automation, offering insights that extend far beyond gaming.

![alt text](https://github.com/Lisciowsky/Dofus-1.29-Bot/blob/main/diagram.png?raw=true)
