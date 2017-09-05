import maya.cmds as cmds

if cmds.window("cnsWin", ex=True):
    cmds.deleteUI("cnsWin", window=True)
    
cmds.window("cnsWin", wh=(200, 50), t="Constraining Tool", s=False)
# adjustable so we can bind buttons to the width
cmds.columnLayout(adj=True)

#Add a Text Scroll List to our UI, and append 3 items: "Point Constrain", "Orient Constrain", and "Parent Constrain"
cmds.textScrollList("constrainList", h=50, a=["Point Constrain", "Orient Constrain", "Parent Constrain"])

#Add a check box to enable or disable "Maintain Offset"
cmds.checkBox("chBxMaintOffset", l="Maintain Offset")

#This button will apply constraints
cmds.button(l="Click to Constrain!", c="constrain()")

#This button will remove constraints
cmds.button(l="Remove Constraint(s)", c="rmvConstraint()")

#Show the window
cmds.showWindow("cnsWin")\


def constrain():
    # si for selected item
    tsl_item = cmds.textScrollList("constrainList", q=True, si=True)
    # v for value
    if cmds.checkBox("chBxMaintOffset", q=True, v=True) == 1:
        if tsl_item[0] == "Parent Constrain":
            # mo for Maintain Offset
            cmds.parentConstraint(mo=True)
        elif tsl_item[0] == "Orient Constrain":
            cmds.orientConstraint(mo=True)
        elif tsl_item[0] == "Point Constrain":
            cmds.pointConstraint(mo=True)
    else:
        if tsl_item[0] == "Parent Constrain":
            cmds.parentConstraint()
        elif tsl_item[0] == "Orient Constrain":
            cmds.orientConstraint()
        elif tsl_item[0] == "Point Constrain":
            cmds.pointConstraint()
            
def rmvConstraint():
    tsl_item = cmds.textScrollList("constrainList", q=True, si=True)
    if tsl_item[0] == "Parent Constrain":
        selCnsObj = cmds.ls(sl=True)
        getPrtCns = cmds.listRelatives(selCnsObj, type="parentConstrain")
        cmds.delete(getPrtCns)
    elif tsl_item[0] == "Orient Constrain":
        selCnsObj = cmds.ls(sl=True)
        getOriCns = cmds.listRelatives(selCnsObj, type="orientConstrain")
        cmds.delete(getOriCns)
    elif tsl_item[0] == "Point Constrain":
        selCnsObj = cmds.ls(sl=True)
        getPtCns = cmds.listRelatives(selCnsObj, type="pointConstrain")
        cmds.delete(getPtCns)