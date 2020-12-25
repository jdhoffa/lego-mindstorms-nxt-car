from flask import Flask, render_template
import nxt.locator
from nxt.motor import *
import time

honk = [698.46, 622.25, 587.33, 523.25, 466.16]
sequence = [1, 3, 5, 5, 5, 4, 3, 2, 1, 1, 1, 3]
duration = [1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2]


b = nxt.locator.find_one_brick()
m_drive = Motor(b, PORT_B)
m_turn = Motor(b, PORT_A)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/forward')
def go_forward():
    m_drive.turn(50, 360)

@app.route('/back')
def go_backward():
    m_drive.turn(-50, 360)

@app.route('/left')
def go_left():
    m_turn.turn(50, 180)

@app.route('/right')
def go_right():
    m_turn.turn(-50, 180)

@app.route('/honk')
def bleep_bloop():
    for note, length in zip(sequence, duration):
      b.play_tone_and_wait(honk[note-1], 100*length)
      time.sleep(0.05)

