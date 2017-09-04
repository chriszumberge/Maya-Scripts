'''
The Pose Saver
Instructions: run the code.  Then select the object(s) you'd like to bookmark and click on any Symbol Button to save a specific pose

'''

#Import the Maya Command module
import maya.cmds as mc

#Condition statement that checks if our window already exists
if mc.window("poseWindow", ex=True):
    #If the above condition is met, then prevent the window from being cloned
    mc.deleteUI("poseWindow", window=True)
#Create a window and make it resizable
mc.window("poseWindow", t="The Pose Saver", wh=(500, 500), s=True)
#Create a Form Layout
myForm = mc.formLayout()
#Create a Tab Layout
myTabs = mc.tabLayout()
#Edit our Form Layout
mc.formLayout(myForm, edit=True, attachForm=[(myTabs, "top", 10), (myTabs, "bottom", 10), (myTabs, "left", 10), (myTabs, "right", 10)])
#Create a Column Layout for our first tab
mkPose_layout = mc.columnLayout()
#Create a Shelf Layout under the Column Layout above
poseShelf = mc.shelfLayout(w=455, h=300)
#Add Symbol Buttons that will save a Shelf Button under our Body, Face, and Misc tabs
mkPose_b_body = mc.symbolButton(image = "mkPoseTool_img_maya_body.jpg", w=150, h=150, c="createShelfButton_body(bodyShelf)")

mkPose_b_face = mc.symbolButton(image = "mkPoseTool_img_maya_face.jpg", w=150, h=150, c="createShelfButton_face(faceShelf)")

mkPose_b_misc = mc.symbolButton(image = "mkPoseTool_img_maya_misc.jpg", w=150, h=150, c="createShelfButton_misc(miscShelf)")
#Use this function to move back to the upper level of our window, in order to create another tab next to the first
mc.setParent("..")

mc.setParent("..")
#Create a Column Layout for our second tab
bodyCtrl_layout = mc.columnLayout()
#Create a Shelf Layout under the Column Layout above
bodyShelf = mc.shelfLayout(w=500, h=500)
#Use this function to move back to the upper level of our window, in order to create another tab next to the second
mc.setParent("..")

mc.setParent("..")
#Create a Column Layout for our third tab
faceCtrl_layout = mc.columnLayout()
#Create a Shelf Layout under the Column Layout above
faceShelf = mc.shelfLayout(w=500, h=500)
#Use this function to move back to the upper level of our window, in order to create another tab next to the third
mc.setParent("..")

mc.setParent("..")
#Create a Column Layout for our fourth and final tab
miscCtrl_layout = mc.columnLayout()
#Create a Shelf Layout under the Column Layout above
miscShelf = mc.shelfLayout(w=500, h=500)
#Use this function to move back to the upper level of our window, in order to create another tab next to the third
mc.setParent("..")

mc.setParent("..")
#Edit our Tab Layout
mc.tabLayout(myTabs, edit=True, tabLabel=[(mkPose_layout, "Pose Types"), (bodyCtrl_layout, "Body Poses"), (faceCtrl_layout, "Facial Poses"), (miscCtrl_layout, "Misc Poses")])
#Show our window
mc.showWindow("poseWindow")

#Create a function that will add a Shelf Button under the Body Poses tab
def createShelfButton_body(targetShelf_body):
    #This variable will store the information that our Shelf Button will hold.  We make sure it's empty so our information doesn't continue to pile everytime we use this tool
    storeCmds_body = ""
    
    #This variable stores our selection
    selPose = mc.ls(sl=True)
    
    #Condition statement that checks the size of our selection
    if len(selPose) < 1:
        #If the condition above is met, then print this warning message
        mc.warning("Must select at least one object!")
    #If the condition above is not true, then run the following commands    
    else:
        #'For' loop - for all items in our selection, run the following commands
        for all in selPose:
            #This variable holds all keyable, readable, writeable, connectable, and unlocked channels of the item(s) selected
            keyable = mc.listAttr(all, k=True, r=True, w=True, c=True, u=True)
            #This line prints the data stored in our "keyable" variable
            print keyable
            #'For' loop - for all stored keyable channels, run the following commands
            for vals in keyable:
                #This variable stores the values of all stored keyable channels
                findVal = mc.getAttr(all + "." + vals)
                #This line prints the data stored in our "findVal" variable
                print findVal
                #This variable stores the string "setAttr " that will be used to set our channels back to the values stored in our Shelf Button
                startCode = "setAttr "
                #This varaible stores the end syntax of the code stores in our Shelf Button.  It, essentially, adds a ";" at the end of each line and uses "\n" to print our data vertically
                endCode = ";\n"
                #This variable stores the command(s) that allow us to revert back to the pose(s)/bookmark(s) we save
                saveToShelf = (startCode + (all + "." + vals) + " %f" + endCode) % findVal
                #This is the first variable we created above.  It's used to store the information of "saveToShelf" so we can add it to our Shelf Button's command
                storeCmds_body += saveToShelf
                #This line prints the data stored in our "storeCmds_body" variable
                print storeCmds_body
        #This variable stores our Prompt Dialog         
        pd_body = mc.promptDialog(t="Body Pose", m="Name of Pose?", b="Save It!")
        #Condition statement that checks if our button gets clicked.  If this condition is met, then run the following commands
        if pd_body == "Save It!":
            #This variable stores the Name we add to our Prompt Dialog
            pd_body_name = mc.promptDialog(q=True, text=True)
            #This line creates our Shelf Button that uses MEL as the source type for the commands stored in "storeCmds_body", and adds the Shelf Button under our custom tab named "Body Poses"
            mc.shelfButton(l=pd_body_name, annotation=pd_body_name, imageOverlayLabel=pd_body_name, i1="Pose_Body_image.jpg", command=storeCmds_body, p=targetShelf_body, sourceType="mel")

#Create a function that will add a Shelf Button under the Facial Poses tab            
def createShelfButton_face(targetShelf_face):
    #This variable will store the information that our Shelf Button will hold.  We make sure it's empty so our information doesn't continue to pile everytime we use this tool
    storeCmds_face = ""
    
    #This variable stores our selection
    selPose = mc.ls(sl=True)
    
    #Condition statement that checks the size of our selection
    if len(selPose) < 1:
        #If the condition above is met, then print this warning message
        mc.warning("Must select at least one object!")
    #If the condition above is not true, then run the following commands    
    else:
        #'For' loop - for all items in our selection, run the following commands
        for all in selPose:
            #This variable holds all keyable, readable, writeable, connectable, and unlocked channels of the item(s) selected
            keyable = mc.listAttr(all, k=True, r=True, w=True, c=True, u=True)
            #This line prints the data stored in our "keyable" variable
            print keyable
            #'For' loop - for all stored keyable channels, run the following commands
            for vals in keyable:
                #This variable stores the values of all stored keyable channels
                findVal = mc.getAttr(all + "." + vals)
                #This line prints the data stored in our "findVal" variable
                print findVal
                #This variable stores the string "setAttr " that will be used to set our channels back to the values stored in our Shelf Button
                startCode = "setAttr "
                #This varaible stores the end syntax of the code stores in our Shelf Button.  It, essentially, adds a ";" at the end of each line and uses "\n" to print our data vertically
                endCode = ";\n"
                #This variable stores the command(s) that allow us to revert back to the pose(s)/bookmark(s) we save
                saveToShelf = (startCode + (all + "." + vals) + " %f" + endCode) % findVal
                #This is the first variable we created above.  It's used to store the information of "saveToShelf" so we can add it to our Shelf Button's command
                storeCmds_face += saveToShelf
                #This line prints the data stored in our "storeCmds_face" variable
                print storeCmds_face
        #This variable stores our Prompt Dialog         
        pd_face = mc.promptDialog(t="Face Pose", m="Name of Pose?", b="Save It!")
        #Condition statement that checks if our button gets clicked.  If this condition is met, then run the following commands
        if pd_face == "Save It!":
            #This variable stores the Name we add to our Prompt Dialog
            pd_face_name = mc.promptDialog(q=True, text=True)
            #This line creates our Shelf Button that uses MEL as the source type for the commands stored in "storeCmds_face", and adds the Shelf Button under our custom tab named "Facial Poses"
            mc.shelfButton(l=pd_face_name, annotation=pd_face_name, imageOverlayLabel=pd_face_name, i1="Pose_Face_image.jpg", command=storeCmds_face, p=targetShelf_face, sourceType="mel")

#Create a function that will add a Shelf Button under the Misc Poses tab            
def createShelfButton_misc(targetShelf_misc):
    #This variable will store the information that our Shelf Button will hold.  We make sure it's empty so our information doesn't continue to pile everytime we use this tool
    storeCmds_misc = ""
    
    #This variable stores our selection
    selPose = mc.ls(sl=True)
    
    #Condition statement that checks the size of our selection
    if len(selPose) < 1:
        #If the condition above is met, then print this warning message
        mc.warning("Must select at least one object!")
    #If the condition above is not true, then run the following commands    
    else:
        #'For' loop - for all items in our selection, run the following commands
        for all in selPose:
            #This variable holds all keyable, readable, writeable, connectable, and unlocked channels of the item(s) selected
            keyable = mc.listAttr(all, k=True, r=True, w=True, c=True, u=True)
            #This line prints the data stored in our "keyable" variable
            print keyable
            #'For' loop - for all stored keyable channels, run the following commands
            for vals in keyable:
                #This variable stores the values of all stored keyable channels
                findVal = mc.getAttr(all + "." + vals)
                #This line prints the data stored in our "findVal" variable
                print findVal
                #This variable stores the string "setAttr " that will be used to set our channels back to the values stored in our Shelf Button
                startCode = "setAttr "
                #This varaible stores the end syntax of the code stores in our Shelf Button.  It, essentially, adds a ";" at the end of each line and uses "\n" to print our data vertically
                endCode = ";\n"
                #This variable stores the command(s) that allow us to revert back to the pose(s)/bookmark(s) we save
                saveToShelf = (startCode + (all + "." + vals) + " %f" + endCode) % findVal
                #This is the first variable we created above.  It's used to store the information of "saveToShelf" so we can add it to our Shelf Button's command
                storeCmds_misc += saveToShelf
                #This line prints the data stored in our "storeCmds_misc" variable
                print storeCmds_misc
        #This variable stores our Prompt Dialog         
        pd_misc = mc.promptDialog(t="Misc Pose", m="Name of Pose?", b="Save It!")
        #Condition statement that checks if our button gets clicked.  If this condition is met, then run the following commands
        if pd_misc == "Save It!":
            #This variable stores the Name we add to our Prompt Dialog
            pd_misc_name = mc.promptDialog(q=True, text=True)
            #This line creates our Shelf Button that uses MEL as the source type for the commands stored in "storeCmds_misc", and adds the Shelf Button under our custom tab named "Misc Poses"
            mc.shelfButton(l=pd_misc_name, annotation=pd_misc_name, imageOverlayLabel=pd_misc_name, i1="Pose_Misc_image.jpg", command=storeCmds_misc, p=targetShelf_misc, sourceType="mel")