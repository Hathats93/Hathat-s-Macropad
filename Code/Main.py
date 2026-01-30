import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.handlers.sequences import send_string, simple_key_sequence
from kmk.modules.encoder import EncoderHandler
from kmk.layers import Layers

keyboard = KMKKeyboard()

# --------------------
# MATRIX (PCB MATCHED)
# --------------------
# Columns: c1=GP26, c2=GP27, c3=GP28
keyboard.col_pins = (board.GP26, board.GP27, board.GP28)

# Rows: r1=GP1, r2=GP2, r3=GP4, r4=GP3
keyboard.row_pins = (board.GP1, board.GP2, board.GP4, board.GP3)

keyboard.diode_orientation = keyboard.DIODE_COL2ROW

# --------------------
# MODULES
# --------------------
layers = Layers()
keyboard.modules.append(layers)

encoder = EncoderHandler()
keyboard.modules.append(encoder)

# Encoder pins: (A, B, None)
# Push button is wired into the matrix, not here
encoder.pins = ((board.GP7, board.GP6, None),)

# Encoder rotation: CCW = volume down, CW = volume up
encoder.map = [
    ((KC.VOLD, KC.VOLU),)
]

# --------------------
# CUSTOM MACROS (Windows)
# --------------------
def open_app(path):
    """Launch a Windows app or URL using Win + R."""
    return simple_key_sequence([
        KC.LGUI(KC.R),
        0.2,
        send_string(path + '\n'),
    ])

SCREENSHOT = KC.LGUI(KC.LSFT(KC.S))

MODRINTH = open_app("C:/Users/manuy/AppData/Local/Modrinth App/Modrinth App.exe")
AFTERBURNER = open_app("C:/Program Files (x86)/MSI Afterburner/MSIAfterburner.exe")
YTMUSIC = open_app("https://music.youtube.com/playlist?list=PLo6qklPTwjaYW88PUh1sFuyacack23Zj_")
YOUTUBE = open_app("https://www.youtube.com")
CHROME = open_app("C:/Program Files/Google/Chrome/Application/chrome.exe")

# Windows Action Center (Bluetooth, Wi-Fi, etc.)
BLUETOOTH = KC.LGUI(KC.A)

# --------------------
# KEYMAP (4 × 3, Single Layer)
# --------------------
keyboard.keymap = [
    [
        KC.MPRV,    KC.MNXT,    KC.MUTE,      # R1 (encoder push = MUTE)
        CHROME,     KC.COPY,    KC.PASTE,     # R2
        SCREENSHOT, MODRINTH,   AFTERBURNER,  # R3
        BLUETOOTH,  YOUTUBE,    YTMUSIC,      # R4
    ]
]

# --------------------
# START KEYBOARD
# --------------------
if __name__ == "__main__":
    keyboard.go()