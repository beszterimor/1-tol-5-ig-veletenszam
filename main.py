def on_button_pressed_a():
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    basic.show_number(randint(1, 5))
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
