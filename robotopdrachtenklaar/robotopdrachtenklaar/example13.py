from RobotArm import RobotArm

robotArm = RobotArm('exercise 13')
robotArm.randomLevel(1,7)
x = 1
scan = True
# Jouw python instructies zet je vanaf hier:
while scan:
    robotArm.grab()
    scan = robotArm.scan()
    if scan:
        for i in range(x):
            robotArm.moveRight()
        robotArm.drop()
        for y in range(x):
            robotArm.moveLeft()
        x += 1

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait(10)