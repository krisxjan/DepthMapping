import freenect
import time
import random
import signal

keep_running = True
last_time = 0
dev = freenect.open_device(freenect.init(), 0)

def body(dev):
    global last_time
    if not keep_running:
        raise freenect.Kill
    if time.time() - last_time < 3:
        return
    last_time = time.time()

    for i in range(0,6):
        led = i
        tilt = i*5
        time.sleep(3)
        freenect.set_led(dev, led)
        freenect.set_tilt_degs(dev, tilt )
        print('led[%d] tilt[%d] accel[%s]' % (led, tilt, freenect.get_accel(dev)))

def handler(signum, frame):
    """Sets up the kill handler, catches SIGINT"""
    global keep_running
    keep_running = False

print('Press Ctrl-C in terminal to stop')
signal.signal(signal.SIGINT, handler)

def main():
    body(dev)

if __name__ == "__main__":
    main()
