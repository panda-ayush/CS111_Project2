######################################################
# Project: Project 2: A Simple Video Game
# UIN: 671442036
# repl.it URL: https://replit.com/@CS111-Fall2021/Project-2-AyushPanda4#main.py

#For this project, I received help from the following members of CS111.

 
######################################################

#import turlte
import turtle

# main method
def main():
  #set up screen size and background as well as tracer
    s = turtle.Screen()
    s.screensize(300, 300)
    w, h = s.screensize()
    s.setup(w + 20, h + 20)
    s.bgpic("space.gif")
    s.bgcolor("black")
    s.tracer(0)

#dictionary containing info about the gam
    game_info = {"lives": 2, "score": 0, "game_state": "not begin", "level": 1}
#dictionary containg info about turtle objects
    objects = [{"t": turtle.Turtle(), "radius": 30, "x": w / 2, "y": -80, "img": "enemy.gif", "type": "enemy"}]

    objects.append({"t": turtle.Turtle(), "radius": 30, "x": 0, "y": -150, "img": "spacecraft.gif", "type": "player"})

    objects.append({"t": turtle.Turtle(), "radius": 30, "x": -w / 2, "y": -10, "img": "enemy.gif", "type": "enemy2"})

    objects.append({"t": turtle.Turtle(), "radius": 30, "x": w / 2, "y": 60, "img": "enemy.gif", "type": "enemy3"})

    objects.append({"t": turtle.Turtle(), "radius": 30, "x": 0, "y": 150, "img": "rock.gif", "type": "rock"})

    objects.append({"pen_color": "white", "write_arg": "Press Space to start game", "t": turtle.Turtle(), "img": "space.gif","type": "begin_screen", "x": 0, "y": 0})

#dictionary containing information about variables
    variables = [({"t": turtle.Turtle(), "radius": 30, "x": -150, "y": 150, "img": "space.gif", "type": "score", "pen_color": "white"})]

    variables.append({"t": turtle.Turtle(), "radius": 30, "x": -150, "y": 150, "img": "space.gif", "type": "lives", "pen_color": "white"})

    variables.append({"t": turtle.Turtle(), "radius": 30, "x": -150, "y": -150, "img": "space.gif", "type": "levels", "pen_color": "white"})

    variables.append({"t": turtle.Turtle(), "radius": 30, "x": 0, "y": 0, "img": "space.gif", "type": "Game_Over", "pen_color": "white"})

    variables.append({"t": turtle.Turtle(), "radius": 30, "x": 0, "y": 0, "img": "space.gif", "type": "Winner", "pen_color": "white"})

    
#function for when up key is pressed
    def up():
        for obj in objects:
            if obj["type"] == "player":
                obj["y"] += 10
#function for when down key is pressed
    def down():
        for obj in objects:
            if obj["type"] == "player":
                obj["y"] -= 10
#function for when left arrow is pressed
    def left():
        for obj in objects:
            if obj["type"] == "player":
                obj["x"] -= 10
#function for when right arrow is pressed
    def right():
        for obj in objects:
            if obj["type"] == "player":
                obj["x"] += 10
#function for when space bar is pressed
    def space():
        game_info["game_state"] = "begin"
        for obj in objects:
            obj["t"].clear()

#while loop for game start screen         
    while game_info["game_state"] == "not begin":
        for obj in objects:
            if obj["type"] == "begin_screen":
                obj["t"].hideturtle()
                obj["t"].pencolor(obj["pen_color"])
                obj["t"].write(obj["write_arg"], align="center", font= ("Times New Roman", 15))
                s.onkey(space, "space")
                s.listen()
                
                break

#while loop for game
    while game_info["game_state"] == "begin":

      for obj in objects:
        objects[5]["t"].hideturtle()

        while game_info["lives"] > 0:
          
            for obj in variables:
              obj["t"].clear()
#turtle method for variables
              if obj["type"] == "score":
                  obj["t"].hideturtle()
                  obj["t"].penup()
                  obj["t"].pencolor(obj["pen_color"])
                  obj["t"].goto(-150, 130)
                  obj["t"].write(("Score", game_info["score"]), align="Left", font= ("Times New Roman", 10))
                  

            
              if obj["type"] == "lives":
                  obj["t"].hideturtle()
                  obj["t"].penup()
                  obj["t"].pencolor("white")
                  obj["t"].goto(150, 130)
                  obj["t"].write(("Lives", game_info["lives"]), align="right", font= ("Times New Roman", 10))
                  
                
           
              if obj["type"] == "levels":
                  obj["t"].hideturtle()
                  obj["t"].penup()
                  obj["t"].pencolor("white")
                  obj["t"].goto(-150, -130)
                  obj["t"].write(("Level", game_info["level"]), align="left", font= ("Times New Roman", 10))
                  

            for obj in objects:
              s.addshape(obj["img"])
              obj["t"].shape(obj["img"])
            obj["t"].clear()

            for obj in objects:
#player turtle
                if (obj["type"] == "player"):
                    obj["t"].penup()
                    
                    s.onkey(up, "Up")
                    s.onkey(down, "Down")
                    s.onkey(left, "Left")
                    s.onkey(right, "Right")
#first enemy turtle
                if (obj["type"] == "enemy"):
                    
                    obj["t"].penup()
                    if game_info["level"] == 1:
                      obj["x"] -= 0.25
                    elif game_info["level"] == 2:
                      obj["x"] -= 0.50
                    elif game_info["level"] == 3:
                      obj["x"] -= 0.75
                    if obj["x"] < -w / 2:
                        obj["x"] = int(w / 2)
#second enemy turtle
                if (obj["type"] == "enemy2"):
                    
                    obj["t"].penup()
                    if game_info["level"] == 1:
                      obj["x"] += 0.25
                    elif game_info["level"] == 2:
                      obj["x"] += 0.50
                    elif game_info["level"] == 3:
                      obj["x"] += 0.75
                    if obj["x"] > w / 2:
                        obj["x"] = int(-w / 2)
#third enemy turtle 
                if (obj["type"] == "enemy3"):
                    
                    obj["t"].penup()
                    if game_info["level"] == 1:
                      obj["x"] -= 0.25
                    elif game_info["level"] == 2:
                      obj["x"] -= 0.50
                    elif game_info["level"] == 3:
                      obj["x"] -= 0.75
                    if obj["x"] < -w / 2:
                        obj["x"] = int(w / 2)
#score increaser variable
                if (obj["type"] == "rock"):
                    
                    obj["t"].penup()

                while game_info["score"] == 30:
                  for obj in objects:
                    obj["t"].hideturtle()
                  for obj in variables:
                    obj["t"].hideturtle()
                  game_info["game_state"] == "winner"

            for obj in objects:
#collision detection and variable updaters
              if (objects[1]["t"].distance(objects[0]["t"]) == 0):
                game_info["lives"] -= 1
                objects[1]["x"] = 0
                objects[1]["y"] = -150
                objects[1]["t"].goto(objects[1]["x"], objects[1]["y"])

              elif(objects[1]["t"].distance(objects[2]["t"]) == 0):
                game_info["lives"] -= 1
                objects[1]["x"] = 0
                objects[1]["y"] = -150
                objects[1]["t"].goto(objects[1]["x"], objects[1]["y"])

              elif (objects[1]["t"].distance(objects[3]["t"]) == 0):
                game_info["lives"] -= 1
                objects[1]["x"] = 0
                objects[1]["y"] = -150
                objects[1]["t"].goto(objects[1]["x"], objects[1]["y"])

              elif (objects[1]["t"].distance(objects[4]["t"]) == 0):
                game_info["score"] += 10
                game_info["level"] += 1
                objects[1]["x"] = 0
                objects[1]["y"] = -150
                objects[1]["t"].goto(objects[1]["x"], objects[1]["y"])
              else:
                obj["t"].goto(obj["x"], obj["y"])

            s.listen()
            s.update()
        while game_info["lives"] <= 0:
          for obj in objects:
            obj["t"].clear()
          
          for obj in variables:
              obj["t"].clear()
#Game over message screen
              if obj["type"] == "Game_Over":
                  obj["t"].hideturtle()
                  obj["t"].penup()
                  obj["t"].pencolor("white")
                  obj["t"].goto(0, 0)
                  obj["t"].write("Game Over", align="center", font= ("Times New Roman", 20))
#Game win message screen
    while game_info["game_state"] == "winner":
      for obj in variables:
              if obj["type"] == "Winner":
                  obj["t"].hideturtle()
                  obj["t"].penup()
                  obj["t"].pencolor("white")
                  obj["t"].goto(0, 0)
                  obj["t"].write("You Win!", align="center", font= ("Times New Roman", 20))


#main method call
main()