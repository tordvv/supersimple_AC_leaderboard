
#Function called 
def print_out(filedir):
    import json

    from os import path
    
    #Create leaderboard file. rest of code wont work 1st time if leaderboard.csv doesn't exist
    if path.exists(r"changeables\leaderboard.csv") == False:
        f = open(r"changeables\leaderboard.csv", "w")
        f.write("1track,minutes,seconds,milliseconds,timeinmilliseconds,firstname,secondname\n")


    # Open the Assigned json file and reads the best laptime of the session
    with open(filedir, 'r') as openfile:
        json_object = json.load(openfile)
    sessions = json_object['sessions']
    session = sessions[0]
    bestlaps = session["bestLaps"]
    bestlap = bestlaps[0]
    time = int(bestlap['time'])

    # Convert the laptime in milliseconds to minutes, seconds and milliseconds
    milliseconds = int(time%1000)
    seconds = int((time/1000)%60)
    minutes = int((time/(1000*60))%60)

    # Compile the times in to a readable format. Example: 79962,1,19,962
    best_time = (f"{time},{minutes},{seconds}," + ("0"*(3-len(str(milliseconds)))) + f"{milliseconds}")

    # Retrieve name of the circuit used
    track = json_object['track']
    
    # Starts function that will retrieve name, and append data to leaderboard
    openwindow(best_time, track)

    # Starts function that will sort the leaderboards, 
    # and remove duplicate track,name,lastname instances with worse lap time
    sort_and_clean_list()

    
    
#test the function
#print_out(r"watchedfiles\testfile.json")



# Program to make a simple
# input screen 

 
def openwindow(besttime, track):
    import tkinter as tk
    
    root=tk.Tk()
    
    # setting the windows size
    root.geometry()
    
    # declaring string variable
    # for storing name and last name
    name_var=tk.StringVar()
    lastname_var=tk.StringVar()


    
    
    # defining a function that will
    # get the name and last name and
    # print them on the screen
    def submit():


        name=name_var.get()
        lastname=lastname_var.get()
        print("The first name is : " + name)
        print("The last name is : " + lastname)

        name_var.set("")
        lastname_var.set("")

        # Append the new score to the leaderboard
        fw = open(r"changeables\leaderboard.csv", "a")
        fw.write(f"{track},{name},{lastname},{besttime}\n")
                


    def close():
        root.destroy()


    # creating a label for
    # name using widget Label
    name_label = tk.Label(root, text = 'First name', font=('calibre',50, 'bold'))
    
    # creating a entry for input
    # name using widget Entry
    name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',50,'normal'))
    
    # creating a label for last name
    passw_label = tk.Label(root, text = ' Last name', font = ('calibre',50,'bold'))
    
    # creating a entry for last name
    lastname_entry=tk.Entry(root, textvariable = lastname_var, font = ('calibre',50,'normal'))
    
    # creating a button using the widget
    # Button that will call the submit function
    sub_btn=tk.Button(root,text = 'Submit', command = lambda:[submit(), close()], font=("calibre", 50, "bold"))
    
    # placing the label and entry in
    # the required position using grid
    # method
    name_label.grid(row=0,column=0)
    name_entry.grid(row=0,column=1)
    passw_label.grid(row=1,column=0)
    lastname_entry.grid(row=1,column=1)
    sub_btn.grid(row=2,column=1)
    
    # performing an infinite loop
    # for the window to display
    root.mainloop()

    # Edited from source:
    # https://www.geeksforgeeks.org/python-tkinter-entry-widget/

# Sort leaderboard and remove duplicates with worse lap time
def sort_and_clean_list():
    

    fr = open(r"C:\Users\tordv\OneDrive - University of Bergen\Other\sim racing\changeables\leaderboard.csv", "r")
    
    # Read the leaderboard file and split it in to lines
    lines = fr.readlines()
    lines.sort()

    # Create a return list
    finallines = []


    for x, line in enumerate(lines):
        # Split the line in to a list
        line = line.split(',')
        #skip the first instance
        if x == 0:
            finallines.append(",".join(line))
            continue
        # Split the previous line in to a list
        lastline = lines[x-1]
        lastline = lastline.split(",")
        # Since the list is sorted from high to low, if the current line has the same track and name,
        # it has a worse laptime and does not get appended to the return list
        if line[0] == lastline[0]:
            if line[1] == lastline[1]:
                if line[2] == lastline[2]:
                     continue
                else:
                    finallines.append(",".join(line))
            else:
                finallines.append(",".join(line))
        else:
            finallines.append(",".join(line))
    
    # Overwrite the leaderboard with the new sorted and cleaned list
    fw = open(r"C:\Users\tordv\OneDrive - University of Bergen\Other\sim racing\changeables\leaderboard.csv", "w")
    fw.writelines(finallines)

# Code written and edited by Tord Vikestad