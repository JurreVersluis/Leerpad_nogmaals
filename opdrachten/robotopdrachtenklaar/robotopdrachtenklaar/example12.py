from RobotArm import RobotArm
count = 9
count2 = 1
robotArm = RobotArm('exercise 12')
kleur = "null"

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3
for i in range(50):
    robotArm.grab()
    kleur = robotArm.scan()
    print(kleur)
    if kleur == "red":
        for x in range(9):
            robotArm.moveRight()
        robotArm.drop()
        for y in range(9):
            robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveRight()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait(10)