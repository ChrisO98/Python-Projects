# GIF Creator A program that puts together multiple images (PNGs, JPGs, TIFFs) to make a smooth GIF that can be exported
# Optional: Make the program convert small video files to GIFs as well.

# import the library
from appJar import gui
from tkinter import *
from PIL import Image, ImageTk
import imageio


# Handle Button Events
def press(button):
    if button == "Upload":
        app.startLabelFrame("Images")
        # Set it up to where you can upload less than 6 images and not get an error
        user_input = app.getEntry("File Directory of Image 1")
        if user_input == "":
            pass
        else:
            photo1 = Image.open(user_input)
            photo11 = photo1.resize((200, 200), Image.ANTIALIAS)
            pic1 = ImageTk.PhotoImage(photo11)
            app.addImageData("pic 1", pic1, 0, 0, 3, 1, fmt="PhotoImage")

        usr_in = app.getEntry("File Directory of Image 2")
        if usr_in == "":
            pass
        else:
            photo2 = Image.open(usr_in)
            photo22 = photo2.resize((200, 200), Image.ANTIALIAS)
            pic2 = ImageTk.PhotoImage(photo22)
            app.addImageData("pic 2", pic2, 1, 0, 3, 1, fmt="PhotoImage")

        usr_in3 = app.getEntry("File Directory of Image 3")
        if usr_in3 == "":
            pass
        else:
            photo3 = Image.open(usr_in3)
            photo33 = photo3.resize((200, 200), Image.ANTIALIAS)
            pic3 = ImageTk.PhotoImage(photo33)
            app.addImageData("pic 3", pic3, 2, 0, 3, 1, fmt="PhotoImage")

        usr_in4 = app.getEntry("File Directory of Image 4")
        if usr_in4 == "":
            pass
        else:
            photo4 = Image.open(usr_in4)
            photo44 = photo4.resize((200, 200), Image.ANTIALIAS)
            pic4 = ImageTk.PhotoImage(photo44)
            app.addImageData("pic 4", pic4, 0, 1, 3, 1, fmt="PhotoImage")

        usr_in5 = app.getEntry("File Directory of Image 5")
        if usr_in5 == "":
            pass
        else:
            photo5 = Image.open(usr_in5)
            photo55 = photo5.resize((200, 200), Image.ANTIALIAS)
            pic5 = ImageTk.PhotoImage(photo55)
            app.addImageData("pic 5", pic5, 1, 1, 3, 1, fmt="PhotoImage")

        usr_in6 = app.getEntry("File Directory of Image 6")
        if usr_in6 == "":
            pass
        else:
            photo6 = Image.open(usr_in6)
            photo66 = photo6.resize((200, 200), Image.ANTIALIAS)
            pic6 = ImageTk.PhotoImage(photo66)
            app.addImageData("pic 6", pic6, 2, 1, 3, 1, fmt="PhotoImage")

        app.stopLabelFrame()

    elif button == "Create GIF":
        # After uploading the images, you click the "Create GIF" button to make a GIF out of the images
        # Somehow compile images into a GIF
        user_input = app.getEntry("File Directory of Image 1")
        usr_in = app.getEntry("File Directory of Image 2")
        usr_in3 = app.getEntry("File Directory of Image 3")
        usr_in4 = app.getEntry("File Directory of Image 4")
        usr_in5 = app.getEntry("File Directory of Image 5")
        usr_in6 = app.getEntry("File Directory of Image 6")

        filenames = [user_input, usr_in, usr_in3, usr_in4, usr_in5, usr_in6]
        images = []
        for filename in filenames:
            images.append(imageio.imread(filename))
        gif_name = app.getEntry("Name GIF")
        if gif_name == "":
            gif_name = "Cool_GIF"
            imageio.mimsave('C:\\Users\\cbort\\Pictures\\Gif Creator\\'+gif_name+'.gif', images)
        else:
            imageio.mimsave('C:\\Users\\cbort\\Pictures\\' + gif_name + '.gif', images)

        app.startSubWindow("GIF Created", modal=True)
        app.addLabel("l10", "   The Gif has been saved in your   \n   Pictures folder.")
        app.stopSubWindow()
        app.showSubWindow("GIF Created")

    elif button == "Cancel":
        app.stop()


app = gui("GIF Creator", "1400x1200")
app.setBg("royalblue")
app.setFont(18)

app.addLabel("title", "Welcome to GIF Creator!",0,0,0,0)
app.setLabelBg("title", "red")
app.setLabelFg("title", "white")

app.addLabel("l1", "Upload the Images you want to be turned into a GIF. Then name the gif and click the Create GIF button!",1,0,0,0)

# add & configure widgets - widgets get a name, to help referencing them later
app.startLabelFrame("Upload")
app.addLabelEntry("File Directory of Image 1",0,0,1,0)
app.addLabelEntry("File Directory of Image 2",1,0,1,0)
app.addLabelEntry("File Directory of Image 3",2,0,1,0)
app.addLabelEntry("File Directory of Image 4",0,1,1,0)
app.addLabelEntry("File Directory of Image 5",1,1,1,0)
app.addLabelEntry("File Directory of Image 6",2,1,1,0)
app.stopLabelFrame()

app.addLabelEntry("Name GIF", 3)

app.setFocus("File Directory of Image 1")

app.addButtons(["Upload", "Cancel", "Create GIF"], press)

# start the GUI
app.go()
