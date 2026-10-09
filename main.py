import board


from kmk.kmk.kmk_keyboard import KMKKeyboard
from kmk.kmk.keys import KC
from kmk.kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = ()
keyboard.row_pins = ()
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
        KC.ESC, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.PSCREEN, KC.INSERT, KC.DELETE,
        KC.GRAVE, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINUS, KC.EQUAL, KC.BSPACE, KC.HOME, KC.NO,
        KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRACKET, KC.RBRACKET, KC.BSLASH, KC.PGUP, KC.NO, 
        KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.K, KC.L

    ]
]

if __name__ == "__main__":
    keyboard.go()
