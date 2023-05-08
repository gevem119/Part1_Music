#import statements
from machine import Pin, PWM
from utime import sleep
import rp2
import array,time
from rp2 import PIO, StateMachine, asm_pio
buzzer = PWM(Pin(18))
button = Pin(20, Pin.IN, Pin.PULL_UP)
button2 = Pin(21, Pin.IN, Pin.PULL_UP)

#premade with all the different notes for you to have a go with
tones = {
"B0": 31,
"C1": 33,
"CS1": 35,
"D1": 37,
"DS1": 39,
"E1": 41,
"F1": 44,
"FS1": 46,
"G1": 49,
"GS1": 52,
"A1": 55,
"AS1": 58,
"B1": 62,
"C2": 65,
"CS2": 69,
"D2": 73,
"DS2": 78,
"E2": 82,
"F2": 87,
"FS2": 93,
"G2": 98,
"GS2": 104,
"A2": 110,
"AS2": 117,
"B2": 123,
"C3": 131,
"CS3": 139,
"D3": 147,
"DS3": 156,
"E3": 165,
"F3": 175,
"FS3": 185,
"G3": 196,
"GS3": 208,
"A3": 220,
"AS3": 233,
"B3": 247,
"C4": 262,
"CS4": 277,
"D4": 294,
"DS4": 311,
"E4": 330,
"F4": 349,
"FS4": 370,
"G4": 392,
"GS4": 415,
"A4": 440,
"AS4": 466,
"B4": 494,
"C5": 523,
"CS5": 554,
"D5": 587,
"DS5": 622,
"E5": 659,
"F5": 698,
"FS5": 740,
"G5": 784,
"GS5": 831,
"A5": 880,
"AS5": 932,
"B5": 988,
"C6": 1047,
"CS6": 1109,
"D6": 1175,
"DS6": 1245,
"E6": 1319,
"F6": 1397,
"FS6": 1480,
"G6": 1568,
"GS6": 1661,
"A6": 1760,
"AS6": 1865,
"B6": 1976,
"C7": 2093,
"CS7": 2217,
"D7": 2349,
"DS7": 2489,
"E7": 2637,
"F7": 2794,
"FS7": 2960,
"G7": 3136,
"GS7": 3322,
"A7": 3520,
"AS7": 3729,
"B7": 3951,
"C8": 4186,
"CS8": 4435,
"D8": 4699,
"DS8": 4978
}

#pre-defined songs
song_1 = ["E5", "E5", "P", "E5", "P", "C5", "E5", "P", "G5", "P", "P", "P", "G4", "P", "P", "P"]
song_2 = ["D5","E5","G5","E5","B5","B5","P","B5","B5","P","A5","A5","P","D5","E5","G5","E5","A5","A5","P","A5","A5","A5","G5","P","P","P"]

#tempo of the songs to make pitch correct
tempo = 320

# Calculate the duration of each note (in seconds)
note_duration = 60 / tempo

#what happens on each tone
def playtone(frequency):
    
    #TODO: DEFINE BUZZER FOR EACH TONE

#silencing the buzzer
def bequiet():
    buzzer.duty_u16(0)

def playsong(mysong):
    
    #TODO: DEFINE A LOOP TO ITERATE THROUGH THE SONG AND PLAY EACH NOTE
    
    #REMEMBER P IS A PAUSE
    
    bequiet()

#getting all the buttons values, 1 is pressed 0 is released
def get_button():
    return not button.value()

def get_button2():
    return not button2.value()


#different function for each button
def button_press_function():
    playsong(song2)
    
def button2_press_function():
    playsong(song)
    
#to stop 
def button_released_function():
    bequiet()


#main function
while True:
  
  if get_button() == 1:
    button_press_function()
  elif get_button2() == 1:
    button2_press_function()
  else:
    button_released_function()
    