# BattleBoats

battleboats is a terminal game, based on the origional battle ships game and written in python. 

a player can challenge an computer in finding the locations of all the enemies ships first by entering
co-ordinates. 

[you can play the game through this link]

## Game flow

![Game Flow](/Images/Untitled%20Diagram.drawio.png)

## Objectives

I want to create that is randomly generated for a different experience every playthrough.

    Was this achieved?
        Yes
    How was this achieved?
        random number generation is featured both for ship placement for the player and computer as well as
        how the computer picks a set of co-ordinates, this means each game will be different, leaving little 
        room to cheat

I want the game to have an element of customisability to the game

    Was this achieved?
        Yes
    How was this achieved?
        the player can pick the board size of the game and also change both the number of subs and frigates. the player 
        also has the ability to enter their name.

i want to make a game with no bugs or errors present, giving the user a clean experience

    Was this achieved?
        Yes
    How was this achieved?
        took great care with making sure all logic errors have been resolved and have dedicated methods for validating
        integer and string values and past guesses.


## How to play

The player must first start the game from the main menu after setting the board size and/or number of subs and frigates or leaving them default

the player will be prompted for their name, entering it will start the game. the player will be given a game board 
with '@' symbols denoting subs and '##' denoting frigates, the position of these ships are randomly generated for the player.

the player will then be asked to enter an x and y co-ordinate ranging from 0 to the board size - 1, if a hit is 
registered the respective co-ordinates on the board will be marked with an '!' if it misses the board will be marked with an 'X'. the computers chosen co-ordinates will update simultaneously

this continues till all ships have been hit on either board, making the opponent the winner.


## Features

### Randomised and customisable game board

players can set the number of ships and the size of the board from the game menu, upon starting the game the player will be given a randomised game board, making each game different.

### Big and small ships

players can set both the number of subs(small ships) and frigates(big boats).

### Thorough data validation

validation is used on all values entered by the player, leaving very little room for error.

### Score tracking

players are notified if they have hit or missed on each turn and previous guesses from prior rounds, and scores are tallied at the end of each round.

### Visual Feedback

hits and missed are marked on the board that is printed out to the terminal


## Upcoming features

giving the player infomation on whether they have hit a sub or frigate

power-ups, such as the ability to hit more than one tile per round and scanning for enmy ships

game balance that automatically sets a certain number of ships for a corrosponding game board size allowing for 
more balanced and enjoyable games

## Testing

### Linting

i ran my code through pep8 validator and it came out with numerous styling errors.

after going back and cleaning up the file i was only left with "line to long errors" 


### Manual Testing

i checked all areas where input is required from the player to make sure the results are expected

### Main menu

at the main menu the only chracters than can be entered that will progress the player is "q" (start game), "w" (change size) and "e" (change number of ship) any other input will make the application ask for input that is either of these chracters. typing any of these chracters in uppercase will have no change on the result of the command.

![main menu validation](/Images/main%20menu%20validation.png)

### Changing game settings

when changing settings the applicable range of numbers are printed alongside the prompt for input, leaving little room for misunderstanding of what is being asked. if an invalid chracter is inputted such as a letter or symbol or a number outside that range, an error message is thrown to the player letting them know where they have gone wrong.

![settings validation](/Images/settings%20validation.png)

### Picking co-ordinates

when picking co-ordinates the numbers inputted by the player are put through the same testing that the integers for the setting have gone through. however a set of co-ordinates can only be guessed once. inputting a set of co-ordinates more than once will throw and error to the player telling them to enter a new set or co-ordinates.

![picking validation](/Images/guesses%20validation.png)

## Bugs

i wanted my co-ordinates to start from bottom left as you see it on the console however this caused me issues due to how messages are printed to the board, i sussed out that if i printed the board in reverse the feedback would be printed the right way however my input was wrong every time, this gave me a great deal of trouble even to the point of writing a small mock up of the logic so i could get a better idea of how it worked. i found the solution after a while and it was simple. the ships were being printed to the board in reverse ie "[y][x]" due to how the board was being printed, but the guesses were being inputted as "[x][y]" meaning they were being flipped. this has now been solved.


## Deployment

There were many steps to deploying this project to Heroku:

    If I had installed any packages to Gitpod, I would need to add then to a list of requirements.

    To do this I would have typed pip3 freeze > requirements.txt and hit enter, this would update the requirements.txt file.
    I'd need to commit and push this to Github.
    Heroku will use this list to install the dependencies into the application before the project is run.
    However, I didn't need to do this as I had no packages installed.

    I went over to my Heroku dashboard and clicked on 'create a new app'.
    I chose a name for my app; every app must have a unique name so I couldn't call it hangman as this was already taken so I went for hang-the-guy.
    Selected my region and clicked create app.
    I then went to the tab at the top of the page and clicked on settings.
    Some apps will include sensitive data in the gitpod workspace that isn't in the github repository because it has been deliberately protected in the gitnore.file. I didn't have any sensitive data to protect but if I had done, I would have needed to create a config var to allow Heroku access to this data.

    To do this, I would have clicked reveal config vars.
    Filled in the key for example: CREDS
    Then copy and pasted the contents of that 'CREDS' file into the value field and clicked add.

    I added the buildpacks needed by clicking on the buildpack button.

    Here I selected python and pressed save changes.
    Then repeated the same process but selected nodejs this time.
    making sure it was done in that order with python at the top and nodejs under.

    I scrolled back up to the tab at the top and clicked deploy.
    I selected github as the deployment method and clicked connect to github.
    Once this is selected, I then searched for my github repository name, and connected to the correct repository.
    Then I scrolled down, here there were two options.

    The first option being to enable automatic deployment, which means that Heroku will rebuild the app every time I pushed a change to github.
    The other option being to manually deploy, which is the choice I went for with this project.

    When all the code is received from github there is a view button that it a link to the running app, I clicked this to make sure everything was running as expected.

## Credits