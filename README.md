# CS111_Project2
The game project


What you will demonstrate
Ability to solve small problems that are part of a larger problem
Ability to represent solutions as combinations of blocks, conditionals and loops
Ability to write Python code to implement solutions
Ability to use good programming style


What you will produce
You'll produce a simple video game where the player must navigate from the bottom of the screen to a specific location at the top;  it will share some similarities with the classic arcade game Frogger (​​http://www.happyhopper.org/)   but it should work like my demonstration version in the 10/22 lectures.  You can not use PyGame or some other game package for this project.   
The game should have a start screen with the name of the game and instructions for the player.  Pressing the Enter or Space key should start the game.
In the game play, your player character will start in the middle of the bottom "row" of the screen, with the goal to come in contact with the benefit object in the top row.  The player moves up/down/left/right in response to arrow keys, and vertical movement should move the player from one row/lane to another.
While the player is trying to reach the destination, 'harm" objects will be moving across the screen, with objects in rows moving right-to-left or left-to-right.   Collision with a harm object should reduce the number of lives remaining and move the player back to the starting position.
Collision with the benefit object should increase the level and move the player back to the starting location.   At each new level, the benefit object (the destination)  should be in a random left/right position in the top row of the game screen.
At each new level, the harm objects should move faster (a little bit.)
When lives are reduced to zero, the game ends - the animation loop should stop and a message should be displayed.  The message should include the score and the level reached. 
Your game should have some theme, implemented as the background image and the game object images.
You'll need to divide the game board into "rows" or "lanes", and the height of these should match the visible size of your images.   Images that are 30 pixels in diameter will let you easily divide the game space into rows/lanes.   You'll have the start and destination rows, then 8 rows of harm objects.

