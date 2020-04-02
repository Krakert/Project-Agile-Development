import math
class arm:
    def __init__(self):
        pass

    def moveArm(self, session, leftRight, stiffness, joints = [], angles = [], timeTocomplete = None):
        correctJoints = []
        arrayOfRadInvert = []
        arrayOfRad = []
        arrayOfTimeToComplete = []
        angleLists = None
        for x in range(len(angles)):                                                                    # Convert all angels to Rad
            if joints[x] == "Hand":
                arrayOfRad.append(angles[x])
            else:
                arrayOfRad.append(math.radians(angles[x]))                                              # And add to new array
        motion = session.service("ALMotion")                                                            # use the AlMotion API

        if leftRight.lower() == "left":                                                                 # Check wich side to use
            for x in range(len(joints)):
                correctJoints.append("L" + joints[x])
            motion.setStiffnesses("LArm", stiffness)
            angleLists = arrayOfRad

        elif leftRight.lower() == "right":
            for x in range(len(joints)):
                correctJoints.append("R" + joints[x])
                arrayOfRadInvert.append(arrayOfRad[x] * - 1)                                            # Right needs negative angels, invert them.
            leftRight
            angleLists = arrayOfRadInvert

        if type(timeTocomplete) is float:                                                               # Overloading, one speed for al joints
            for j in range (len(joints)):                                                               # Or all joints there own speed
                arrayOfTimeToComplete.append(timeTocomplete)
            timeLists = arrayOfTimeToComplete
        else:
            timeLists = timeTocomplete

        isAbsolute = True                                                                               # Absolute move, False for relative
        motion.angleInterpolation(correctJoints, angleLists, timeLists, isAbsolute)                     # Execute movement


    def moveArmToRestPosistion(self, session, leftRight):                                               # Move the arms to start posistion
        motion = session.service("ALMotion")                                                            # use the AlMotion API
        if leftRight.lower() == "left":
            motion.setStiffnesses("LArm", 0.5)
            motion.angleInterpolation(["LShoulderPitch", "LShoulderRoll",
                                       "LElbowYaw", "LElbowRoll",
                                       "LWristYaw", "LHand"],
                                      [1.43, 0.2, -1.18,
                                       -0.41, 0.10, 0.3], [2, 2, 2, 2, 2, 2], True)
        elif leftRight.lower() == "right":
            motion.setStiffnesses("RArm", 0.5)
            motion.angleInterpolation(["RShoulderPitch", "RShoulderRoll",
                                       "RElbowYaw", "RElbowRoll",
                                       "RWristYaw", "RHand"],
                                      [1.43, -0.2, 1.18,
                                       0.41, 0.10, 0.3], [2, 2, 2, 2, 2, 2], True)
