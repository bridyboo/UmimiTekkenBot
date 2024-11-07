from inputs import get_gamepad
import math
import threading
import time

class XboxController(object):
    MAX_TRIG_VAL = math.pow(2, 8)
    MAX_JOY_VAL = math.pow(2, 15)

    def __init__(self):

        self.LeftJoystickY = 0
        self.LeftJoystickX = 0
        self.RightJoystickY = 0
        self.RightJoystickX = 0
        self.LeftTrigger = 0
        self.RightTrigger = 0
        self.LeftBumper = 0
        self.RightBumper = 0
        self.A = 0
        self.X = 0
        self.Y = 0
        self.B = 0
        self.LeftThumb = 0
        self.RightThumb = 0
        self.Back = 0
        self.Start = 0
        self.LeftDPad = 0
        self.RightDPad = 0
        self.UpDPad = 0
        self.DownDPad = 0

        self._monitor_thread = threading.Thread(target=self._monitor_controller, args=())
        self._monitor_thread.daemon = True
        self._monitor_thread.start()


    def read(self):
        back = self.LeftDPad
        forward = self.RightDPad
        up = self.UpDPad
        down = self.DownDPad
        one = self.X
        two = self.Y
        three = self.A
        four = self.B
        RT = self.RightTrigger
        RB = self.RightBumper
        return [back, forward, up, down, one, two, three, four, RT, RB]


    def _monitor_controller(self):
        while True:
            events = get_gamepad()
            for event in events:
                if event.code == 'ABS_Y':
                    self.LeftJoystickY = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_X':
                    self.LeftJoystickX = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_RY':
                    self.RightJoystickY = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_RX':
                    self.RightJoystickX = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_Z':
                    self.LeftTrigger = event.state / XboxController.MAX_TRIG_VAL # normalize between 0 and 1
                elif event.code == 'ABS_RZ':
                    self.RightTrigger = math.ceil(event.state/XboxController.MAX_TRIG_VAL)
                elif event.code == 'BTN_TL':
                    self.LeftBumper = event.state
                elif event.code == 'BTN_TR':
                    self.RightBumper = event.state
                elif event.code == 'BTN_SOUTH':
                    self.A = event.state
                elif event.code == 'BTN_WEST':
                    self.X = event.state
                elif event.code == 'BTN_NORTH':
                    self.Y = event.state
                elif event.code == 'BTN_EAST':
                    self.B = event.state
                elif event.code == 'BTN_THUMBL':
                    self.LeftThumb = event.state
                elif event.code == 'BTN_THUMBR':
                    self.RightThumb = event.state
                elif event.code == 'BTN_SELECT':
                    self.Back = event.state
                elif event.code == 'BTN_START':
                    self.Start = event.state
                elif event.code == 'ABS_HAT0X': # this should be correct now (i think)
                    if event.state == 1:
                        self.RightDPad = event.state
                    elif event.state == -1:
                        event.state = 1
                        self.LeftDPad = event.state
                    else:
                        self.RightDPad, self.LeftDPad = 0, 0
                elif event.code == 'ABS_HAT0Y':  #SOCD is still not perfect, when down is help and press up it's not returning 1 for up
                    event.state = event.state * -1
                    if event.state == 1:
                        self.UpDPad = event.state
                    elif event.state == -1:
                        self.DownDPad = 1
                    else:
                        self.UpDPad, self.DownDPad = 0, 0




# [0    1          2    3   4     5    6     7     8    9]
# [back, forward, up, down, one, two, three, four, RT, RB]
def main():
    controller = XboxController()

    try:
        while True:
            input_values = controller.read()
            if any (input_values):
                print(input_values)
                print (f"back: {input_values[0]}, forward: {input_values[1]},up:{input_values[2]}, down:{input_values[3]},one:{input_values[4]}, "
                    f"two: {input_values[5]},three: {input_values[6]}, four: {input_values[7]}, RT: {input_values[8]}, RB: {input_values[9]}")
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Exiting program.")

if __name__ == "__main__":
    main()
