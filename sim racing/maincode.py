

def print_out(filedir):
    import json

    from os import path
    
    if path.exists(r"C:\Users\tordv\OneDrive - University of Bergen\Other\sim racing\changeables\leaderboard.csv") == False:
        f = open(r"C:\Users\tordv\OneDrive - University of Bergen\Other\sim racing\changeables\leaderboard.csv", "w")
        f.write("1track,minutes,seconds,milliseconds,timeinmilliseconds,firstname,secondname\n")


    #f = open(filedir, "r")
    with open(filedir, 'r') as openfile:
        json_object = json.load(openfile)
    sessions = json_object['sessions']
    session = sessions[0]
    bestlaps = session["bestLaps"]
    bestlap = bestlaps[0]
    time = int(bestlap['time'])
    milliseconds = int(time%1000)
    seconds = int((time/1000)%60)
    minutes = int((time/(1000*60))%60)

    best_time = (f"{time},{minutes},{seconds}," + ("0"*(3-len(str(milliseconds)))) + f"{milliseconds}")

    track = json_object['track']
    
    openwindow(best_time, track)
    sort_and_clean_list()

    
    

#print_out(r"C:\Users\tordv\OneDrive - University of Bergen\Other\sim racing\changeables\testfile.json")



# Program to make a simple
# login screen 

 
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
        print("The name is : " + name)
        print("The last name is : " + lastname)

        name_var.set("")
        lastname_var.set("")


        fr = open(r"C:\Users\tordv\OneDrive - University of Bergen\Other\sim racing\changeables\leaderboard.csv", "r")
        fw = open(r"C:\Users\tordv\OneDrive - University of Bergen\Other\sim racing\changeables\leaderboard.csv", "a")
        fw.write(f"{track},{name},{lastname},{besttime}\n")
                


    def close():
        root.destroy()


    # creating a label for
    # name using widget Label
    name_label = tk.Label(root, text = 'Username', font=('calibre',50, 'bold'))
    
    # creating a entry for input
    # name using widget Entry
    name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',50,'normal'))
    
    # creating a label for last name
    passw_label = tk.Label(root, text = 'Last name', font = ('calibre',50,'bold'))
    
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


def sort_and_clean_list():
    
    fr = open(r"C:\Users\tordv\OneDrive - University of Bergen\Other\sim racing\changeables\leaderboard.csv", "r")
    
    lines = fr.readlines()
    lines.sort()
    finallines = []
    for x, line in enumerate(lines):
        line = line.split(',')
        if x == 0:
            finallines.append(",".join(line))
            continue
        lastline = lines[x-1]
        lastline = lastline.split(",")
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
    
    fw = open(r"C:\Users\tordv\OneDrive - University of Bergen\Other\sim racing\changeables\leaderboard.csv", "w")
    fw.writelines(finallines)
