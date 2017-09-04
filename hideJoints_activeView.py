import maya.cmds as cmds

# get the active view, finding the panel with focus
activeView = cmds.getPanel(wf=True)

# If the model editor in the active view has joints on
if cmds.modelEditor(activeView, q=True, joints=True) == 1:
    # Now in edit mode, set joints to false
    cmds.modelEditor(activeView, e=True, joints=False)