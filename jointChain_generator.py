import maya.cmds as mc

for x in range(5):
    mc.joint(n="jntSpine_%d" % x)
    # Offset for each joint
    jntPos = x * 5
    # Space out joints
    mc.move(0, jntPos, 0)

# oj -> Orient Joint, ch -> Children; only affects up until the last joint
mc.joint("jntSpine_0", edit=True, oj="xyz", secondaryAxisOrient="yup", ch=True)

# Zero out orientation of last joint so it matches that of the parent, which will match the rest of the chain
# ls for Last Selection
selLastJnt = mc.ls(sl=True)
mc.setAttr(selLastJnt[0] + ".jointOrientX", 0)
mc.setAttr(selLastJnt[0] + ".jointOrientY", 0)
mc.setAttr(selLastJnt[0] + ".jointOrientZ", 0)