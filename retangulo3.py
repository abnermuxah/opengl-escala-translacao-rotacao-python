from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
scale = 1
transx = transy = 1
rota = 1
def draw1():
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(10,-10,10,-10)

    glScale(scale,scale,0)
    glTranslate(transx, transy, 0)
    glRotate(rota, rota, rota, 0)

    glBegin(GL_POLYGON)
    glColor3d(1, 0, 0)
    glVertex3d(-1, -1, 1)

    glColor3d(0, 1, 0)
    glVertex3d(1, -1, 1)

    glColor3d(0, 0, 1)
    glVertex3d(1, 1, 1)

    glColor3d(1, 1, 1)
    glVertex3d(-1, 1, 1)

    glEnd()
    glFlush()
def keyboard(key, x, y):
    ch = key.decode("utf-8") # a funcao so aceita formato string
    global scale, transx, transy, rota
    if ch == '+':
        scale += 0.5
    if ch == '-':
        scale -= 0.5
    if ch == 'w':
        transy -= 0.5
    if ch == 's':
        transy += 0.5
    if ch == 'a':
        transx += 0.5
    if ch == 'd':
        transx -= 0.5
    if ch == 'y':
        rota += 1
    if ch == 'h':
        rota -= 1
    draw1()
if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(800, 600)
    glutCreateWindow('Window')
    glClearColor(0.2,0.2,0.2,0)
    glutKeyboardFunc(keyboard)
    glutDisplayFunc(draw1)
    glutMainLoop()
