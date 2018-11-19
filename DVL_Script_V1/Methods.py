
def Print_Velocity_Information(__dataEnsemble__):
    velocity_ID = '0100'
    velocityBegin = __dataEnsemble__.rfind(velocity_ID)
    velocity = __dataEnsemble__[velocityBegin: velocityBegin + 242]
    print(velocity)
