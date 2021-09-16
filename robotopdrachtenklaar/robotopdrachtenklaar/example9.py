from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

# Jouw python instructies zet je vanaf hier:

for i in range(3):
    robotArm.moveRight()

for blokStapel in range(4):
    for x in range(4-blokStapel):
        robotArm.grab()

        for i in range(5):
            robotArm.moveRight()

        robotArm.drop()

        for i in range(5):
            robotArm.moveLeft()

    robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait(10)