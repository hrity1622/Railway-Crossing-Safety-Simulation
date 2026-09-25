
# Railway Crossing Safety Simulation

## Computer Graphics Sessional Project

A real-time **Railway Crossing Safety Simulation** developed using **Python, PyOpenGL, and GLUT**.

The project demonstrates how Computer Graphics techniques can be applied to simulate a real-world railway crossing safety system. The simulation includes a moving train, railway gate, traffic signal, road, railway tracks, and a moving car.

When the train enters the detection zone, the system automatically activates the red signal and closes the railway gate. The approaching car stops before the railway crossing. When the train leaves the detection zone, the signal becomes green and the gate opens again.

---

## Project Features

* Moving train simulation
* Automatic railway gate control
* Automatic red/green traffic signal
* Moving car with stop-line detection
* Interactive pause/resume control
* Adjustable train speed
* Simulation reset option
* 2D graphical environment
* Real-time animation using GLUT timer

---

## Computer Graphics Techniques Used

This project implements four major Computer Graphics techniques:

### 1. Line & Shape Drawing

OpenGL primitives are used to draw:

* Road
* Railway tracks
* Train
* Car
* Railway gate
* Traffic signal
* Road markings

### 2. 2D Transformations

2D transformations are used for object movement and animation.

* Translation is used to move the train.
* Translation is used to move the car.
* Rotation is used to open and close the railway gate.

### 3. Color Fill

Different colors are used to represent objects and system states.

For example:

* Red signal → Train approaching / Stop
* Green signal → Safe / Go
* Different colors → Train, car, road, railway track and other objects

### 4. Line Clipping

Line clipping is used for the road divider.

The road marking is divided around the railway crossing so that it does not appear over the railway track.

---

## How the Safety System Works

The simulation continuously checks the position of the train.

```text
Train approaches
       ↓
Train enters detection zone
       ↓
Traffic signal becomes RED
       ↓
Railway gate starts closing
       ↓
Car stops before stop line
       ↓
Train leaves detection zone
       ↓
Traffic signal becomes GREEN
       ↓
Railway gate starts opening
       ↓
Car continues moving
```

---

## Controls

| Key     | Function                  |
| ------- | ------------------------- |
| `SPACE` | Pause / Resume simulation |
| `+`     | Increase train speed      |
| `-`     | Decrease train speed      |
| `R`     | Reset simulation          |
| `ESC`   | Exit application          |

---

## Technologies Used

* Python
* PyOpenGL
* GLUT
* OpenGL
* 2D Computer Graphics
* Real-time Animation

---

## Installation

### Step 1: Install Python

Make sure Python is installed on your computer.

Check using:

```bash
python --version
```

### Step 2: Install Required Libraries

Open a terminal inside the project folder and run:

```bash
pip install -r requirements.txt
```

Or install the packages directly:

```bash
pip install PyOpenGL PyOpenGL_accelerate
```

---

## How to Run

Run the following command:

```bash
python railway_crossing.py
```

The OpenGL window will open and the railway crossing simulation will start automatically.

---

## Project Structure

```text
Railway-Crossing-Safety-Simulation/
│
├── railway_crossing.py
├── requirements.txt
└── README.md
```

---

## Project Objective

The main objective of this project is to demonstrate the practical application of Computer Graphics concepts in a real-world transportation safety scenario.

The project combines graphical object drawing, 2D transformations, color representation, line clipping, animation, keyboard interaction, and simple automatic control logic into one interactive simulation.

---

## Future Improvements

If more development time were available, the following features could be added:

* Multiple cars
* More realistic train coaches
* Train horn and railway warning sounds
* Warning lights before gate closure
* Pedestrian movement
* More realistic railway crossing environment
* Improved vehicle and train animations
* Additional user controls

---

## Author

**Samia Tabassum Hrity**

**Department of Computer Science & Engineering**
**Leading University, Sylhet**

**Computer Graphics Sessional**

---

## Academic Project

This project was developed as part of the **Computer Graphics Sessional Project**.

The implementation demonstrates practical use of Computer Graphics concepts through an interactive Python OpenGL simulation.

