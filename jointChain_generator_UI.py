import maya.cmds as mc

# If there already exists the window we're creating
if mc.window("mkJnt_win", ex=True):
    # Close it
    mc.deleteUI("mkJnt_win", window=True)
    
# Create the window, static 100 width, not resizable
mc.window("mkJnt_win", t="Joint Generator", w=100, s=False)
# Create an adjustable column layout (stretch to width of window)
mc.columnLayout("c_Layout", adj=True)
mc.separator()
# First section for naming, quantity, and orientation
mc.text("DEFINE JOINT(S)")
mc.separator()

mc.textFieldGrp("jntName", label="Name of Prefix:")
mc.textFieldGrp("jntAmount", label="Number of Joints:")
mc.textFieldGrp("jntSpacing", label="Joint Spacing:")
mc.separator()

mc.text("CHOOSE AN ORIENTATION FOR CHAIN")
mc.separator()

mc.button("b_xyz", label="XYZ", h=30, c="xyz()", p="c_Layout")
mc.button("b_zxy", label="ZXY", h=30, c="zxy()", p="c_Layout")
mc.button("b_yzx", label="YZX", h=30, c="yzx()", p="c_Layout")

mc.showWindow("mkJnt_win")

def xyz():
    #q -> Query, tx -> Text
    jointName = mc.textFieldGrp("jntName", q=True, tx=True)
    jointAmount = mc.textFieldGrp("jntAmount", q=True, tx=True)
    jointSpacing = mc.textFieldGrp("jntSpacing", q=True, tx=True)
    # Clear selection so joints aren't parented
    mc.select(cl=True)
    
    if jointAmount == "1":
        jntSingle = mc.joint(n=jointName)
        mc.setAttr(jntSingle + ".jointOrientX", -90)
        mc.setAttr(jntSingle + ".jointOrientY", 0)
        mc.setAttr(jntSingle + ".jointOrientZ", 90)
    else:        
        for x in range(int(jointAmount)):
            mc.joint(n=(jointName + "_%d") % x)
            # Offset for each joint
            jntPos = (x * float(jointSpacing))
            # Space out joints
            mc.move(0, jntPos, 0)
        
        # oj -> Orient Joint, ch -> Children; only affects up until the last joint
        mc.joint((jointName + "_0"), edit=True, oj="xyz", secondaryAxisOrient="yup", ch=True)
        
        # Zero out orientation of last joint so it matches that of the parent, which will match the rest of the chain
        # ls for Last Selection
        selLastJnt = mc.ls(sl=True)
        mc.setAttr(selLastJnt[0] + ".jointOrientX", 0)
        mc.setAttr(selLastJnt[0] + ".jointOrientY", 0)
        mc.setAttr(selLastJnt[0] + ".jointOrientZ", 0)
        
def zxy():
    #q -> Query, tx -> Text
    jointName = mc.textFieldGrp("jntName", q=True, tx=True)
    jointAmount = mc.textFieldGrp("jntAmount", q=True, tx=True)
    jointSpacing = mc.textFieldGrp("jntSpacing", q=True, tx=True)
    # Clear selection so joints aren't parented
    mc.select(cl=True)
    
    if jointAmount == "1":
        jntSingle = mc.joint(n=jointName)
        mc.setAttr(jntSingle + ".jointOrientX", -90)
        mc.setAttr(jntSingle + ".jointOrientY", 0)
        mc.setAttr(jntSingle + ".jointOrientZ", 0)
    else:        
        for x in range(int(jointAmount)):
            mc.joint(n=(jointName + "_%d") % x)
            # Offset for each joint
            jntPos = (x * float(jointSpacing))
            # Space out joints
            mc.move(0, jntPos, 0)
        
        # oj -> Orient Joint, ch -> Children; only affects up until the last joint
        mc.joint((jointName + "_0"), edit=True, oj="zxy", secondaryAxisOrient="yup", ch=True)
        
        # Zero out orientation of last joint so it matches that of the parent, which will match the rest of the chain
        # ls for Last Selection
        selLastJnt = mc.ls(sl=True)
        mc.setAttr(selLastJnt[0] + ".jointOrientX", 0)
        mc.setAttr(selLastJnt[0] + ".jointOrientY", 0)
        mc.setAttr(selLastJnt[0] + ".jointOrientZ", 0)
        
def yzx():
    #q -> Query, tx -> Text
    jointName = mc.textFieldGrp("jntName", q=True, tx=True)
    jointAmount = mc.textFieldGrp("jntAmount", q=True, tx=True)
    jointSpacing = mc.textFieldGrp("jntSpacing", q=True, tx=True)
    # Clear selection so joints aren't parented
    mc.select(cl=True)
    
    if jointAmount == "1":
        jntSingle = mc.joint(n=jointName)
        mc.setAttr(jntSingle + ".jointOrientX", 0)
        mc.setAttr(jntSingle + ".jointOrientY", 0)
        mc.setAttr(jntSingle + ".jointOrientZ", 0)
    else:        
        for x in range(int(jointAmount)):
            mc.joint(n=(jointName + "_%d") % x)
            # Offset for each joint
            jntPos = (x * float(jointSpacing))
            # Space out joints
            mc.move(0, jntPos, 0)
        
        # oj -> Orient Joint, ch -> Children; only affects up until the last joint
        mc.joint((jointName + "_0"), edit=True, oj="yzx", secondaryAxisOrient="yup", ch=True)
        
        # Zero out orientation of last joint so it matches that of the parent, which will match the rest of the chain
        # ls for Last Selection
        selLastJnt = mc.ls(sl=True)
        mc.setAttr(selLastJnt[0] + ".jointOrientX", 0)
        mc.setAttr(selLastJnt[0] + ".jointOrientY", 0)
        mc.setAttr(selLastJnt[0] + ".jointOrientZ", 0)