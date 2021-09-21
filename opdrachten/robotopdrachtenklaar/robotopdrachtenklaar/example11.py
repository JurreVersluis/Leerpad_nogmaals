from RobotArm import RobotArm
count = 9
count2 = 1
robotArm = RobotArm('exercise 11')


# Jouw python instructies zet je vanaf hier:
robotArm.speed = 2
for i in range(20):
    robotArm.grab()
    Kleur = robotArm.scan()
    if Kleur == "white":
        robotArm.drop()

    else:
        for x in range(9):
            robotArm.moveRight()
        robotArm.drop()
        Kleur = "neutraal"
        for y in range(count):
            robotArm.moveLeft()
        count -= 1
    robotArm.moveRight()
for d in range(7):
    for b in range(count2):
        robotArm.moveLeft()

    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    count2 += 1

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait(10)