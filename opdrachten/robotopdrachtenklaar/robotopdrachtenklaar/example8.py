from RobotArm import RobotArm
import pygame
import sys
import random

robotArm = RobotArm('exercise 8')

# Jouw python instructies zet je vanaf hier:
robotArm.moveRight()
for i in range(7):
    robotArm.grab()
    for a in range(8):
        robotArm.moveRight()
    robotArm.drop()
    for b in range(8):
        robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait(10)