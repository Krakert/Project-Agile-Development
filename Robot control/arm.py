
class arm:

    def moveArm(self, session, left_Richt, joints = [], angles = [], timeTocomplete = [], ):
        motion = session.service("ALMotion")
        motion.setStiffnesses("Head", 0.5)
        names = joints
        arrayOfRad = []
        for x in range(len(angles)):
            arrayOfRad.append(math.radians(angles[x]))
        angleLists = arrayOfRad
        timeLists = timeTocomplete
        isAbsolute = True
        motion.angleInterpolation(names, angleLists, timeLists, isAbsolute)