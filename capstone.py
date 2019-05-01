# SPGL Minimal Code by /u/wynand1004 AKA @TokyoEdTech
# Requires SPGL Version 0.8 or Above
# SPGL Documentation on Github: https://wynand1004.github.io/SPGL
# Use this as the starting point for your own games

# Import SPGL
import spgl
import random

#specify lives
lives = 3

# Create Classes
class Paddle(spgl.Sprite):
	def __init__(self, shape, color, x, y, width, height):
		super().__init__(shape, color, x, y, width, height)
		self.speed = 0
		self.set_image("paddle.gif", 100, 20)
		
	def tick(self):
		self.move()
		
	def move(self):
		self.fd(self.speed)
		
		if self.xcor() + self.width / 2 > game.SCREEN_WIDTH / 2  :
			self.goto(game.SCREEN_WIDTH /2  - self.width/2 , self.ycor())
			self.speed = 0
			
		if self.xcor() - self.width /2 < -game.SCREEN_WIDTH / 2 :
			self.goto(-game.SCREEN_WIDTH / 2  + self.width/2, self.ycor())
			self.speed = 0

			
	def move_right(self):
		self.setheading(0)
		self.speed = 17
		
	def stop_move_right(self):
		self.speed = 0
		
	
	def move_left(self):
		self.setheading(180)
		self.speed = 17
		
	def stop_move_left(self):
		self.speed = 0
		
	def set_width(self, width):
		self.width = width
		

class Ball(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.speed = 0
		self.dx = 0
		self.set_image("ball.gif", 20, 20)
		
	def tick(self):
		self.move()	
		
	def move(self):
		if self.dx == 0 and self.dy == 0:
			ball.setx(paddle.xcor())
			ball.sety(paddle.ycor() + paddle.height)
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
			global lives
			lives -= 1
			
		if abs(ball.dx) < 1:
			ball.dx *= 1.001
			ball.dy *= 1.001			

		
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
		self.dx = 0
		self.shapesize(stretch_wid=1, stretch_len=2.5, outline=None)
		
	def check_collision(self, ball):
		self.reflect(ball)
		self.destroy()
			
	def reflect(self, ball):
		if ball.xcor() > self.xcor() - self.width /2 and ball.xcor() < self.xcor() + self.width / 2 and ball.ycor() < self.ycor() - 10:
			print("COLLISION BELOW")
			ball.dy *= -1
			ball.tick()
		
		elif ball.xcor() > self.xcor() - self.width /2 and ball.xcor() < self.xcor() + self.width / 2 and ball.ycor() > self.ycor() + 10:
			print("COLLISION ABOVE")
		 
			ball.dy *= -1
			ball.tick()
		
		elif ball.xcor() < self.xcor() - self.width / 2:
			print("LEFT COLLISION")
			ball.dx *= -1
			ball.tick()
		
		elif ball.xcor() > self.xcor() + self.width/2:
			print("rIGHT COLLISION")
			ball.dx *= -1
			ball.tick()
			
		
class Powerup(Brick):
	def __init__(self, shape, color, x, y, type):
		Brick.__init__(self, shape, color, x, y)
		self.type = type
		print("power")
		
		
	def check_collision(self, ball):
		self.reflect(ball)
		self.dy += -3
		print("collision")
		self.move()
		

class Double_Break_Brick(Brick):
	def __init__(self, shape, color, x, y):
		Brick.__init__(self, shape, color, x, y)
		self.collisions = 0
		
		# power ups: player/, slow/, enlarge/, catch, disruption
		
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

#create a list of power-ups
powerups = []

#create a list of double_break bricks
double_bricks = []



#define the first level
level_1 = [
"                                            ",
"       X                                     ",
"   X   X   X                                 ",
"       X                                     ",
"                                             ",
"                                             ",
"                                             ",
"                                             ",
"                      d                      ",
"                    d   d                    ",
"                d   d   d   d                ",
"            d   X   X   d   X   X            ",
"        X   X   X   X   X   X   X   X        ",
"    X   X   X   X   X   X   X   X   X   X    ",
"X   X   X   X   X   p   p   p   p   p   p   p",
"                                             ",
]


# append level 1 to levels
levels.append(level_1)
# Create Functions
	# function to draw the level.
def draw_level(level):
	for y in range(len(level)):
		for x in range(len(level[y])):
			if level[y][x] == "X":
				screen_x = -350 + (x * 16)
				screen_y = 300 - (y * 30)
			
				brick = Brick("square", "blue", screen_x, screen_y)
				bricks.append(brick)
			
			elif level[y][x] == "p":
				screen_x = -350 + (x * 16)
				screen_y = 300 - (y * 30)
				
				oneup = Powerup("square", "blue", screen_x, screen_y, "player")
				powerups.append(oneup)
				
			elif level[y][x] == "s":
				screen_x = -350 + (x * 16)
				screen_y = 300 - (y * 30)
				
				slow = Powerup("square", "blue", screen_x, screen_y, "slow")
				powerups.append(slow)
				
			elif level[y][x] == "e":
				screen_x = -350 + (x * 16)
				screen_y = 300 - (y * 30)
				
				enlarge = Powerup("square", "green", screen_x, screen_y, "enlarge")
				powerups.append(enlarge)
				
			elif level[y][x] == "d":
				screen_x = -350 + (x * 16)
				screen_y = 300 - (y * 30)
				
				double_brick = Double_Break_Brick("square", "white", screen_x, screen_y)
				double_bricks.append(double_brick)

			elif level[y][x] == "catch":
				screen_x = -350 + (x*16)
				screen_y = 300 - (y*30)
				
				catch = Powerup("sqare", "yellow", screen_x, screen_y, "catch")
				powerups.append(catch)

# Initial Game setup
game = spgl.Game(800, 600, "black", "Dakinoid By Dakina", 0)

draw_level(level_1)

# Create Sprites
paddle = Paddle("square", "white", 0, -250, 100, 20)
paddle.width = 100
paddle.height = 20
paddle.shapesize(stretch_wid=1, stretch_len=5, outline=None)
ball = Ball("circle", "skyblue", 0, -229)
ball.width = 20
ball.height = 20


# Create Labels


# Create Buttons

# Set Keyboard Bindings

# talk to Mr.Thompson about on key release
game.set_keyboard_down_binding(spgl.KEY_LEFT, paddle.move_left)
game.set_keyboard_up_binding(spgl.KEY_LEFT, paddle.stop_move_left)
game.set_keyboard_down_binding(spgl.KEY_RIGHT, paddle.move_right)
game.set_keyboard_up_binding(spgl.KEY_RIGHT, paddle.stop_move_right)
game.set_keyboard_down_binding(spgl.KEY_SPACE, ball.start_moving)
while True:
	# Call the game tick method
	game.tick()
	
	
	# check for collision between ball and paddle
	if game.is_collision(paddle, ball):
		ball.dy *= -1
		
		#if ball.xcor() <= paddle.xcor() + 20 and ball.xcor() >= paddle.xcor() - 20:
			#ball.dy *= -1
					
		#elif ball.xcor() > paddle.xcor() + 20:
			#ball.dy *= 0.9
			#ball.dx *= 1.1
				
		#elif ball.xcor() < paddle.xcor() -20:
		#	ball.dx *= 1.1
			#ball.dy *= 0.9
    	
	# check for horizontal collision 
	for brick in bricks:
		if game.is_collision(brick, ball):
			brick.check_collision(ball)
				

			
	# check for collision between ball and double_brick
	for double_brick in double_bricks:
		if game.is_collision(double_brick, ball):
			ball.dy *= -1
			ball.tick()
			double_brick.collisions += 1
			double_brick.color("pink")
			
			if double_brick.collisions == 2:
				double_brick.destroy()
				
	#check for power up block collisions 
	
	for powerup in powerups:
		if game.is_collision(powerup, ball):
			powerup.check_collision(ball)

			
			
			# Check type
			if powerup.type == "player":
				lives += 1
				print(lives)
				
			if powerup.type == "slow":
				ball.dx *= 0.9
				ball.dy *= 0.9
				
			if powerup.type == "enlarge":
				paddle.width = 150
				paddle.shapesize(stretch_wid=1, stretch_len=7.5, outline=None)
				
			if powerup.type == "catch":
				pass
				

	# lives
	if lives == 0:
		game.exit()
    

