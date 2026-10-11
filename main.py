import board


from kmk.kmk.kmk_keyboard import KMKKeyboard
from kmk.kmk.keys import KC
from kmk.kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP15, board.GP14, board.GP13, board.GP12, board.GP11, board.GP10, board.GP9, board.GP8, board.GP7, board.GP6, board.GP5, board.GP4, board.GP3, board.GP2, board.GP1, board.GP0)
keyboard.row_pins = (board.GP26, board.GP22, board.GP21, board.GP20, board.GP19, board.GP18)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
        KC.ESC, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.PSCREEN, KC.INSERT, KC.DELETE,
        KC.GRAVE, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINUS, KC.EQUAL, KC.BSPACE, KC.HOME, KC.NO,
        KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRACKET, KC.RBRACKET, KC.BSLASH, KC.PGUP, KC.NO, 
        KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCOLON, KC.QUOTE, KC.ENTER, KC.PGDOWN, KC.NO, KC.NO,
        KC.LSHIFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMMA, KC.DOT, KC.SLASH, KC.RSHIFT, KC.UP, KC.END, KC.NO, KC.NO,
        KC.LCTRL, KC.LGUI, KC.LALT, KC.SPACE, KC.RALT, KC.NO, KC.RCTL, KC.LEFT, KC.DOWN, KC.RIGHT, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,


        KC.NUM, KC.KP_SLASH, KC.KP_ASTERISK, KC.KP_MINUS, 
        KC.KP_7, KC.KP_8, KC.KP_9, KC.KP_PLUS, 
        KC.KP_4, KC.KP_5, KC.KP_6, KC.NO,
        KC.KP_1, KC.KP_2, KC.KP_3, KC.KP_ENTER,
        KC.KP_0, KC.NO, KC.KP_DOT, KC.NO
    ]

]

if __name__ == "__main__":
    keyboard.go()
