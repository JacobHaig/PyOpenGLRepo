### Pygame and PyOpenGL are a must
import pygame 
from pygame.locals import * 

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = ((1,-1,-1),
			(1, 1,-1),
			(-1, 1,-1),
			#(-.5, 0.5,-.5),
			(-1,-1,-1),
			(1,-1, 1),
			(1, 1, 1),
			(-1,-1, 1),
			(-1, 1, 1))

edges = ((0, 1),
		 (0, 3),
		 (0, 4),
		 (2, 1),
		 (2, 3),
		 (2, 7),
		 (6, 3),
		 (6, 4),
		 (6, 7),
		 (5, 1),
		 (5, 4),
		 (5, 7))

surfaces = ((0, 1, 2, 3),
			(3, 2, 7, 6),
			(6, 7, 5, 4),
			(4, 5, 1, 0),
			(1, 5, 7, 2),
			(4, 0, 3, 6))


def cube():
	
	# Draw the Faces
	glBegin(GL_QUADS)
	for sureface in surfaces:
		#glColor3fv((0, 1, 0)) # Single Colored Faces
		for vertex in sureface:
			glColor3fv((vertices[vertex][0],vertices[vertex][1],vertices[vertex][2])) # Multi Color
			glVertex3fv(vertices[vertex])
	glEnd()

	# Draw the Lines
	glBegin(GL_LINES)
	for edge in edges:
		glColor3fv((1, 0, 0)) # Single Colored Lines
		for vertex in edge:
			glVertex3fv(vertices[vertex])
	glEnd()

# Main Function
def main():
	# Start Pygame with OpenGL
	pygame.init()
	display = (800,600)
	pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

	# Perspective, Translation, and Rotation Init
	gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
	glTranslatef(0.0, 0.0, -4.0)
	glRotatef(0,0,0,0)

	# Quit Pygame
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		# Main loop
		glRotatef(1, 3, 1, 1)
		# Clear Screen
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		# Call Cube.  Draws the faces and lines of the cube
		cube()
		# Update the display
		pygame.display.flip() 
		# Sleep the program for 10ms
		pygame.time.wait(10)

# Call the main function
main()