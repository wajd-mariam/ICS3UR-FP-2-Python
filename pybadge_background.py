#!/usr/bin/env python3

# Created by: Wajd Mariam
# Created on: Sep 2019
# This program changes the background of the Pybadge

import ugame
import stage

# an image bank of CircuitPython
image_bank_1 = stage.Bank.from_bmp16("ball.bmp")

def main():

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_1, 10, 8)
    # changing 0,0 iamge to the 3rd image
    background.tile(4 ,3 , 3)
   
    # setting up the background to show up on the PyPadge
    # setting up the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    game.layers = [background]
   
   
    game.render_block()
   
    while True:
        # comment
        pass
       
if __name__ == "__main__":
    main()