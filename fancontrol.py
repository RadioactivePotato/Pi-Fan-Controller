from gpiozero import OutputDevice
import time

# Set the GPIO pin for the fan
FAN_PIN = 27
FAN_ON_DURATION = 120  # how long to turn fan on for (in seconds)
TEMP_THRESHOLD = 50.0  # temperature required to turn fan on in Celsius

fan = OutputDevice(FAN_PIN)

def get_cpu_temperature():
    """Read the CPU temperature from the system."""
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
        temp = f.read()
    return int(temp) / 1000  # convert from millidegree to celsius

def control_fan():
    try:
        while True:
            cpu_temp = get_cpu_temperature()

            if cpu_temp >= TEMP_THRESHOLD:
                fan.on()  # turn the fan on
                time.sleep(FAN_ON_DURATION)
                fan.off()  # turn the fan off

            time.sleep(10)  # check temps every 10s

    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    control_fan()
