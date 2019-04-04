# SPGL Minimal Code by /u/wynand1004 AKA @TokyoEdTech
# Requires SPGL Version 0.8 or Above
# SPGL Documentation on Github: https://wynand1004.github.io/SPGL
# Use this as the starting point for your own games

# Import SPGL
import spgl

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
		self.speed = 8
	
	
	def move_left(self):
		self.setheading(180)
		self.speed = 8
		

class Ball(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.speed = 0
		
		
	def move(self):
		self.fd(self.speed)
		
		if self.xcor() > game.SCREEN_WIDTH / 2 - 20:
			self.goto(game.SCREEN_WIDTH / 2 - 20, self.ycor())

			
		if self.xcor() < -game.SCREEN_WIDTH / 2 + 10:
			self.goto(-game.SCREEN_WIDTH / 2 + 10, self.ycor())

		
		if self.ycor() > game.SCREEN_HEIGHT:
			self.goto(self.xcor, game.SCREEN_HEIGHT)
			self.rt(40)
		
			
		
		
# Create Functions

# Initial Game setup
game = spgl.Game(800, 600, "black", "Dakinoid By Dakina", 0)

# Create Sprites
paddle = Paddle("square", "white", 0, -250)
ball = Ball("circle", "skyblue", 0, -229)
# Create Labels

# Create Buttons

# Set Keyboard Bindings
game.set_keyboard_binding(spgl.KEY_LEFT, paddle.move_left)
game.set_keyboard_binding(spgl.KEY_RIGHT, paddle.move_right)

while True:
    # Call the game tick method
    game.tick()
