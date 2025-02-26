# imports modules
import pygame, random, sqlite3

# Game Initialization
pygame.init()

# Resolution
screen = pygame.display.set_mode((1000, 750))

# Default colours
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
mainMenuBackGroundColour = (239,228,176)
blue = (0, 0, 255)
yellow = (255, 255, 0)
pink = (255, 0, 127)

# Game Framerate
clock = pygame.time.Clock()
FPS = 30

# Declare variables which will become global
boxColour = red
boxesRevealed = 0
level = 1
lineColour = black
revealCalled = 1

#Initialises fonts
gameTitleFonts = pygame.font.SysFont('arial', 90)
smallFont = pygame.font.SysFont('arial', 40)
regularFont = pygame.font.SysFont('arial', 60)

# Main Menu
def settings():
    global boxColour, lineColour
    # draws the background and text on the screen
    screen.blit(pygame.image.load("settingsmenu.png"),(0,0))
    screen.blit(smallFont.render("Box Colour (white, black, red, green, blue, yellow, pink)", 0, black),(5,25))
    screen.blit(smallFont.render("Line Colour (white, black, red, green, blue, yellow, pink)", 0, black),(5,175))
    pygame.display.update()
    # initialises variables and arrays used within the settings function
    line_text = ''
    box_text = ''
    colour_list = ['white', 'black', 'red', 'green', 'blue', 'yellow', 'pink']
    colourNumber_list = [(255, 255, 255),(0, 0, 0),(255, 0, 0),(0, 255, 0),(0, 0, 255),(255, 255, 0),(255, 0, 127)]
    box_clicked = True
    line_clicked = False
    settings = True
    validBoxColour = bool
    validLineColour = bool

    # Creates a fixed loop so the settings menu is constantly running, allows the screen to be updated with the users text and buttons to work
    while settings == True:
        mousex, mousey = pygame.mouse.get_pos()
        pygame.display.update()
        for event in pygame.event.get():
                # Creates a conditional statement for if the mouse is over the back button or not
                if (mousex > 5 and mousex < 125) and (mousey > 625 and mousey < 670):
                    screen.blit(smallFont.render("Back", 0, green),(40,615))
                else:
                    screen.blit(smallFont.render("Back", 0, black),(40,615))
                # Creates a conditional statement for if the mouse is over the submit button or not
                if (mousex > 759 and mousex < 930) and (mousey > 318 and mousey < 354):
                    screen.blit(smallFont.render("Submit", 0, green),(760,318))
                else:
                    screen.blit(smallFont.render("Submit", 0, black),(760,318))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Creates a conditiaonl statement to check if the mouse is on the box colour input box
                    if (mousex > 43 and mousex < 497) and (mousey > 109 and mousey < 161):
                        box_clicked = True
                        line_clicked = False
                    # Creates a conditional statement to check if the mouse is on the line colour input box
                    elif (mousex > 43 and mousex < 497) and (mousey > 276 and mousey < 335):
                        box_clicked = False
                        line_clicked = True
                    # Checks to see if the box colour and line colour inputted is equal to a valid colour that the game supports
                    elif (mousex > 759 and mousex < 930) and (mousey > 318 and mousey < 354):
                        for i in range(len(colour_list)):
                            if box_text.lower() == colour_list[i]:
                                boxColour = colourNumber_list[i]
                                validBoxColour = True
                            if line_text.lower() == colour_list[i]:
                                lineColour = colourNumber_list[i]
                                validLineColour = True
                        # If both of the inputted values are equal to valid colours then returns to the main menu
                        if validBoxColour == True and validLineColour == True:
                            main_menu()
                        # If line colour or box colour aren't equal then displays an error message on the screen.
                        if validLineColour != True:
                            screen.blit(smallFont.render("Invalid Colour Entered for Line Colour", True, black), (450, 420))
                        if validBoxColour != True:
                            screen.blit(smallFont.render("Invalid Colour Entered for Box Colour", True, black), (450, 380))
                        # Stops players from entering one valid value then deleting that value then entering another value in the other box and the game taking it as a valid input
                        if validBoxColour == True or validLineColour == True:
                            validBoxColour = False
                            validLineColour = False
                    # if the users click on the mouse button then it returns to the main menu
                    if (mousex > 5 and mousex < 125) and (mousey > 626 and mousey < 670):
                        main_menu()
                    # Limits the users input to a certain number of characters
                if event.type == pygame.KEYDOWN:
                    if len(line_text) >= 6:
                        line_text = line_text[:6]
                    if len(box_text) >= 6:
                        box_text = box_text[:6]
                    # Checks if the box colour box is clicked and the user has clicked backpaace then removes one character from the box colour. If the user isn't pressing backspace or return then adds that character to the box text
                    if box_clicked == True:
                        if event.key == pygame.K_BACKSPACE:
                            box_text = box_text[:-1]
                        elif event.key != pygame.K_BACKSPACE and event.key != pygame.K_RETURN:
                            box_text += event.unicode
                    # Checks if the line box is clicked and the user has clicked backpaace then removes one character from the line colour. If the user isn't pressing backspace or return then adds that character to the box text
                    elif line_clicked == True:
                        if event.key == pygame.K_BACKSPACE:
                                line_text = line_text[:-1]
                        elif event.key != pygame.K_BACKSPACE and event.key != pygame.K_RETURN:
                            line_text += event.unicode

                    # Redraws the images and text so the screen can display correctly without text being drawn over
                    screen.blit(pygame.image.load("settingsmenu.png"),(0,0))
                    screen.blit(smallFont.render("Box Colour (white, black, red, green, blue, yellow, pink)", 0, black),(5,25))
                    screen.blit(smallFont.render("Line Colour (white, black, red, green, blue, yellow, pink)", 0, black),(5,175))
                    screen.blit(smallFont.render("Submit", 0, black),(760,318))
                    screen.blit(smallFont.render("Back", 0, black),(40,615))
                    screen.blit(smallFont.render(line_text, True, black), (45, 276))
                    screen.blit(smallFont.render(box_text, True, black), (45,109))

def instructions():
    # Sets variables to false and draws images and text on the screen
    menu = False
    instructions = True
    screen.blit(pygame.image.load("instructionsBackground.png"),(0,0))
    screen.blit(gameTitleFonts.render("Instructions", 0, blue),(250,80))
    screen.blit(smallFont.render("Once the game starts all squares will be revealed",0, blue), (20, 200))
    screen.blit(smallFont.render("It is up to you to memorise what each of these squares are.",0, blue), (20, 250))
    screen.blit(smallFont.render("These squares will become covered and you need to",0, blue), (20, 300))
    screen.blit(smallFont.render("click on the boxes which don't contain bombs.",0, blue), (20, 350))
    screen.blit(smallFont.render("Clicking on powerups will take 1 off your overall time.",0, blue), (20, 400))

    # Creates a while loop so that the button will work when the user clicks it.
    while instructions == True:
        mousex, mousey = pygame.mouse.get_pos()
        pygame.display.update()
        for event in pygame.event.get():
                # If the user hovers over the back button the text changes from black to green and if the user clicks the button while it is green then the game calls the main menu function
                if (mousex > 31 and mousex < 165) and (mousey > 672 and mousey < 730):
                    screen.blit(smallFont.render("Back", 0, green),(65,675))
                else:
                    screen.blit(smallFont.render("Back", 0, black),(65,675))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (mousex > 31 and mousex < 165) and (mousey > 672 and mousey < 730):
                        main_menu()

def onHover(font1, text1, colour1, xaxis1, yaxis1, font2, text2,colour2,xaxis2,yaxis2,font3,text3,colour3,xaxis3,yaxis3):
    # Draws the parameters on the screen
    screen.blit(font1.render(text1,0,colour1), (xaxis1, yaxis1))
    screen.blit(font2.render(text2,0,colour2), (xaxis2, yaxis2))
    screen.blit(font3.render(text3,0,colour3), (xaxis3, yaxis3))

def main_menu():
    # Draws main menu elements on the screen.
    screen.blit(pygame.image.load("mainmenu.png"), (0, 0))
    screen.blit(pygame.image.load("instructionsIcon.png"), (80,-10))
    screen.blit(pygame.image.load("settings.png"), (10, 0))
    screen.blit(regularFont.render("Start", 0, black),(245,175))
    screen.blit(smallFont.render("Leaderboard", 0, black),(200,287))
    screen.blit(regularFont.render("Quit", 0, black),(245,384))
    screen.blit(gameTitleFonts.render("Memory Game", 0, yellow),(500,80))

    # Updates the display so the above items are drawn
    pygame.display.update()
    menu = True

    # Creates a while loop so that the buttons work
    while menu == True:
        pygame.display.update()
        for event in pygame.event.get():
            mousex, mousey = pygame.mouse.get_pos()
            # Calls the onHover function so that the text is drawn in the correct positions and colours when  hovered.
            if (mousex>190 and mousex<400) and (mousey>185 and mousey<235):
                onHover(regularFont, "Start", green, 245, 175, smallFont, "Leaderboard", black, 200, 287, regularFont, "Quit", black, 245, 384)
            elif (mousex>190 and mousex<400) and (mousey>290 and mousey<335):
                onHover(regularFont, "Start", black, 245, 175, smallFont, "Leaderboard", green, 200, 287, regularFont, "Quit", black, 245, 384)
            elif (mousex > 190 and mousex < 400) and (mousey>395 and mousey<445):
                onHover(regularFont, "Start", black, 245, 175, smallFont, "Leaderboard", black, 200, 287, regularFont, "Quit", green, 245, 384)
            # Creates a conditional statement so that if the user clicks one of the buttons on the screen
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (mousex>190 and mousex<400) and (mousey>185 and mousey<235):
                    main_game()
                elif (mousex>190 and mousex<400) and (mousey>290 and mousey<335):
                    leaderboard()
                elif (mousex> 10 and mousex < 73) and (mousey > 0 and mousey < 55):
                    settings()
                elif (mousex > 80 and mousex < 180) and (mousey > 0 and mousey < 80):
                    instructions()
                elif (mousex > 190 and mousex < 400) and (mousey>395 and mousey<445):
                        pygame.quit()
                        quit()

def databaseInsert(playerName, playerScore):
    # Creates a connection to the database
    connection = sqlite3.connect('playerData.db')
    cursor = connection.cursor()
    # Creates a table to store the data
    cursor.execute('''CREATE TABLE IF NOT EXISTS PlayerData (
                            playerName Varchar(30) NOT NULL,
                            playerScore INT NOT NULL);''')
    # Inserts the data into the table that was just created
    cursor.execute("INSERT INTO playerData(playerName, playerScore)VALUES(?,?)",(playerName, playerScore))
    # Commits these to the database.
    connection.commit()

def databaseGather():
    # Creates the array to store the player data
    playerData = []
    # Creates a connection
    connection = sqlite3.connect('playerData.db')
    cursor = connection.cursor()
    # Creates the database table
    cursor.execute('''CREATE TABLE IF NOT EXISTS PlayerData (
                            playerName Varchar(30) NOT NULL,
                            playerScore INT NOT NULL);''')
    # Selects the data from the table
    cursor.execute("SELECT * FROM playerData")
    # Commits these to the database.
    connection.commit()

    # Fetches all the data
    playerSet = cursor.fetchall()
    # Creates a fixed loop to store the data from the database into variables
    for line in playerSet:
        nameCopy = False
        playerName = line[0]
        playerScore = line[1]

        # Compares the username to a previous username and if the username is equal to an old username and the score is higher then it uses the new score instead of the old score
        for i in range(len(playerData)):
            if playerName == playerData[i][0]:
                position = i
                if playerScore > int(playerData[position][1]):
                    # Replaces old score
                    playerData[position][1] = playerScore
                nameCopy = True
        if nameCopy == False:
            # Adds the data from the database into a 2d array
            playerData.append([playerName,playerScore])
    # Closes connection
    cursor.close()
    return playerData

def leaderboard():
    # Draws the background and creates a connection
    screen.blit(pygame.image.load("leaderboardBackground.png"), (0, 0))
    connection = sqlite3.connect('playerData.db')
    cursor = connection.cursor()
    # Leaderboard UI
    pygame.display.flip()
    Leaderboard = True
    # Puts the data from the databaseGather function into a 2d array in the leaderboard function
    playerData = databaseGather()

    # Creates a fixed loop to hold the insertion sort.
    for index in range (len(playerData)):
        # Storess the value to be inserted into the array
        currentvalue = playerData[index]
        position = index
        # Compares the scores and swaps where necessary.
        while position > 0 and int(playerData[position-1][1] < int(currentvalue[1])):
            playerData[position] = playerData[position-1]
            position -= 1
        # Inserts the value into the array
        playerData[position] = currentvalue
    # Limits the number of results shown on the leaderboard
    if len(playerData) < 7: # Stops the game from crashing if there is no data actually in the 2d array
        loopNumber = len(playerData)
    elif len(playerData) >= 7:
        loopNumber = 6
    for i in range(loopNumber):
        # Draws the data from the database on the screen.
        screen.blit(smallFont.render(str(i + 1), 0, black), (345, (i * 35) + 260))
        screen.blit(smallFont.render(playerData[i][0], 0, black), (375, (i * 35) + 260))
        screen.blit(smallFont.render(str(playerData[i][1]), 0, black), (540, (i * 35) + 260))

    # Draws helpful information on thes screen informing the player what each column on the leaderboard.
    screen.blit(smallFont.render("Name", 0, black),(375,215))
    screen.blit(smallFont.render("Score",0, black),(540,215))

    # Creates a while loop so that the buttons will work due to inputs being constantly checked.
    while Leaderboard == True:
        pygame.display.update()
        for event in pygame.event.get():
            # Gets mouse position
            mousex, mousey = pygame.mouse.get_pos()
            # If the users mouse is over the back button then turn the text green if it's not make it black
            if (mousex > 5 and mousex < 125) and (mousey > 40 and mousey < 93):
                screen.blit(smallFont.render("Back", 0, green),(40,40))
            else:
                screen.blit(smallFont.render("Back", 0, black),(40,40))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (mousex>5 and mousex<125) and (mousey>40 and mousey<93):
                     main_menu()

def main_game():
    # Gets the global variables used in the function
    global boxColour, lineColour, level
    # Sets the screen size
    screen = pygame.display.set_mode((600, 400))

    # Populates the variables used in level 1 with data
    boxes = 4
    bombs = 2
    timer = 5
    rows = 2

    # Creates a conditional statement for if the player is on level 2
    if level == 2:
        # If that conditional statement is true then it populates the varibles used in level 2 with data
        screen = pygame.display.set_mode((1000, 400))
        boxes = 8
        bombs = 4
        timer = 8
        rows = 2

    # Creates a conditional statement for if the player is on level 3
    if level == 3:
        # If that conditional statement is true then it populates the varibles used in level 3 with data
        screen = pygame.display.set_mode((1200, 600))
        boxes = 15
        bombs = 6
        timer = 10
        rows = 3

    # Creates a conditional statement for if the player is on level 4
    if level == 4:
        # If that conditional statement is true then it populates the varibles used in level 4 with data
        screen = pygame.display.set_mode((1600, 600))
        boxes = 21
        bombs = 10
        timer = 15
        rows = 3

    def board(boxes, bombs):
        # Creates a fixed loop to loop for only the number of boxes needed in 1 row
        for i in range (0, round(boxes / rows)):
            redBoxPositionFromLeft = i * 200
            #Draws row 1 of the red boxes on the screen
            pygame.draw.rect(screen, boxColour, pygame.Rect(redBoxPositionFromLeft, 20, 200, 200))

            #Draws row 2 of the red boxes on the screen
            pygame.draw.rect(screen, boxColour, pygame.Rect(redBoxPositionFromLeft, 220, 200, 200))

            # Creates a conditional statement for if the player is on level 3
            if level >= 3:
                #Draws row 3 of the red boxes on the screen
                pygame.draw.rect(screen, boxColour, pygame.Rect(redBoxPositionFromLeft, 420, 200, 200))
        # Calls the black lines function to draw the lines
        blackLines()

    def blackLines():
        infoObject = pygame.display.Info()
        # Creates a fixed loop to loop for the number of rows + 1
        for i in range (0, rows + 4):

            blackBoxHorizontalFromTop = (i * 200) # could just combine
            blackBoxDiognalFromLeft = (i * 200)

            #diagonal - draws the black lines that go up
            pygame.draw.rect(screen, lineColour, pygame.Rect(blackBoxDiognalFromLeft, 0, 20, infoObject.current_h))

            #horizontal - draws the black lines that go along the way
            pygame.draw.rect(screen, lineColour, pygame.Rect(0, 0, (infoObject.current_w - 200) , 20))
            pygame.draw.rect(screen, lineColour, pygame.Rect(0, blackBoxHorizontalFromTop - 20, (infoObject.current_w - 200) , 20))

    def whatIsSquare(randomNumber, playerScoreTime):
        # Gets global variables and initialises local variables
        global boxesRevealed
        squareIs = str
        boxesRevealed += 1
        # If the number that was passed in is = 0 then the game ends as 0 represents a bomb
        if randomNumber == 0:
            pygame.mixer.Sound.play(pygame.mixer.Sound("gameLoss.wav"))
            enter_Name(playerScoreTime)
        # If the number that was passed in is = 1 then the game passes back out the grass image
        elif randomNumber == 1:
            squareIs = pygame.image.load("grass.png")
            return squareIs
        # If the number that was passed in is = 2 then the game passes back out the power up image and activates the powerup ability
        elif randomNumber == 2:
            squareIs = pygame.image.load("powerup.png")
            playerScoreTime -= 1
            return squareIs

    def gameRunning(timer):
        # Gets global variables and intialises local variables
        global revealCalled
        infoObject = pygame.display.Info()
        isRevealed = True
        timerText = str(timer).rjust(3)
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        counterUpper = int = 0
        running = True
        randomNumber = []
        playerScoreTime = 0
        timerOrigianl = int

        # Manually inputs the correct number of bombs to ensure that the right of number of bombs exists
        for i in range(0,bombs):
            randomNumber.append(0)
        # Inputs the other numbers making sure to only loop for the correct number of squares
        for i in range(0,boxes - bombs):
            randomNumber.append(random.randint(1,2))

        # Shuffles the array so each square is assigned a random number each round
        random.shuffle(randomNumber)

        # Creates a new timer to store the original timer value which the game starts on
        timerOriginal = timer

        while running == True:
            for event in pygame.event.get():
                mousex, mousey = pygame.mouse.get_pos()
                if event.type == pygame.USEREVENT:
                    # For every second in the game the timer will go down and the other variables will go up as they store how long levels are taking
                    timer -= 1
                    counterUpper += 1
                    playerScoreTime += 1
                    # The number that will be drawn on the screen showing how much time is left
                    timerText = str(timer).rjust(3)
                    # Once the time the reveal is on for is over the revealed squares are drawn over and allows the user to clicks squares since the revealed squares are now gone
                    if timer == 0:
                        board(boxes,bombs)
                        timer = 60
                        isRevealed = False
                        counterUpper = 0
                    # Makes it so the game ends when the timer hits 0
                    if counterUpper == 59:
                        enter_Name(playerScoreTime)
                    # Checks the reveal timer is collect and that the game is currently revealing on the right level, reveals the images on the square and makes it so the user can't click squares while the boxes are revealed
                    if timer == (timerOriginal - 1) and revealCalled == level:
                        revealCalled += 1
                        isRevealed = True
                        reveal(timer, counterUpper, randomNumber)

                # Creates a conditional statemement to check that the user has clicked the left mouse button and the game is currently not revealing the squares
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and isRevealed == False:
                    # Allows the squares of level 1 to be clicked on so that they can be revealed
                    if (mousex<=200) and (mousey<=200):
                        screen.blit(whatIsSquare(randomNumber[0], playerScoreTime), (20, 20))

                    if (mousex > 200 and mousex <= 400) and (mousey <= 200):
                        screen.blit(whatIsSquare(randomNumber[1], playerScoreTime), (220, 20))

                    if (mousex < 200) and (mousey >= 200 and mousey <= 400):
                        screen.blit(whatIsSquare(randomNumber[2], playerScoreTime), (20, 200))

                    if (mousex <= 400 and mousex > 200) and (mousey <= 400 and mousey > 200):
                        screen.blit(whatIsSquare(randomNumber[3], playerScoreTime), (220, 200))

                    # If the level is greater than or equal to 2 then allow the squares which first appear in level 2 to be clicked on
                    if level >= 2:
                        if (mousex <= 600 and mousex > 400) and (mousey <= 200):
                            screen.blit(whatIsSquare(randomNumber[4], playerScoreTime), (420, 20))

                        if (mousex <= 800 and mousex > 600) and (mousey <= 200):
                            screen.blit(whatIsSquare(randomNumber[5], playerScoreTime), (620, 20))

                        if (mousex <= 600 and mousex > 400) and (mousey <= 400 and mousey > 200):
                            screen.blit(whatIsSquare(randomNumber[6], playerScoreTime), (420, 200))

                        if (mousex <= 800 and mousex > 600) and (mousey <= 400 and mousey > 200):
                            screen.blit(whatIsSquare(randomNumber[7], playerScoreTime), (620, 200))

                    # If the level is greater than or equal to 3 then allow the squares which first appear in level 3 to be clicked on
                    if level >= 3:
                        if (mousex <= 1000 and mousex > 800) and (mousey <= 200):
                            screen.blit(whatIsSquare(randomNumber[8], playerScoreTime), (820, 20))

                        if (mousex <= 1000 and mousex > 800) and (mousey <= 400 and mousey > 200):
                            screen.blit(whatIsSquare(randomNumber[9], playerScoreTime), (820, 200))

                        if (mousex <= 200) and (mousey > 400 and mousey <= 600):
                            screen.blit(whatIsSquare(randomNumber[10], playerScoreTime), (20, 400))

                        if (mousex > 200 and mousex <= 400) and (mousey > 400 and mousey <= 600):
                            screen.blit(whatIsSquare(randomNumber[11], playerScoreTime), (220, 400))

                        if (mousex > 400 and mousex <= 600) and (mousey > 400 and mousey <= 600):
                            screen.blit(whatIsSquare(randomNumber[12], playerScoreTime), (420, 400))

                        if (mousex > 600 and mousex <= 800) and (mousey > 400 and mousey <= 600):
                            screen.blit(whatIsSquare(randomNumber[13], playerScoreTime), (620, 400))

                        if (mousex > 800 and mousex <= 1000) and (mousey > 400 and mousey <= 600):
                            screen.blit(whatIsSquare(randomNumber[14], playerScoreTime), (820, 400))

                    # If the level is greater than or equal to 4 then allow the squares which first appear in level 4 to be clicked on
                    if level == 4:
                        if (mousex <= 1200 and mousex > 1000) and (mousey <= 200):
                            screen.blit(whatIsSquare(randomNumber[15], playerScoreTime), (1020, 20))

                        if (mousex <= 1400 and mousex > 1200) and (mousey <= 200):
                            screen.blit(whatIsSquare(randomNumber[16], playerScoreTime), (1220, 20))

                        if (mousex <= 1200 and mousex > 1000) and (mousey <= 400 and mousey > 200):
                            screen.blit(whatIsSquare(randomNumber[17], playerScoreTime), (1020, 200))

                        if (mousex <= 1400 and mousex > 1200) and (mousey <= 400 and mousey > 200):
                            screen.blit(whatIsSquare(randomNumber[18], playerScoreTime), (1220, 200))

                        if (mousex <= 1200 and mousex > 1000) and (mousey <= 600 and mousey > 400):
                            screen.blit(whatIsSquare(randomNumber[19], playerScoreTime), (1020, 400))

                        if (mousex <= 1400 and mousex > 1200) and (mousey <= 600 and mousey > 400):
                            screen.blit(whatIsSquare(randomNumber[20], playerScoreTime), (1220, 400))

                    # Redraws the black lines over the squares so the images are not overlapping
                    blackLines()

                # If the user has clicked every box except the ones that are bombs and you aren't on level 4 then it calls the level_complete function - !4 is needed as if you are on level 4 then it displays enter_Name
                if boxesRevealed == (boxes - bombs) and level != 4:
                    level_complete(playerScoreTime)

                # If the user has clicked every box except the ones that are bombs and you are on level 4 then it calls the enter_Name function
                if boxesRevealed == (boxes - bombs) and level == 4: # could just turn this in to else so it geos else: level_complete()
                    pygame.mixer.Sound.play(pygame.mixer.Sound("gameWin.wav"))
                    enter_Name(playerScoreTime)

            # Draws the information on the right side of the screen in the correct positions for level 1
            if level == 1: #4 boxes
                pygame.draw.rect(screen, mainMenuBackGroundColour, pygame.Rect(420, 0, 200, infoObject.current_h))
                screen.blit(smallFont.render("Time Left:", 0, green),(422, 20))
                screen.blit(smallFont.render(timerText, 0, green), (555, 20))

            # Draws the information on the right side of the screen in the correct positions for level 2
            if level == 2: #8 boxes
                pygame.draw.rect(screen, mainMenuBackGroundColour, pygame.Rect(820, 0, 200, infoObject.current_h))
                screen.blit(smallFont.render("Time Left:", 0, green),(820, 20))
                screen.blit(smallFont.render(timerText, 0, green), (945, 20))

            # Draws the information on the right side of the screen in the correct positions for level 3
            if level == 3: # 16 boxes
                pygame.draw.rect(screen, mainMenuBackGroundColour, pygame.Rect(1020, 0, 200, infoObject.current_h))
                screen.blit(smallFont.render("Time Left:", 0, green),(1030, 20))
                screen.blit(smallFont.render(timerText, 0, green), (1150, 20))

            # Draws the information on the right side of the screen in the correct positions for level 4
            if level == 4: # 24 boxes
                pygame.draw.rect(screen, mainMenuBackGroundColour, pygame.Rect(1420, 0, 200, infoObject.current_h))
                screen.blit(smallFont.render("Time Left:", 0, green),(1400, 20))
                screen.blit(smallFont.render(timerText, 0, green), (1550, 20))

            # Updates the display so the information is drawn
            pygame.display.flip()
            # Makes the timer tick so that the timer works correctly
            clock.tick(60)

    def reveal(timer, counterUpper, randomNumber):
        # Passes in the global variable level and initialises an array
        global level
        currentSquare = []

        # Creates a fixed loop to check what each square is then saves the correct picture to the number of the square
        for i in range (0, boxes):
            if randomNumber[i] == 0:
                currentSquare.append(pygame.image.load("bomb.png"))
            elif randomNumber[i] == 1:
                currentSquare.append(pygame.image.load("grass.png"))
            elif randomNumber[i] == 2:
                currentSquare.append(pygame.image.load("powerup.png"))

        # Draws what each square is on the screen in the correct position, and only draws them when they are on the correct level
        screen.blit(currentSquare[0], (20, 20))
        screen.blit(currentSquare[1], (220, 20))
        screen.blit(currentSquare[2], (20, 200))
        screen.blit(currentSquare[3], (220, 200))
        if level >= 2:
            screen.blit(currentSquare[4], (420, 20))
            screen.blit(currentSquare[5], (620, 20))
            screen.blit(currentSquare[6], (420, 200))
            screen.blit(currentSquare[7], (620, 200))
        if level >= 3:
            screen.blit(currentSquare[8], (820, 20))
            screen.blit(currentSquare[9], (820, 200))
            screen.blit(currentSquare[10], (20, 400))
            screen.blit(currentSquare[11], (220, 400))
            screen.blit(currentSquare[12], (420, 400))
            screen.blit(currentSquare[13], (620, 400))
            screen.blit(currentSquare[14], (820, 400))
        if level == 4:
            screen.blit(currentSquare[15], (1020, 20))
            screen.blit(currentSquare[16], (1220, 20))
            screen.blit(currentSquare[17], (1020, 200))
            screen.blit(currentSquare[18], (1220, 200))
            screen.blit(currentSquare[19], (1020, 400))
            screen.blit(currentSquare[20], (1220, 400))
        # Draws the blackLines function so that the images don't overlap the black lines
        blackLines()

    # Draws the board and the gamerunning function so the game functions correctly
    board(boxes, bombs)
    gameRunning(timer)

def level_complete(playerScoreTime):
    # Passes in the global variables and sets the screen to an appropriate size and draws the appropriate image.
    global level, boxesRevealed, revealCalled
    screen = pygame.display.set_mode((1000, 750))
    screen.blit(pygame.image.load("levelCompleteScreen.png"), (0, 0))

    # Draws the text on the screen
    screen.blit(smallFont.render("Next Level", 0, blue),(410, 255))
    screen.blit(smallFont.render("Main Menu", 0, black),(415,415))
    screen.blit(gameTitleFonts.render("Level Complete", 0, blue),(400,100))

    # Updates the display so that the information is drawn.
    pygame.display.update()

    levelComplete = True

    # Creates a while loop so that the buttons function correctly
    while levelComplete == True:
        # Updates the display constantly so the buttons are constantly updated
        pygame.display.update()
        for event in pygame.event.get():
            mousex, mousey = pygame.mouse.get_pos()
            # If the user hovers over the next level button then it turns blue and the other text turns black to avoid both colours being highlighted.
            if (mousex > 394 and mousex < 604) and (mousey > 250 and mousey < 305):
                screen.blit(smallFont.render("Next Level", 0, blue),(410, 255))
                screen.blit(smallFont.render("Main Menu", 0, black),(415, 415))
            # If the user hovers over the Main Menu button then it turns blue and the other text turns black to avoid both colours being highlighted.
            elif (mousex > 394 and mousex < 604) and (mousey > 421 and mousey < 480):
                screen.blit(smallFont.render("Next Level", 0, black),(410, 255))
                screen.blit(smallFont.render("Main Menu", 0, blue),(415, 415))
            # If the user clicks down and clicks on a button then calls it necessary function and sets the variables to the correct values.
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (mousex > 394 and mousex < 604) and (mousey > 250 and mousey < 305):
                    level += 1
                    boxesRevealed = 0
                    main_game()
                elif (mousex > 394 and mousex < 604) and (mousey > 421 and mousey < 480):
                    level = 1
                    boxesRevealed = 0
                    revealCalled = 1
                    playerScoreTime = 0
                    main_menu()

def enter_Name(playerScoreTime):
    # Passes in the global variables
    global level, boxesRevealed, revealCalled
    # Sets the score variable to the correct value
    playerScore = round((level * 1500 / playerScoreTime) + (level * 200))
    # Updates the screen to the correct size and draws the correct information then updates the display so the information is drawn
    screen = pygame.display.set_mode((1000, 750))
    screen.blit(pygame.image.load("enterNameScreen.png"), (0, 0))
    pygame.display.update()
    # Sets relevant variables to correct values.
    user_text = ''
    enterName = True
    nameEntered = False
    # Creates a while loop so that the buttons function correctly
    while enterName == True:
        mousex, mousey = pygame.mouse.get_pos()
        for event in pygame.event.get():
            # If the user presses a key then it redraws the screen again so that it looks like the text is being drawn normally.
            if event.type == pygame.KEYDOWN:
                screen.blit(pygame.image.load("enterNameScreen.png"), (0, 0))
                # If they click backspace then removes the last character
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                # If they aren't clicking backspace or enter then it adds the typed key to their name to avoid invalid characters being added to the name.
                elif event.key != pygame.K_BACKSPACE and event.key != pygame.K_RETURN:
                    user_text += event.unicode
            # Limits user_text to 8 characters
            user_text = user_text[:8]
            # Validates the user has entered something for their name
            if len(user_text) >= 1:
                nameEntered = True
            if len(user_text) == 0:
                nameEntered = False
            # Draws the needed text on the screen
            screen.blit(regularFont.render("Game Over", 0, red),(340, 65))
            screen.blit(smallFont.render("Enter Name", 0, black),(365, 120))
            screen.blit(smallFont.render("Submit Name", 0, black),(400,400))
            screen.blit(regularFont.render("Retry", 0, black),(425,280))
            screen.blit(regularFont.render(user_text, True, black), (284,172))
            # If the user hovers over a button then it functions correctly.
            if (mousex > 394 and mousex < 604) and (mousey > 421 and mousey < 480):
                screen.blit(smallFont.render("Submit Name",0,green),(400,400))
            elif (mousex > 394 and mousex < 604) and (mousey > 294 and mousey < 345):
                screen.blit(regularFont.render("Retry", 0, green),(425,280))
            # Updates thedisplay so the information is shown on screen
            pygame.display.flip()
            # If the user presses mousedown then sets variables which will always be changed regardless of the box the user clicks to the correct value
            if event.type == pygame.MOUSEBUTTONDOWN:
                playerName = user_text
                level = 1
                revealCalled = 1
                boxesRevealed = 0
                # If the user clicks the submit value and they have entered something in the box then calls the database function and sets the nesecarry variables and calls the correct function
                if (mousex > 394 and mousex < 604) and (mousey > 421 and mousey < 480) and nameEntered == True:
                    databaseInsert(playerName, playerScore)
                    playerScoreTime = 0
                    main_menu()
                # If the user clicks the submit value and they have not entered something in the box then draws an error message on the screen
                if (mousex > 394 and mousex < 604) and (mousey > 421 and mousey < 480) and nameEntered == False:
                    screen.blit(regularFont.render("Name Not Entered", 0, black), (284,172))
                    pygame.display.update()
                # If the user clicks retry then resets the time taken and calls the main game function again.
                if (mousex > 394 and mousex < 604) and (mousey > 294 and mousey < 345):
                    playerScoreTime = 0
                    main_game()

#Initialize the Game
main_menu()
pygame.quit()
quit()