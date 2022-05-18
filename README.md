# BattleBoats
 
Battleboats is a terminal game, based on the original battleships game and written in python.
 
a player can challenge an computer in finding the locations of all the enemies ships first by entering
co-ordinates.
 
[you can play the game through this link](https://battle-boats.herokuapp.com/)
 
## Game flow
 
![Game Flow](/Images/Untitled%20Diagram.drawio.png)
 
## Objectives
 
1. I want to create a game that is randomly generated for a different experience every playthrough.
 
- Was this achieved?
    - Yes
- How was this achieved?
    - random number generation is featured both for ship placement for the player and computer as well as
    how the computer picks a set of coordinates, this means each game will be different, leaving little
    room to cheat
 
2. I want the game to have an element of customizability to the game
 
- Was this achieved?
    - Yes
- How was this achieved?
    - The player can pick the board size of the game and also change both the number of subs and frigates. the player
    also has the ability to enter their name.
 
3. I want to make a game with no bugs or errors present, giving the user a clean experience
 
- Was this achieved?
    - Yes
- How was this achieved?
    took great care with making sure all logic errors have been resolved and have dedicated methods for validating
    integer and string values and past guesses.
 
 
## How to play
 
- The player must first start the game from the main menu after setting the board size and/or number of subs and frigates or leaving them default
 
- The player will be prompted for their name, entering it will start the game. the player will be given a game board
with '@' symbols denoting subs and '##' denoting frigates, the position of these ships are randomly generated for the player.
 
- The player will then be asked to enter an x and y coordinate ranging from 0 to the board size - 1, if a hit is
registered the respective coordinates on the board will be marked with an '!' if it misses the board will be marked with an 'X'. the computers chosen coordinates will update simultaneously
 
- this continues till all ships have been hit on either board, making the opponent the winner.
 
 
## Features
 
### Randomised and customisable game board
 
- Players can set the number of ships and the size of the board from the game menu, upon starting the game the player will be given a randomised game board, making each game different.

![randomised game board](/Images/features%20randomisation.png)
 
### Big and small ships
 
- Players can set both the number of subs(small ships) and frigates(big boats).

![big and small ships](/Images/features%20ship%20sizes.png)
 
### Thorough data validation
 
- Validation is used on all values entered by the player, leaving very little room for error. this is shown in greater detail further in the documentation


### Score tracking
 
- Players are notified if they have hit or missed on each turn and previous guesses from prior rounds, and scores are tallied at the end of each round.

![score tracking](/Images/features%20score.png)
 
### Visual Feedback
 
- Hits and misses are marked on the board that is printed out to the terminal

![visual feedback](/Images/features%20v5s4a3%20feedbac2.png) 
 
## Upcoming features
 
- Giving the player information on whether they have hit a sub or frigate
 
- Power-ups, such as the ability to hit more than one tile per round and scanning for enemy ships
 
- Game balance that automatically sets a certain number of ships for a corresponding game board size allowing for
more balanced and enjoyable games
 
## Testing
 
### Linting
 
I ran my code through pep8 validator and it came out with numerous styling errors.
 
![pep8 before](/Images/pep8%20before.png)
 
After going back and cleaning up the file I was only left with "line too long errors" which I struggled with repairing as I didnt have the skill set to do it in a way that didnt raise more errors. 
 
![line shortening](/Images/line%20short.png)

![pep8 after](/Images/linto.png)

 
 
### Manual Testing
 
I checked all areas where input is required from the player to make sure the results are expected
 
### Main menu
 
At the main menu the only characters that can be entered that will progress the player is "q" (start game), "w" (change size) and "e" (change number of ship) any other input will make the application ask for input that is either of these characters. typing any of these characters in uppercase will have no change on the result of the command.
 
![main menu validation](/Images/main%20menu%20validation.png)
 
### Changing game settings
 
When changing settings the applicable range of numbers are printed alongside the prompt for input, leaving little room for misunderstanding of what is being asked. if an invalid character is inputted such as a letter or symbol or a number outside that range, an error message is thrown to the player letting them know where they have gone wrong.
 
![settings validation](/Images/settings%20validation.png)
 
### Picking coordinates
 
When picking coordinates the numbers inputted by the player are put through the same testing that the integers for the setting have gone through. however a set of coordinates can only be guessed once. inputting a set of coordinates more than once will throw an error to the player telling them to enter a new set of coordinates.
 
![picking validation](/Images/guesses%20validation.png)
 
## Bugs
 
I wanted my coordinates to start from bottom left as you see it on the console however this caused me issues due to how messages are printed to the board.
 
 I sussed out that if I printed the board in reverse the feedback would be printed the right way however my input was wrong every time, this gave me a great deal of trouble even to the point of writing a small mock up of the logic (test.py) so I could get a better idea of how it worked. I found the solution after a while and it was simple.
 
 The ships were being printed to the board in reverse i.e. "[y][x]" due to how the board was being printed, but the guesses were being inputted as "[x][y]" meaning they were being flipped. This has now been solved.


![testing](/Images/testDOTpy.png)
 
## Deployment
 
There were many steps to deploying this project to Heroku:
 
1. If I had installed any packages to Gitpod, I would need to add them to a list of requirements.
 
- To do this I would have typed pip3 freeze > requirements.txt and hit enter, this would update the requirements.txt file.
- I'd need to commit and push this to Github.
- Heroku will use this list to install the dependencies into the application before the project is run.
- However, I didn't need to do this as I had no packages installed.
 
2. I went over to my Heroku dashboard and clicked on 'create a new app'.
3. I chose a name for my app; every app must have a unique name, battle-boats had not been taken
4. Selected my region and clicked create app.
5. I then went to the tab at the top of the page and clicked on settings.
6. Some apps will include sensitive data in the gitpod workspace that isn't in the github repository because it has been deliberately protected in the gitignore.file. I didn't have any sensitive data to protect but if I had done, I would have needed to create a config var to allow Heroku access to this data.
 
- To do this, I would have clicked reveal config vars.
- Filled in the key for example: CREDS
- Then copy and paste the contents of that 'CREDS' file into the value field and clicked add.
 
7. I added the buildpacks needed by clicking on the buildpack button.
 
- Here I selected python and pressed save changes.
- Then repeated the same process but selected nodejs this time.
- making sure it was done in that order with python at the top and nodejs under.
 
8. I scrolled back up to the tab at the top and clicked deploy.
9. I selected github as the deployment method and clicked connect to github.
10. Once this is selected, I then searched for my github repository name, and connected to the correct repository.
11. Then I scrolled down, here there were two options.
 
- The first option is to enable automatic deployment, which means that Heroku will rebuild the app every time I pushed a change to github.
- The other option being to manually deploy, which is the choice I went for with this project.
 
12. When all the code is received from github there is a view button that is a link to the running app, I clicked this to make sure everything was running as expected.
 
## Credits
 
- [draw.io](https://draw.io) was used to create my flowchart.
 
- [pep8](https://pep8online.com) was used to validate the code.
 
- [google](https://google.com) was used to look up various coding questions.
