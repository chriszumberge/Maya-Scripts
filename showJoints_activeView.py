import maya.cmds as cmds

# get the active view, finding the panel with focus
activeView = cmds.getPanel(wf=True)

# If the model editor in the active view has joints off
if cmds.modelEditor(activeView, q=True, joints=True) == 0:
    # Now in edit mode, set joints to true
    cmds.modelEditor(activeView, e=True, joints=True)