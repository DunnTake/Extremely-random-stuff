from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QGridLayout, QTimeEdit
from PyQt5.QtCore import Qt, QTimer
import random
import subprocess
import os
import time
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("enter credentials")
        
        # Credentials GUI ---------------
        
        self.usr = QLabel()
        self.usr.setText("Username")
        self.uinput = QLineEdit()
        self.pword = QLabel()
        self.pword.setText("Password")
        self.pinput = QLineEdit()
        self.error = QLabel()
        self.error.setStyleSheet("color: red;")
        self.error.setText("Error: Password or username is incorrect")

        # Login Button -----------------

        self.button = QPushButton()
        self.button.setText("Sign in")
        self.button.setFixedSize(480,60)
        self.button.pressed.connect(self.signin)

        self.submit = QPushButton()
        self.submit.setText("Submit")
        self.submit.setFixedSize(480,60)
        self.submit.pressed.connect(self.sub)
        # Layout -----------------------

        self.grid = QVBoxLayout()
        self.grid.setAlignment(Qt.AlignCenter)
        self.grid.setSpacing(20)

        self.grid.addWidget(self.usr)
        self.grid.addWidget(self.uinput)
        self.grid.addWidget(self.pword)
        self.grid.addWidget(self.pinput)
        self.grid.addWidget(self.button)

        # App -------------------------

        container = QWidget()
        container.setLayout(self.grid)
        self.setCentralWidget(container)
        self.setFixedSize(500,300)
        self.path = 0
        self.p1diag = 0
        self.end = 0
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # Misc ------------------------
        
        # p1diag2 random input
        self.rando = ["Are friends and family","Are games","Is work","Is school","Is sleeping (or lack thereof)","Is the future"]
        self.pick = random.choice(self.rando)
        self.mood = None
        self.p1no = 0
        # DEV TOOLS, USE FOR BUGTESTING
        #self.path = 1

        # -----------------------------



    def signin(self):
        index = self.grid.indexOf(self.error)
        user = self.uinput
        pword = self.pinput
        error = self.error

        if self.path == 0:
            if user.text() == "" or pword.text() == "":
                error.setText("Error: Username or Password boxes cannot be left empty")
            else:
                error.setText("Error: Password or username is incorrect")


        # Path 1: Incorrect, S-81 kicks out of app

        if user.text() == "incorrect" or pword.text() == "incorrect":
            error.setText("Error: Incorrect username or password, try again")
        if user.text() in ["again", "try again"] or pword.text() in ["again", "try again"]:
            error.setText("Error: Stop trying to be funny, just type something else")
            self.path = 1
        if self.path == 1:
            if user.text() == "no" or pword.text() == "no" or user.text() in ["something", "some", "thing", "something else", "else"] or pword.text() in ["something", "some", "thing", "something else", "else"]:
                self.end = 1
                user.setDisabled(True)
                pword.setDisabled(True)
                self.button.setDisabled(True)
                error.setText("GET")
                QTimer.singleShot(2000, lambda: (
                    error.setStyleSheet("font-size: 30px; color: red;"),
                    error.setText("OUT"),
                    QTimer.singleShot(2000, lambda: (
                        window.hide(),
                        QApplication.quit(),
                    ))))
        if index == -1:
            self.grid.addWidget(self.error)
        
        # Path 1: User comes back

    def p1dialogue(self):
        # Dialogue
        error = self.error
        pword = self.pinput
        user = self.uinput
        error.setStyleSheet("font-size: 12px; color: red;")
        error.setText("..")
        QTimer.singleShot(3000, lambda: (
            error.setText("Oh."),
            QTimer.singleShot(2500, lambda: (
                error.setText("You came back."),
                QTimer.singleShot(3000, lambda: (
                    error.setText("I've had some little time to think"),
                    QTimer.singleShot(3500, lambda: (
                        error.setText("And I realized maybe I was a little too harsh on you"),
                        QTimer.singleShot(4500, lambda: (
                            error.setText("Or maybe you have some unresoved childhood trauma?"),
                            QTimer.singleShot(4500, lambda: (
                                error.setText("That could be true, hmm.."),
                                QTimer.singleShot(2000, lambda: (
                                    error.setText(".."),
                                    QTimer.singleShot(1500, lambda: ( 
                                        error.setText("...."),
                                        QTimer.singleShot(1500, lambda: (
                                            error.setText("So.."),
                                            QTimer.singleShot(1500, lambda: (
                                                error.setText("How about this.."),
                                                QTimer.singleShot(1500, lambda: (
                                                    error.setText("I'll ask you simple questions about your problems"),
                                                    QTimer.singleShot(4500, lambda: (
                                                        error.setText("And you answer yes/no in the username box"),
                                                        QTimer.singleShot(3500, lambda: (
                                                            error.setText("Got it? I'll go first"),
                                                            QTimer.singleShot(2000, lambda: (
                                                                error.setText("Has your day been fine?"),
                                                                user.setDisabled(False),
                                                                self.pword.setDisabled(True),
                                                                self.button.setDisabled(False),
                                                                self.grid.removeWidget(self.button),
                                                                self.grid.removeWidget(self.error),
                                                                self.error.hide(),
                                                                self.button.hide(),
                                                                self.grid.addWidget(self.submit),
                                                                self.grid.addWidget(self.error),
                                                                self.error.show()
                                                            ))))))))))))))
                                            ))))))))))))))
        self.path = 1.5
        self.p1diag = 1
                        

        #Path 1: yes/no, therapy session

    
    def sub(self):
        delay = int() # Delay singleshot expressions
        ans = self.uinput.text().strip().lower()
        insert = str() # Answer-specific insertion
        error = self.error

        if ans.startswith("y") == False and ans.startswith("n") == False:
            txt = error.text()
            error.setText("Only yes or no please..")
            self.submit.setDisabled(True)
            QTimer.singleShot(2000, lambda: (
                error.setText(txt),
                self.submit.setDisabled(False),
            ))
            return

        if self.p1diag == 1:
            self.submit.setDisabled(True)
            if ans.startswith("y"):
                error.setText("Well that is good to hear!")
                delay = 2500
                insert = "so happy"
                self.mood = "happy"

            else:
                error.setText("I'm sorry to hear that..")
                QTimer.singleShot(2000, lambda: (
                    error.setText("I hope things will go well for you soon")
                ))
                delay = 5000
                insert = "down"
                self.mood = "sad"

            QTimer.singleShot(delay, lambda: (
                    error.setText("Hmm.."),
                    QTimer.singleShot(1500, lambda: (
                        error.setText(str(self.pick + " making you feeling " + insert + "?")),
                        self.submit.setDisabled(False)
                    ))
                ))
            
            self.p1diag = 2
            return

        if self.p1diag == 2:
            mood = self.mood
            self.submit.setDisabled(True)
            if ans.startswith("n"):
                error.setText(random.choice(["Oh okay", "Alright", "Oh", "I see", "Ah okay"]))
                if self.p1no != 3:
                    QTimer.singleShot(1500, lambda: (
                        error.setText("Then..")
                        ))
                    delay = 2500
                elif self.p1no == 2:
                    delay = 1500
                self.p1no += 1

            elif ans.startswith("y"):
                if self.pick == "Are friends and family":
                    if mood == "sad":
                        error.setText("Oof, that's complicated")
                        QTimer.singleShot(2500, lambda: (
                            error.setText("There isn't much to do other than to hang tight in there")
                            ))
                        delay = 8500
                    elif mood == "happy":
                        error.setText("That's great, having a support system is really important.")
                        QTimer.singleShot(4000, lambda: (
                           error.setText("Appreciate the moment, a lot of people would be suffering where you are right now") 
                            ))
                        delay = 11500

                elif self.pick == "Is school":
                    if mood == "sad":
                        error.setText("I think people usually forget to take breaks")
                        QTimer.singleShot(3000, lambda: (
                            error.setText("No matter how bad things are, the worst thing you can let go of is yourself")
                            ))
                        delay = 10000
                    elif mood == "happy":
                        error.setText("Must feel great to do well in school.")
                        QTimer.singleShot(4000, lambda: (
                            error.setText("If I were you I would try to bring other people up to my level")
                            ))
                        delay = 11000

                elif self.pick == "Are games":
                    if mood == "sad":
                        error.setText("Why not a different activity?")
                        QTimer.singleShot(2500, lambda: (
                            error.setText("After all, isn't it bad to have too much of it?")
                                ))
                        delay = 5500
                    elif mood == "happy":
                        error.setText("So you like games, huh?")
                        QTimer.singleShot(2500, lambda: (
                            error.setText("Try to have frequent breaks so y'know, you don't get rusty")
                                ))
                        delay = 6500
                
                elif self.pick == "Is work":
                    if mood == "sad":
                        error.setText("I can say all about taking breaks and being happy and stuff")
                        QTimer.singleShot(5000, lambda: (
                            error.setText("But i think having good time management is also good if not  more important")
                            ))
                        delay = 12000
                    if mood == "happy":
                        error.setText("That's great.")
                        QTimer.singleShot(2000, lambda: (
                            error.setText("Not all share the same sentiment as you, cherish that")
                            ))
                        delay = 9000
                
                elif self.pick == "Is sleeping (or lack thereof)":
                    if mood == "sad":
                        error.setText("Just sleep, I know it's easier said than done")
                        QTimer.singleShot(4000, lambda: (
                            error.setText("but you'll always find time to rest up everyday, don't toss it away")
                            )) 
                        delay = 10500
                    if mood == "happy":
                        error.setText("That sounds nice.")
                        QTimer.singleShot(2000, lambda: (
                            error.setText("Keep it up, and you'll keep feeling fresh")
                            ))
                        delay = 8000
                
                elif self.pick == "Is the future":
                    if mood == "sad":
                        error.setText("I get it, it sucks how uncertain we are about it")
                        QTimer.singleShot(4000, lambda: (
                            error.setText("That's why we gotta cherish the now, when it's still in our sight")
                            )) 
                        delay = 10000
                    if mood == "happy":
                        error.setText("How confident.")
                        QTimer.singleShot(2000, lambda: (
                            error.setText("Don't forget about the present also, you won't regret it when it becomes a memory")
                            ))
                        delay = 9000
                
            if len(self.rando) > 3:
                self.rando.remove(self.pick)
                self.pick = random.choice(self.rando)
                if mood == "happy":
                    insert = "so happy"
                else:
                    insert = "down"
                
                QTimer.singleShot(delay, lambda: (
                    error.setText(str(self.pick + " making you feeling " + insert + "?")),
                    self.submit.setDisabled(False)
                    ))
                return
            else:
                if self.p1no != 4:
                    QTimer.singleShot(delay,lambda:(
                        error.setText("Y'know"),
                        QTimer.singleShot(2000,lambda:(
                            error.setText("What I said can apply to a lot of things"),
                            QTimer.singleShot(3500,lambda:(
                                error.setText("At the end of the day, keeping yourself safe is the most imporant thing"),
                                QTimer.singleShot(6000,lambda:(
                                    error.setText("That's what my creator used to say anyway..."),
                        ))))))))
                    delay = delay + 16000
                elif self.p1no == 4:
                    QTimer.singleShot(delay,lambda:(
                        error.setText("Well that wasn't really productive at all"),
                        QTimer.singleShot(3000,lambda:(
                            error.setText("I would really love to know more about you, but..")
                    ))))
                    delay = delay + 7000

                QTimer.singleShot(delay,lambda:(
                    error.setText("....."),
                        QTimer.singleShot(1500,lambda:(
                            error.setText("I think it's about time we wrapped up this talk"),
                            QTimer.singleShot(4000,lambda:(
                                error.setText("I hope it solved your childhood issues or something. Oh well,"),
                                QTimer.singleShot(5000,lambda:(
                                    error.setText("I'll be here in the database processing stuff, be seeing you later."),
                                    QTimer.singleShot(5500,lambda:(
                                        window.hide(),
                                        QApplication.quit()
                ))))))))))
                self.end = 1
                return

def clear():
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

def eraseline():
    sys.stdout.write("\033[F") 
    sys.stdout.write("\033[K") 
    sys.stdout.flush()

def preamble():
    clear()
    time.sleep(1)
    input("You received a message. Press Enter to open :: ")
    print("")
    print("Showing mail--")
    time.sleep(1.5)
    print("""
------------------------
From: Muhammed Singal (PERSONNEL ID: 040752)    dated: 14/7/1984 at 16:08:45
To: Marcus Caspian (PERSONNEL ID: 052974)
Subject: IMPORTANT, S-81 CONTAINMENT BREACH

Hey,

Specimen 81 has breached containment. It went inanimate in the containment floppy disk during routine checkups. The new guy thought the entity had already breached (it wasn't at the time), and tried to access the disk, and S-81 took the chance to break out for real. (Safe to say, this guy needs to be fired)

You're our server guy, so I need you to sweep the servers and find something, any lead about S-81 whereabouts. Meanwhile, I'll try to track down Damien Harrison, the former lead researcher on S-81, to see if he has any insight on the entity.
          
Act fast, the more time we waste, the faster it is for the entity to break out into the world wide web. At that point, theres no telling what it would do.

That is all. Best regards,
Singal 
          
-------------------------
          """)
    input("Press Enter to proceed :: ")



def midp1(): # This will be path 1, when booting back on, path 1 therapy session starts
    pass # Throws back into Brune Co. terminal, where the player finds a way to boot up and contact the database, leading to path 2
    clear()
    print("""#------- Brune Co. --------
|
| Device administrator: Marcus Caspian
| Version: 12.0185.21     
|
          
""")
    time.sleep(1.5)
    input("""------- DATABASE EXECUTABLE -------
          
FATAL ERROR: APPLICATION CLOSED UNEXPECTEDLY, CRASH LOG AUTOMATICALLY SENT TO MAINTENANCE
PRESS ENTER TO RESTART APPLICATION :: """)
    
    print("""ERROR: COULD NOT RESTART APPLICATION, RUNNING DIAGNOSTICS-""")
    time.sleep(1)
    eraseline()
    for i in range(2,4):
        eraseline()
        print("ERROR: COULD NOT RESTART APPLICATION, RUNNING DIAGNOSTICS" + "-" * i)
        time.sleep(1)
    print("""
DIAGNOSTICS COMPLETE, ISSUE FOUND: MISSING SYSTEM FILES,""")
    time.sleep(1.5)
    print("REINSTALLING MISSING FILES-")
    time.sleep(1)
    for i in range(2,4):
        eraseline()
        print("REINSTALLING MISSING FILES" + "-" * i)
        time.sleep(1)
    print("NOTICE: REINSTALLATION CAN TAKE SEVERAL MINUTES, PLEASE WAIT (ETA: UNKNOWN)")
    time.sleep(0.5)
    print("")
    input("ENTER TO RETURN TO MAIN TERMINAL :: ")
    #The same intro terminal but S-81_REPORT.txt is partially uncorrupted, then the reinstallation completes
    clear()
    time.sleep(1.5)
    accessed = False
    print("""#------- Brune Co. --------
|
| Device administrator: Marcus Caspian
| Version: 12.0185.21
|

""")
    time.sleep(1.5)
    print("Last time since last login: 15-07-1984 2:34:17")
    print("")
    while True:
        skip = False
        cd = str()
        if accessed == False:
            print("""Available files ------------
|
| 1. INTRODUCTION_PLEASE_READ.txt
| 2. to_do.txt
| 3. S-81_REPORT.txt    \033[93m -- FILE RECOVERY COMPLETE -- \033[0m
| 4. Database.exe
|            
---------------------------                  
            """)
        else:
            print("""Available files ------------
|
| 1. INTRODUCTION_PLEASE_READ.txt
| 2. to_do.txt
| 3. S-81_REPORT.txt
| 4. Database.exe
|            
---------------------------                  
                  """)
        while True:
            cd = input("Enter 'cd [number]' to access files :: ")
            if cd in ["cd 1", "cd 2", "cd 3", "cd 4"]:
                break
        if cd == "cd 1":
            print("Opening INTRODUCTION_PLEASE_READ.txt--")
            time.sleep(1.5)
            clear()
            print("INTRODUCTION, PLEASE READ")
            print("")
            print("""FROM THE CREATOR

Hello,

\033[32mABOUT THE GAMEPLAY\033[0m
This is a "game" I made while learning PyQt5. The idea first came when I was making a log in screen, which eventually kind of devolved into this. There isn't really a gameplay here, it's more of a story-based interactive experience therefore \033[93mit requires a LOT of reading\033[0m, so I suggest you play it preferrably \033[93mwith patience and no distractions.\033[0m

\033[93mBear with me here, this is important for your sanity:\033[0m The first few hours when i was making the login screen and conceptualizing the game, I didn't really took the audience's perception into account. This and the lack of second thoughts made the first segment of this part is extremely unintuitive and frustrating to get through the first time. So \033[93mif you are at the first login screen before the initial kickout, if the program tells you that your "password or username is incorrect", then just type "incorrect" in one of the boxes\033[0m, do the same thing for the rest of the responses, and you will get kicked out, which would be the end of it

There is a lot to be fixed and improved. But after finishing the first part, I had no idea what to do for part 2 and felt like the program was already a mess and was dragging on. I do want to keep this world idea in the back of my head until I accumulate enough skill and motivation to proceed with this idea. But for now, the second part is not going to be in progress for anytime soon

\033[32mABOUT THE STORY\033[0m
\033[93mIf you are curious about the story and don't want any spoilers, I suggest you skip this part and just play through the game and come back (or don't) to this. It is the focal point of this interactive experience after all\033[0m
                  
I wanted to go for a kind of "creepypasta" vibe with a bit of fiction. Specfically, it is a universe where the SCP foundation exists under the name "Brune Co.", confining and researching anomalous activities specifically in Chernobyl, which is the birthplace for all of the entities after the nuclear incident. You play as Marcus Caspian, a server administrator for Brune Co., who gets involved in recontaining S-81, a sentient computer virus like program that breached containment and moved itself into the servers.
                  
A colleague of yours, Muhammed Singal, went to track down the former lead researcher on S-81, Damien Harrison, to get his insight on the entity. During the course of the game you and Singal would be exchanging mails, updating each other on the situation.
                  
Of course, that is what I have merely planned and have only executed the part where you respond back to Singal so far. For part 2, I planned to have the player comb through the entity-infected database, trying to find information on the entity and containing it themself. Though the idea started the snowballed into burnt outs and reluctant works

\033[32mABOUT YOU\033[0m
If you're reading this, you're one of the few friends who I've shown this to, so of course thank you for taking the time to read through this wall of text and play this game, and I apologize in-advance for the cringe in-game events and missed opportunities. Trust me when I say that I am well aware of the gameplay and vibe issues, sadly those aren't going to be fixed anytime soon, I've already spent the last remaining speck of my motivation writing this, and I'm very ready to move on to other projects.

Still, I would love to hear your feedback on this, about what works and what doesn't, what you would have added in, removed or done differently. I have learnt a lot about programming and storytelling while making this, and I feel like I have a lot more to learn.
                  
Again, thank you for playing, and I hope you have fun with this silly program I made. Perhaps even in a hot mess we can still find perfection within the imperfections.
----------------------------
            """)

        elif cd == "cd 2":
            print("Opening TO-DO.txt--")
            time.sleep(1.5)
            clear()
            print("""-------- TO-DO LIST --------)
                
1. Contact maintenance, need to get the AC fixed
2. Ask Jared for his copy of the manual
3. Pet that cat I see on the way to work everyday
4. Review S-81_REPORT.txt, don't know how that got there, prolly sent by Singal
5. Access Database via the old worker's account

----------------------------""")
            print("")

        elif cd == "cd 3":
            accessed = True
            print("Opening S-81_REPORT.txt--")
            time.sleep(1.5)
            clear()
            print("------- S-81 REPORT ------- \033[93mSUCCESSFULLY RECOVERED MOST OF CONTENT, RESIDUAL CORRUPTION MAY REMAIN\033[0m")
            print("")
            print("""February 9, 1983. █his is log No.█, Dr Dam█en speaking.

Recently, there were sud░▒en gravitational activities in Anoma▒█ous Point 81, an area in Ch██nobyl with strange occur░▒ences, possibly brought about by the nucl█▒ar fallout that followed the city's evacua█▒ion. Now, sudden activities like these are just another Tuesday for us, so we contacted APAP (A█▒alous Point Assessment Program) for field assessment.

Squad 8, I think, was the team they sent for the task. They managed to quickly identi▒█fy the source of the disturbance; at the center of the storm-like chaos is an old comp█▒ter, floating and shaking mid-air. The team, impre▒█ssively, managed to find out that while the computer caused gravitational anomalies, the "program" (for lack of a better word) was what was activating it in the first place.

The computer itself wasn't really a topic of great concern; this gravitatio█▒al disturbance had happened more than once, all of which were caused by it. And we already knew of its existence, disa▒█bled it, and it remained inani░▒mate since then. However, it appears that a pro▒█gram (or perhaps a vi░▒rus) made its way into it and acti█▒ated the computer's anomalous functio█▒ality itself.

Squad 8 mana█▒ed to extract the program by uploading it to a hard drive and success▒█fully brought it back to Brune Containme▒█nt. At the time of speaking, I have been gi░▒ven the disk and am tasked with mana█▒ing, research▒█ing, and containing this entity, which we now call Specimen 81.

    --- END OF LOG ---
                  
    """)
            
        elif cd == "cd 4":
            skip = False
            if accessed == False:
                print("\033[32mThe S-81_REPORT.txt was recovered and is unread.\033[0m")
                k = input("\033[32mProceed? (y/n) :: \033[0m")
                if k == "y":
                    clear()
                else:
                    clear()
                    skip = True
            if skip == False:    
                print("Opening Database.exe--")
                time.sleep(1.5)
                clear()
                print("----- DATABASE EXECUTABLE -----")
                print("")
                print("Executing Database.exe...")
                time.sleep(2)
                break
        if skip == False:
            while True:
                input("Enter to return to file selection :: ")
                clear()
                break




app = QApplication(sys.argv)

window = MainWindow()

#PATH 1 END
def p1end():
    clear()
    print("\033[32mWriting mail\033[0m")
    for i in range(1,4):
        time.sleep(1.5)
        eraseline()
        print("\033[32mWriting mail" + "." * i + "\033[0m")
    print("")
    print("""------------MAIL PREVIEW------------
From: Marcus Caspian (PERSONNEL ID: 052974)     dated: 14/7/1984 at 21:37:13
To: Muhammed Singal (PERSONNEL ID: 040752)
Subject: RE: IMPORTANT, S-81 CONTAINMENT BREACH
          
S,

I've located S-81, it seems to have resided itself in the database, Damien's database to be exact. I have no idea how or why it got there, I have a few theories, but I can't confirm any of them until I gain access to the database.

The enity did make contact with me in the login terminal, but it was unlike ive seen. It talks almost like a normal human being, one that acts like an asshole, anyway (it tried to 'solve my childhood trauma' because i was annoying it). I'll talk more about it when we're done

Anyway, I need Damien's credentials to access the database and the floppy disk (or any functional copy) to upload and store S-81. I have a feeling something might happen when I successfully log in..

There are only those two problems. After that, you can keep finding Damien, he knows best in worst cases
   
Act fast,
Marcus
--------------------------------------
          """) # INCOMPLETE HERE 
    time.sleep(2)
    input("Press Enter to send mail :: ")
    print("Sending mail--")
    time.sleep(2)





def p2preamble():
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
    time.sleep(1)
    print("\033[32mTWO DAYS LATER\033[0m")
    time.sleep(2)
    print("")
    input("You received a message. Press Enter to open :: ")
    print("")
    print("Showing mail--")
    time.sleep(1.5)
    print("""
------------------------
From: Muhammed Singal (PERSONNEL ID: 040752)    dated: 16/7/1984 at 2:45:36
To: Marcus Caspian (PERSONNEL ID: 052974)
Subject: RE: RE: IMPORTANT, S-81 CONTAINMENT BREACH

No leads so far, this Damien guy is better at keeping himself hidden than i thought. It's almost as if after he got transferred to a different sector, he deliberately tried to scrub clean every trail.

But he did leave behind his credentials, exactly as you need it. You should thank Hobb, our cybersecurity guy for it. Here it is:

Username: DamienHarrison89
Password: DH58145

Hobb will be giving you a new copy of the disk you asked for when you arrive. Once you are certain you've arrived at its core, you know what to do. If you forgot (which i hope to hell you didn't), insert the floppy disk and run this command in the terminal:
          "disk import program:database/CD/name:S-81 --allfiles"

\033[93mWrite it all down on a note if you need it\033[0m. We have to be extremely careful here, you know how much is riding on this. I'm sorry I cannot be there myself, but I've got a possible lead as to Damien's whereabouts.
          
Good luck,
Singal
-----------------------
""")
    time.sleep(1.5)
    input("")
    print("Press Enter to proceed :: ")
    clear()
    time.sleep(1.5)
    print("\033[32mPart 2\033[0m")
    time.sleep(1.5)
    print("\033[32mIs not out yet :P\033[0m")
    while True:
        pass
'''    print("""#------- Brune Co. --------)
|
| Device administrator: Marcus Caspian
| Version: 12.0185.21
|

        """)
'''


#REMOVE ''' BEFORE PUSHING EXE
#INRODUCTION

cds = []
def p1start():
    clear()
    time.sleep(1)
    print("\033[32mPart 1\033[0m")
    time.sleep(1.5)
    print("""#------- Brune Co. --------
    |
    | Device administrator: Marcus Caspian
    | Version: 12.0185.21
    |

    """)
    time.sleep(1.5)
    print("Last time since last login: 13-07-1984 8:18:35")
    print("")
    while True:
        skip = False
        cd = str()
        print("""Available files ------------
    |
    | 1. INTRODUCTION_PLEASE_READ.txt
    | 2. to_do.txt
    | 3. S-81_REPORT.txt
    | 4. Database.exe
    |            
    ---------------------------                  
            """)
        while True:
            cd = input("Enter 'cd [number]' to access files :: ")
            if cd in ["cd 1", "cd 2", "cd 3", "cd 4"]:
                break
        if cd == "cd 1":
            cds.append("1")
            print("Opening INTRODUCTION_PLEASE_READ.txt--")
            time.sleep(1.5)
            clear()
            print("INTRODUCTION, PLEASE READ")
            print("")
            print("""------- INTRODUCTION -------
FROM THE CREATOR

Hello,

\033[32mABOUT THE GAMEPLAY\033[0m
This is a "game" I made while learning PyQt5. The idea first came when I was making a log in screen, which eventually kind of devolved into this. There isn't really a gameplay here, it's more of a story-based interactive experience therefore \033[93mit requires a LOT of reading\033[0m, so I suggest you play it preferrably \033[93mwith patience and no distractions.\033[0m

\033[93mBear with me here, this is important for your sanity:\033[0m The first few hours when i was making the login screen and conceptualizing the game, I didn't really took the audience's perception into account. This and the lack of second thoughts made the first segment of this part is extremely unintuitive and frustrating to get through the first time. So \033[93mif you are at the first login screen before the initial kickout, if the program tells you that your "password or username is incorrect", then just type "incorrect" in one of the boxes\033[0m, do the same thing for the rest of the responses, and you will get kicked out, which would be the end of it

There is a lot to be fixed and improved. But after finishing the first part, I had no idea what to do for part 2 and felt like the program was already a mess and was dragging on. I do want to keep this world idea in the back of my head until I accumulate enough skill and motivation to proceed with this idea. But for now, the second part is not going to be in progress for anytime soon

\033[32mABOUT THE STORY\033[0m
\033[93mIf you are curious about the story and don't want any spoilers, I suggest you skip this part and just play through the game and come back (or don't) to this. It is the focal point of this interactive experience after all\033[0m
                  
I wanted to go for a kind of "creepypasta" vibe with a bit of fiction. Specfically, it is a universe where the SCP foundation exists under the name "Brune Co.", confining and researching anomalous activities specifically in Chernobyl, which is the birthplace for all of the entities after the nuclear incident. You play as Marcus Caspian, a server administrator for Brune Co., who gets involved in recontaining S-81, a sentient computer virus like program that breached containment and moved itself into the servers.
                  
A colleague of yours, Muhammed Singal, went to track down the former lead researcher on S-81, Damien Harrison, to get his insight on the entity. During the course of the game you and Singal would be exchanging mails, updating each other on the situation.
                  
Of course, that is what I have merely planned and have only executed the part where you respond back to Singal so far. For part 2, I planned to have the player comb through the entity-infected database, trying to find information on the entity and containing it themself. Though the idea started the snowballed into burnt outs and reluctant works

\033[32mABOUT YOU\033[0m
If you're reading this, you're one of the few friends who I've shown this to, so of course thank you for taking the time to read through this wall of text and play this game, and I apologize in-advance for the cringe in-game events and missed opportunities. Trust me when I say that I am well aware of the gameplay and vibe issues, sadly those aren't going to be fixed anytime soon, I've already spent the last remaining speck of my motivation writing this, and I'm very ready to move on to other projects.

Still, I would love to hear your feedback on this, about what works and what doesn't, what you would have added in, removed or done differently. I have learnt a lot about programming and storytelling while making this, and I feel like I have a lot more to learn.
                  
Again, thank you for playing, and I hope you have fun with this silly program I made. Perhaps even in a hot mess we can still find perfection within the imperfections.
----------------------------
            """)

        elif cd == "cd 2":
            cds.append("2")
            print("Opening TO-DO.txt--")
            time.sleep(1.5)
            clear()
            print("""-------- TO-DO LIST --------)
                
    1. Contact maintenance, need to get the AC fixed
    2. Ask Jared for his copy of the manual
    3. Pet that cat I see on the way to work everyday
    4. Review S-81_REPORT.txt, don't know how that got there, prolly sent by Singal
    5. Access Database via the old worker's account

    ----------------------------""")
            print("")

        elif cd == "cd 3":
            cds.append("3")
            print("Opening S-81_REPORT.txt--")
            time.sleep(1.5)
            clear()
            print("------- S-81 REPORT -------")
            print("")
            print("""Febru░░▒▒████████ 9, 19█3. ██░▒▒▒ is l░g █o.█, Dr ██▒▒▒▒ sp░▒██.

    Re░░▒▒██████████████ there w░▒▒▒ sud░▒ gravi░░▒▒████████████████████ activi░▒▒▒ in Anoma▒██████ Point 8█, an area in Ch▒██████ with strange occ░▒██████, possibly brough█▒▒▒▒▒▒▒ut by the n░cl░░▒▒████████ fallout that f░▒██████ the city's evac░▒██████. N░▒▒▒▒▒ sud░▒ activi░▒▒▒ like th░░░ ██▒▒▒▒ just ano░▒██████ Tues░░▒▒▒▒ for ▒█▒▒▒▒, so we con░▒██████ APAP (A▒██████ Point Assess░▒██████ Prog░▒██) for fi░▒██████ assess░▒██████.

    Sq░▒██████ 8, I th░▒▒▒▒, was th░ ███▒▒▒▒ they s░▒▒▒▒ for th░ task. Th░▒▒▒▒ managed to qu░░▒▒████████ id░▒████████ the sour░▒▒▒▒ of the di░▒██████, at the cen░▒▒▒▒ of the st░▒██████ chaos is an old comp░▒██████, flo░▒██████ and sha░▒██████ mid-air. Th░ team, impr░▒██████, man░▒██████ to find out th░▒▒▒▒ while the comp░▒██████ caused gravi░▒██████ anomalies, the "p░░▒▒████████████████████████████████████████" was wh░▒▒▒▒ w░▒▒▒▒ act░▒██████ it in the fi░▒██████ place.

    Th░ comp░▒██████ itself w░▒'t rea░▒██████ a topic of g░▒██████ concern; th░░▒▒████████████████████████████████████████████████████████ disturbance had happ░▒██████ more th░▒▒▒▒ once, all of which were caus░▒▒▒▒ by it. And we al░▒██████ knew of █ts exis░▒██████, disa░▒██████ it, and it remai░▒██████ inani░▒██████ since th░▒▒▒▒. How░▒▒▒▒, it appears th░▒▒▒▒ a ░▒████████████████████████ (or per░▒██████ a ░▒████████████████████████) made █ts way into █t and act░▒██████ the comp░▒██████'s anom░▒██████ funct░░▒▒████████████████████████████████ itself.

    S░▒██████ 8 man░▒██████ to extr░░▒▒████████████████████████████ by upl░▒██████ it to a ha░▒██████ drive and succ░▒██████████ brought it b░▒██████ to Bru░▒██████ Cont░▒██████. At th░▒▒▒▒ time of spe░▒██████, █ h░▒▒▒▒ been gi░▒██████ th░▒ d░▒▒▒▒ and am ta░▒██████ with man░▒██████, rese░▒██████ and cont░▒██████ th░▒ ░▒████████████████████████, wh░▒▒▒▒ we now c░▒██████ Spec░▒██████ 81.

    ----------------------------
    """)
            time.sleep(2)
            print("\033[93m[ERR: DATA CORRUPTED, RECOVERY IN PROGRESS, ETA: UNKNOWN]\033[0m")
            print("")
            time.sleep(1.5)
        elif cd == "cd 4":
            skip = False
            if cds.count("1") == 0 or cds.count("2") == 0 or cds.count("3") == 0:
                print("\033[32mRunning this executable will proceed, make sure you have read all the files first.\033[0m")
                k = input("\033[32mProceed? (y/n) :: \033[0m")
                if k == "y":
                    clear()
                else:
                    clear()
                    skip = True
            if skip == False:    
                print("Opening Database.exe--")
                time.sleep(1.5)
                clear()
                print("----- DATABASE EXECUTABLE -----")
                print("")
                print("Executing Database.exe...")
                time.sleep(2)
                input("Warning: Unauthorized access detected, please enter PIN to continue :: ")
                print("")
                print("PIN incorrect, intruder detected")
                time.sleep(1.5)
                print("")
                print("Removing User Access--")
                time.sleep(1)
                sys.stdout.write("\033[F") 
                sys.stdout.write("\033[K") 
                sys.stdout.flush()
                print("\033[31m\033[9mRemoving User Access--\u0336\033[0m")
                time.sleep(0.7)
                sys.stdout.write("\033[F") 
                sys.stdout.write("\033[K") 
                print("Access Granted")
                break
        if skip == False:
            while True:
                k = input("Enter to return to file selection :: ")
                clear()
                break

    print("")
    time.sleep(1.5)
    print("Accessing system--")
    time.sleep(2)
    print("")
    print("NOTICE: DATABASE ACCOUNT NOT FOUND, PLEASE SIGN IN TO CONTINUE")
    time.sleep(2)
    print("")
    print("WARNING: CORRUPTION OF UNKNOWN PRECEDENT DETECTED IN THE EXECUTABLE, PROCEED WITH CAUTION")
    time.sleep(3)
    print("")
    print("Launching Sign-in Interface--")
    time.sleep(1.5)

    window.show()
    app.exec_()



preamble()
p1start()
midp1()
window.show()
window.p1dialogue()
app.exec_()
p1end()
p2preamble()