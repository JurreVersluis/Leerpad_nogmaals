from RobotArm import RobotArm
import pygame
import sys
import random

robotArm = RobotArm('exercise 3')

# Jouw python instructies zet je vanaf hier:

for i in range(4):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait(10)