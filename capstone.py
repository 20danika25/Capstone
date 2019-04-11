# SPGL Minimal Code by /u/wynand1004 AKA @TokyoEdTech
# Requires SPGL Version 0.8 or Above
# SPGL Documentation on Github: https://wynand1004.github.io/SPGL
# Use this as the starting point for your own games

# Import SPGL
import spgl
import random

# Create Classes
class Paddle(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.speed = 0
	
	def tick(self):
		self.move()
		
	def move(self):
		self.fd(self.speed)
		
		if self.xcor() > game.SCREEN_WIDTH / 2 - 20:
			self.goto(game.SCREEN_WIDTH / 2 - 20, self.ycor())
			self.speed = 0
			self.setheading(0)
			
		if self.xcor() < -game.SCREEN_WIDTH / 2 + 10:
			self.goto(-game.SCREEN_WIDTH / 2 + 10, self.ycor())
			self.speed = 0
			self.setheading(180)
			
	def move_right(self):
		self.setheading(0)
		self.speed = 10
	
	
	def move_left(self):
		self.setheading(180)
		self.speed = 10
		

class Ball(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.speed = 0
		self.dx = 0

		
	def tick(self):
		self.move()	
		
	def move(self):
		self.goto(self.xcor() + self.dx, self.ycor() + self.dy)
		
		if self.xcor() > game.SCREEN_WIDTH / 2 - 20:
			self.dx *= -1
			
			
		if self.xcor() < -game.SCREEN_WIDTH / 2 + 10:
			self.dx *= -1
			
		
		if self.ycor() > game.SCREEN_HEIGHT / 2 - 10:
			self.dy *= -1
		
		if self.ycor() < -game.SCREEN_HEIGHT / 2 + 20:
			self.goto(0,-229)
			self.dy = 0
			self.dx = 0


		
	def start_moving(self):
		self.dx = 5
		self.dy = 5
		self.heading = random.randint(50,130)
			
	
		
class Brick(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.speed = 0
		self.width = 50
		self.height = 20
		self.shapesize(stretch_wid=1, stretch_len=2.5, outline=None)
		

		
class Powerup(Brick):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		Brick.__init__(self,shape,color,x, y)
		
		
class Pen(spgl.Sprite): # for the actual bricks
	def __init__(self):
		spgl.Sprite.__init__(self)
		self.shape("square")
		self.color(white)
		self.penup()
		self.speed(0)
		
# create a list of levels
levels = [""]

# create a list of bricks
bricks = []

#define the first level
level_1 = [
"                                           ",
"X                                         X",
"X                                         X",
"X                                         X",
"X                                         X",
"X                                         X",
"X                                         X",
"X                                         X",
"X                                         X",
"X                                         X",
"X                                         X",
"X                                         X",
"X                                         X",
"X                                         X",
"X                                         X",
"                                           ",
]
# append level 1 to levels
levels.append(level_1)
# Create Functions
	# function to draw the level.
def draw_level(level):
	for y in range(len(level)):
		for x in range(len(level[y])):
			if level[y][x] == "X":
				screen_x = -300 + (x * 16)
				screen_y = 300 - (y * 30)
			
				brick = Brick("square", "white", screen_x, screen_y)
				bricks.append(brick)



# Initial Game setup
game = spgl.Game(800, 600, "black", "Dakinoid By Dakina", 0)

draw_level(level_1)

# Create Sprites
paddle = Paddle("square", "white", 0, -250)
paddle.width = 100
paddle.height = 20
paddle.shapesize(stretch_wid=1, stretch_len=5, outline=None)
ball = Ball("circle", "skyblue", 0, -229)
ball.width = 20
ball.height = 20


# Create Labels

# Create Buttons

# Set Keyboard Bindings
game.set_keyboard_binding(spgl.KEY_LEFT, paddle.move_left)
game.set_keyboard_binding(spgl.KEY_RIGHT, paddle.move_right)
game.set_keyboard_binding(spgl.KEY_SPACE, ball.start_moving)
while True:
	# Call the game tick method
	game.tick()

	# check for collision between ball and paddle
	if game.is_collision(paddle, ball):
		ball.dy *= -1
    	
	# check for collision between ball and brick
	for brick in bricks:
		if game.is_collision(brick, ball):
			print("hit")
			ball.dy *= -1
			brick.destroy()
    

