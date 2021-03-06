from __future__ import division
from __future__ import print_function

import sys

import OpenGL.GL as gl
import OpenGL.GLU as glu
import OpenGL.GLUT as glut


def init() :
    gl.glClearColor(0.0, 0.0, 0.0, 0.0)
    gl.glShadeModel(gl.GL_FLAT)


def display() :
    global camera
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    gl.glPushMatrix()
    gl.glRotatef(camera, 1.0, 0.0, 0.0)
    gl.glColor3f(0.3, 0.7, 0.25)         # toroide de cor verde
    glut.glutWireTorus(0.5, 1.0, 20, 50) # criacao de um toroide:
                                         #   0.5 raio interno
                                         #   1.0 raio externo
                                         #   20 lados para cada secao radial
                                         #   50 divisoes radiais para o toroide
    gl.glPopMatrix()
    glut.glutSwapBuffers()


def reshape(w, h) :
    gl.glViewport (0, 0, w, h)
    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity ()

    # angulo de visao na direcao Y modificado de 60.0 para 55.0
    glu.gluPerspective(55.0, w/h, 1.0, 20.0)

    gl.glMatrixMode(gl.GL_MODELVIEW)
    gl.glLoadIdentity()

    # posicao do olho no eixo X modificada de 0.0 para 1.0
    # posicao do olho no eixo Y modificada de 0.0 para 2.0
    # posicao do olho no eixo Z modificada de 5.0 para 3.5
    glu.gluLookAt(1.0, 2.0, 3.5, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)


def keyboard(key, x, y) :
    global camera
    if key == 'c' :
        camera = (camera + 10) % 360
    elif key == 'C' :
        camera = (camera - 10) % 360
    else :
        return
    glut.glutPostRedisplay()


def main() :
    _ = glut.glutInit(sys.argv)
    glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB)

    glut.glutInitWindowSize(500, 500)
    glut.glutInitWindowPosition(100, 100)
    _ = glut.glutCreateWindow(sys.argv[0])

    init()

    global camera
    camera = 0
    _ = glut.glutDisplayFunc(display)
    _ = glut.glutReshapeFunc(reshape)
    _ = glut.glutKeyboardFunc(keyboard)

    glut.glutMainLoop()


if __name__ == "__main__" :
    main()
