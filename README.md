# BattleBoats

battleboats is a terminal game, based on the origional battle ships game and written in python. 

a player can challenge an computer in finding the locations of all the enemies ships first by entering
co-ordinates. 

[you can play the game through this link]

## How to play

The player must first start the game from the main menu after setting the board size and/or number of ships or leaving
them default

the player will be prompted for their name, entering it will start the game. the player will be given a game board 
with '@' symbols, denoting the position of the ships randomly generated for the player.

the player will then be asked to enter an x and y co-ordinate ranging from 0 to the board size - 1, if a hit is 
registered the respective co-ordinates on the board will be marked with an '!' if it misses the board will be marked with an 'X'. the computers chosen co-ordinates will update simultaneously

this continues till all ships have been hit on either board, making the opponent the winner.


## Features

### Randomised and customisable game board

players can set the number of ships and the size of the board from the game menu, upon starting the game the player will be given a randomised game board, making each game different.




## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!