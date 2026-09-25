# ============================================================
# RAILWAY CROSSING SAFETY SIMULATION
# Computer Graphics Sessional Project
#
# CG Techniques:
# 1. Line & Shape Drawing
# 2. 2D Transformations
# 3. Color Fill
# 4. Line Clipping
#
# Controls:
# SPACE = Pause / Resume
# +     = Increase train speed
# -     = Decrease train speed
# R     = Reset simulation
# ESC   = Exit
# ============================================================
 
import sys
import math
 
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
 
 
# ============================================================
# GLOBAL VARIABLES
# ============================================================
 
train_x = -250.0
train_speed = 2.0
 
# 90 degrees = open, 0 degrees = closed
gate_angle = 90.0
gate_speed = 2.0
 
signal_red = False
 
car_y = -100.0
car_speed = 1.5
 
paused = False
 
 
# ============================================================
# BASIC DRAWING FUNCTIONS
# ============================================================
 
def draw_rectangle(x1, y1, x2, y2, r, g, b):
    # What it does: Draws a filled rectangle.
    # When used: Used for road, train, car, gate and signal.
    # Real-world use: UI rendering, maps and vector graphics.
 
    glColor3f(r, g, b)
 
    glBegin(GL_QUADS)
 
    glVertex2f(x1, y1)
    glVertex2f(x2, y1)
    glVertex2f(x2, y2)
    glVertex2f(x1, y2)
 
    glEnd()
 
 
def draw_line(x1, y1, x2, y2, width=2):
    # What it does: Draws a straight line between two points.
    # When used: Used for railway tracks and road markings.
    # Real-world use: Maps, CAD and vector graphics.
 
    glLineWidth(width)
 
    glBegin(GL_LINES)
 
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
 
    glEnd()
 
 
def draw_circle(cx, cy, radius, r, g, b):
    # What it does: Draws a filled circle.
    # When used: Used for traffic lights and gate pivot.
    # Real-world use: Traffic indicators and UI systems.
 
    glColor3f(r, g, b)
 
    glBegin(GL_TRIANGLE_FAN)
 
    glVertex2f(cx, cy)
 
    for i in range(361):
 
        angle = math.radians(i)
 
        x = cx + radius * math.cos(angle)
        y = cy + radius * math.sin(angle)
 
        glVertex2f(x, y)
 
    glEnd()
 
 
# ============================================================
# TEXT DRAWING
# ============================================================
 
def draw_text(x, y, text, r=1.0, g=1.0, b=1.0):
    # Draws simple text on the OpenGL window.
 
    glColor3f(r, g, b)
 
    glRasterPos2f(x, y)
 
    for character in text:
 
        glutBitmapCharacter(
            GLUT_BITMAP_HELVETICA_12,
            ord(character)
        )
 
 
# ============================================================
# LINE CLIPPING
# ============================================================
 
def clip_vertical_line(y1, y2, min_y, max_y):
    # What it does:
    # Clips a vertical road-marking line to a visible region.
    #
    # When used:
    # Prevents road divider lines from entering the railway area.
    #
    # Real-world use:
    # Similar clipping is used in maps, games and rendering systems
    # to display only the visible part of graphical objects.
 
    clipped_y1 = max(y1, min_y)
    clipped_y2 = min(y2, max_y)
 
    # The complete line is outside the visible region.
    if clipped_y1 >= clipped_y2:
        return None
 
    return clipped_y1, clipped_y2
 
 
def draw_clipped_road_line(x, y1, y2):
    # Railway occupies approximately y = 395 to 505.
    # Road markings should not appear over the railway track.
 
    railway_bottom = 395
    railway_top = 505
 
    # Part below the railway crossing.
    bottom_part = clip_vertical_line(
        y1,
        y2,
        0,
        railway_bottom
    )
 
    if bottom_part is not None:
 
        clipped_y1, clipped_y2 = bottom_part
 
        draw_line(
            x,
            clipped_y1,
            x,
            clipped_y2,
            3
        )
 
    # Part above the railway crossing.
    top_part = clip_vertical_line(
        y1,
        y2,
        railway_top,
        600
    )
 
    if top_part is not None:
 
        clipped_y1, clipped_y2 = top_part
 
        draw_line(
            x,
            clipped_y1,
            x,
            clipped_y2,
            3
        )
 
 
# ============================================================
# ROAD
# ============================================================
 
def draw_road():
    # Draw the main vertical road.
 
    draw_rectangle(
        330, 0,
        470, 600,
        0.25, 0.25, 0.25
    )
 
    # Draw road divider using line clipping.
 
    glColor3f(
        1.0,
        1.0,
        1.0
    )
 
    for y in range(0, 600, 60):
 
        draw_clipped_road_line(
            400,
            y,
            y + 30
        )
 
    # Draw the stop line before the railway crossing.
 
    draw_rectangle(
        335, 295,
        465, 302,
        1.0, 1.0, 1.0
    )
 
 
# ============================================================
# RAILWAY TRACK
# ============================================================
 
def draw_railway():
    # Draw railway ground.
 
    draw_rectangle(
        0, 395,
        800, 505,
        0.45, 0.30, 0.15
    )
 
    # Draw railway sleepers.
 
    glColor3f(
        0.25,
        0.15,
        0.08
    )
 
    for x in range(0, 801, 40):
 
        draw_line(
            x, 405,
            x, 495,
            5
        )
 
    # Draw railway rails.
 
    glColor3f(
        0.15,
        0.15,
        0.15
    )
 
    draw_line(
        0, 420,
        800, 420,
        6
    )
 
    draw_line(
        0, 480,
        800, 480,
        6
    )
 
 
# ============================================================
# RAILWAY GATE
# ============================================================
 
def draw_gate():
    # Draw gate support.
 
    draw_rectangle(
        285, 320,
        310, 400,
        0.25, 0.25, 0.25
    )
 
    pivot_x = 300
    pivot_y = 390
 
    glPushMatrix()
 
    # Move the local origin to the gate pivot.
    # This is a 2D translation operation.
 
    glTranslatef(
        pivot_x,
        pivot_y,
        0
    )
 
    # Rotate the gate around its pivot.
    # This is a 2D rotation operation.
 
    glRotatef(
        gate_angle,
        0,
        0,
        1
    )
 
    # Draw gate barrier.
 
    draw_rectangle(
        0, -10,
        150, 10,
        0.90, 0.10, 0.10
    )
 
    # Draw white stripes.
 
    for x in range(20, 140, 40):
 
        draw_rectangle(
            x, -10,
            x + 15, 10,
            1.0, 1.0, 1.0
        )
 
    glPopMatrix()
 
    # Draw pivot.
 
    draw_circle(
        pivot_x,
        pivot_y,
        8,
        0.10, 0.10, 0.10
    )
 
 
# ============================================================
# TRAFFIC SIGNAL
# ============================================================
 
def draw_signal():
    # Draw signal pole.
 
    draw_rectangle(
        490, 270,
        500, 360,
        0.15, 0.15, 0.15
    )
 
    # Draw signal box.
 
    draw_rectangle(
        470, 350,
        520, 430,
        0.08, 0.08, 0.08
    )
 
    # Color Fill is used to represent signal states.
 
    if signal_red:
 
        # Red ON.
 
        draw_circle(
            495, 405,
            12,
            1.0, 0.0, 0.0
        )
 
        # Green OFF.
 
        draw_circle(
            495, 375,
            12,
            0.0, 0.20, 0.0
        )
 
    else:
 
        # Red OFF.
 
        draw_circle(
            495, 405,
            12,
            0.20, 0.0, 0.0
        )
 
        # Green ON.
 
        draw_circle(
            495, 375,
            12,
            0.0, 1.0, 0.0
        )
 
 
# ============================================================
# TRAIN
# ============================================================
 
def draw_train():
    # The entire train moves using 2D translation.
 
    glPushMatrix()
 
    glTranslatef(
        train_x,
        0,
        0
    )
 
    # Engine body.
 
    draw_rectangle(
        0, 425,
        150, 475,
        0.10, 0.35, 0.75
    )
 
    # Engine front.
 
    draw_rectangle(
        120, 440,
        175, 475,
        0.10, 0.35, 0.75
    )
 
    # Driver window.
 
    draw_rectangle(
        100, 445,
        125, 468,
        0.70, 0.90, 1.0
    )
 
    # Coach.
 
    draw_rectangle(
        -130, 425,
        -10, 475,
        0.75, 0.15, 0.10
    )
 
    # Coach windows.
 
    draw_rectangle(
        -110, 445,
        -85, 465,
        0.70, 0.90, 1.0
    )
 
    draw_rectangle(
        -65, 445,
        -40, 465,
        0.70, 0.90, 1.0
    )
 
    # Connector.
 
    draw_rectangle(
        -15, 442,
        5, 455,
        0.10, 0.10, 0.10
    )
 
    glPopMatrix()
 
 
# ============================================================
# CAR
# ============================================================
 
def draw_car():
    # What it does: Draws a top-view car.
    # When used: Used to simulate road traffic.
    # Real-world use: Traffic and transportation simulations.
 
    glPushMatrix()
 
    # Move the entire car vertically using 2D translation.
 
    glTranslatef(
        0,
        car_y,
        0
    )
 
    # Car body.
 
    draw_rectangle(
        355, 0,
        395, 80,
        0.95, 0.75, 0.05
    )
 
    # Window area.
 
    draw_rectangle(
        360, 20,
        390, 60,
        0.10, 0.35, 0.55
    )
 
    # Front windshield.
 
    draw_rectangle(
        362, 52,
        388, 65,
        0.65, 0.90, 1.0
    )
 
    # Rear windshield.
 
    draw_rectangle(
        362, 15,
        388, 28,
        0.65, 0.90, 1.0
    )
 
    # Wheels.
 
    draw_rectangle(
        350, 12,
        357, 30,
        0.05, 0.05, 0.05
    )
 
    draw_rectangle(
        350, 55,
        357, 73,
        0.05, 0.05, 0.05
    )
 
    draw_rectangle(
        393, 12,
        400, 30,
        0.05, 0.05, 0.05
    )
 
    draw_rectangle(
        393, 55,
        400, 73,
        0.05, 0.05, 0.05
    )
 
    glPopMatrix()
 
 
# ============================================================
# INFORMATION PANEL
# ============================================================
 
def draw_information():
    # Draw project title.
 
    draw_text(
        20,
        575,
        "Railway Crossing Safety Simulation",
        0.05,
        0.05,
        0.05
    )
 
    # Draw current system status.
 
    if signal_red:
 
        draw_text(
            20,
            550,
            "Status: TRAIN APPROACHING - STOP",
            0.80,
            0.0,
            0.0
        )
 
    else:
 
        draw_text(
            20,
            550,
            "Status: SAFE - GO",
            0.0,
            0.35,
            0.0
        )
 
    # Draw controls.
 
    draw_text(
        560,
        575,
        "SPACE: Pause/Resume",
        0.05,
        0.05,
        0.05
    )
 
    draw_text(
        560,
        555,
        "+/-: Train Speed",
        0.05,
        0.05,
        0.05
    )
 
    draw_text(
        560,
        535,
        "R: Reset   ESC: Exit",
        0.05,
        0.05,
        0.05
    )
 
    if paused:
 
        draw_text(
            370,
            570,
            "PAUSED",
            0.80,
            0.0,
            0.0
        )
 
 
# ============================================================
# AUTOMATIC SAFETY SYSTEM
# ============================================================
 
def update_safety_system():
    # What it does:
    # Detects whether the train is approaching the crossing.
    #
    # When used:
    # Controls the traffic signal and railway gate.
    #
    # Real-world use:
    # Automatic railway crossing control systems.
 
    global gate_angle
    global signal_red
 
    # Train detection zone.
 
    if 100 <= train_x <= 650:
 
        signal_red = True
 
        # Close gate gradually.
 
        if gate_angle > 0:
 
            gate_angle -= gate_speed
 
            if gate_angle < 0:
                gate_angle = 0
 
    else:
 
        signal_red = False
 
        # Open gate gradually.
 
        if gate_angle < 90:
 
            gate_angle += gate_speed
 
            if gate_angle > 90:
                gate_angle = 90
 
 
# ============================================================
# CAR MOVEMENT SYSTEM
# ============================================================
 
def update_car():
    # Controls car movement based on the traffic signal.
 
    global car_y
 
    car_front = car_y + 80
 
    stop_position = 290
 
    # --------------------------------------------------------
    # RED SIGNAL
    # --------------------------------------------------------
 
    if signal_red:
 
        # Move until the car reaches the stop line.
 
        if car_front < stop_position:
 
            car_y += car_speed
 
            # Prevent crossing the stop line.
 
            if car_y + 80 > stop_position:
 
                car_y = stop_position - 80
 
        # If the car already passed the railway,
        # allow it to continue moving.
 
        elif car_y > 510:
 
            car_y += car_speed
 
        # Otherwise the car stays stopped.
 
    # --------------------------------------------------------
    # GREEN SIGNAL
    # --------------------------------------------------------
 
    else:
 
        car_y += car_speed
 
    # Reset car after leaving the screen.
 
    if car_y > 650:
 
        car_y = -100
 
 
# ============================================================
# RESET SIMULATION
# ============================================================
 
def reset_simulation():
    # Restores the initial simulation state.
 
    global train_x
    global train_speed
    global car_y
    global gate_angle
    global signal_red
    global paused
 
    train_x = -250.0
    train_speed = 2.0
 
    car_y = -100.0
 
    gate_angle = 90.0
 
    signal_red = False
 
    paused = False
 
 
# ============================================================
# KEYBOARD CONTROLS
# ============================================================
 
def keyboard(key, x, y):
    # Handles keyboard interaction.
 
    global paused
    global train_speed
 
    # ESC = Exit.
 
    if key == b'\x1b':
 
        glutLeaveMainLoop()
 
    # SPACE = Pause / Resume.
 
    elif key == b' ':
 
        paused = not paused
 
    # + = Increase train speed.
 
    elif key == b'+' or key == b'=':
 
        train_speed += 0.5
 
        if train_speed > 8.0:
            train_speed = 8.0
 
    # - = Decrease train speed.
 
    elif key == b'-' or key == b'_':
 
        train_speed -= 0.5
 
        if train_speed < 0.5:
            train_speed = 0.5
 
    # R = Reset.
 
    elif key == b'r' or key == b'R':
 
        reset_simulation()
 
    glutPostRedisplay()
 
 
# ============================================================
# DISPLAY
# ============================================================
 
def display():
    # Clear the previous frame.
 
    glClear(
        GL_COLOR_BUFFER_BIT
    )
 
    glLoadIdentity()
 
    # Draw complete scene.
 
    draw_road()
    draw_car()
    draw_railway()
    draw_gate()
    draw_signal()
    draw_train()
    draw_information()
 
    # Display completed frame.
 
    glutSwapBuffers()
 
 
# ============================================================
# ANIMATION UPDATE
# ============================================================
 
def update(value):
    # Updates moving objects and safety logic.
 
    global train_x
 
    if not paused:
 
        # Move train.
 
        train_x += train_speed
 
        # Update gate and signal.
 
        update_safety_system()
 
        # Update car.
 
        update_car()
 
        # Reset train after leaving the screen.
 
        if train_x > 950:
 
            train_x = -250
 
    # Request next frame.
 
    glutPostRedisplay()
 
    # Approximately 60 FPS.
 
    glutTimerFunc(
        16,
        update,
        0
    )
 
 
# ============================================================
# OPENGL INITIALIZATION
# ============================================================
 
def init():
    # Set grass background color.
 
    glClearColor(
        0.55,
        0.80,
        0.45,
        1.0
    )
 
    # Set projection matrix.
 
    glMatrixMode(
        GL_PROJECTION
    )
 
    glLoadIdentity()
 
    # 2D coordinate system:
    # Bottom-left = (0, 0)
    # Top-right = (800, 600)
 
    gluOrtho2D(
        0,
        800,
        0,
        600
    )
 
    # Return to model-view matrix.
 
    glMatrixMode(
        GL_MODELVIEW
    )
 
    glLoadIdentity()
 
 
# ============================================================
# MAIN PROGRAM
# ============================================================
 
def main():
    # Initialize GLUT.
 
    glutInit(sys.argv)
 
    # Enable RGB color and double buffering.
 
    glutInitDisplayMode(
        GLUT_DOUBLE | GLUT_RGB
    )
 
    # Set window size.
 
    glutInitWindowSize(
        800,
        600
    )
 
    # Set initial window position.
 
    glutInitWindowPosition(
        100,
        100
    )
 
    # Create application window.
 
    glutCreateWindow(
        b"Railway Crossing Safety Simulation"
    )
 
    # Initialize OpenGL.
 
    init()
 
    # Register callbacks.
 
    glutDisplayFunc(
        display
    )
 
    glutKeyboardFunc(
        keyboard
    )
 
    # Start animation timer.
 
    glutTimerFunc(
        16,
        update,
        0
    )
 
    # Start GLUT event loop.
 
    glutMainLoop()
 
 
# ============================================================
# START PROGRAM
# ============================================================
 
if __name__ == "__main__":
    main()