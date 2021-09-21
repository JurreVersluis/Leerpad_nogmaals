from RobotArm import RobotArm
import pygame
import sys
import random

robotArm = RobotArm('exercise 4')

# Jouw python instructies zet je vanaf hier:

robotArm.grab()
for i in range(3):
    robotArm.moveRight()
robotArm.drop()
for i in range(3):
    robotArm.moveLeft()
robotArm.grab()
for i in range(2):
    robotArm.moveRight()
robotArm.drop()
for i in range(2):
    robotArm.moveLeft()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
robotArm.moveRight()
robotArm.grab()
robotArm.moveLeft()
robotArm.drop()
for i in range(2):
    robotArm.moveRight()
robotArm.grab()
for i in range(2):
    robotArm.moveLeft()
robotArm.drop()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait(10)