
print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.rgb import RGB
from kmk.modules.layers import Layers


keyboard = KMKKeyboard()

keyboard.col_pins = (
    board.GP0,board.GP1, board.GP2, board.GP3, board.GP4,
    board.GP5,board.GP6, board.GP7, board.GP8, board.GP9,
    board.GP10,board.GP11, board.GP12, board.GP13, board.GP14
    
)

keyboard.row_pins = (
    board.GP16,board.GP17, board.GP18, board.GP19, board.GP20
    )   


keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.modules.append(Layers())

_______ = KC.TRNS   
XXXXXXX = KC.NO     
FN = KC.MO(1)       




keyboard.keymap = [ 
    [ # LAYER 0:QWERTY
    KC.ESC,    KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,    KC.N6,    KC.N7,    KC.N8,    KC.N9,    KC.N0,     KC.MINUS,  KC.EQUAL, KC.BSLS,   KC.GRV,
    KC.PGUP, KC.TAB,    KC.Q,     KC.W,     KC.E,     KC.R,     KC.T,     KC.Y,     KC.U,     KC.I,     KC.O,     KC.P,      KC.LBRC,   KC.RBRC,  KC.BSPC,
    KC.PGDN, KC.CAPS,   KC.A,     KC.S,     KC.D,     KC.F,     KC.G,     KC.H,     KC.J,     KC.K,     KC.L,     KC.SCLN,   KC.QUOT,   KC.ENT,   KC.DEL,
    XXXXXXX, KC.LSFT,   KC.Z,     KC.X,     KC.C,     KC.V,     KC.B,     KC.N,     KC.M,     KC.COMM,  KC.DOT,   KC.SLSH,   KC.RSFT,   KC.UP,    FN,
    XXXXXXX, KC.LCTL,   XXXXXXX,  KC.LGUI,  XXXXXXX,  KC.LALT,  KC.SPC,   KC.SPC,   XXXXXXX,  XXXXXXX,  KC.RALT,  XXXXXXX,   XXXXXXX,   XXXXXXX,  KC.RCTL,
],

[  # LAYER 1: LAYER 1: F-keys and RGB controls (hold FN)
        _______, _______, KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,  KC.F12,  KC.DEL,
        _______, _______, KC.RGB_TOG, KC.RGB_MODE_RAINBOW, KC.RGB_HUI, KC.RGB_HUD, KC.RGB_SAI, KC.RGB_SAD, KC.RGB_VAI, KC.RGB_VAD, _______, _______, _______, _______, _______,
        _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,
        XXXXXXX, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, KC.PGUP, _______,
        XXXXXXX, _______, XXXXXXX, _______, XXXXXXX, _______, _______, _______, XXXXXXX, XXXXXXX, _______, XXXXXXX, XXXXXXX, XXXXXXX, _______,
],

]

rgb = RGB(
    pixel_pin=board.GP15,
    num_pixels=66,
    val_limit=100,     
    val_default=40,
    hue_default=0,
    sat_default=255,
)
keyboard.extensions.append(rgb)



if __name__ == '__main__':
    keyboard.go()   


