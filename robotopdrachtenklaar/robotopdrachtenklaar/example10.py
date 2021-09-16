from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')
ib = 5
ibd = 5
# Jouw python instructies zet je vanaf hier:
for i in range(5):
    robotArm.grab()
    for y in range(5):
        robotArm.moveRight()
    robotArm.drop()
    for x in range(ib - 1):
        robotArm.moveLeft()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait(10)