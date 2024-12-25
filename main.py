import os
import time
from colorama import Fore, Style


def get_pi_temperature():
    """Reads the Raspberry Pi CPU temperature."""
    try:
        # Read the temperature from the file system
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
            temp_raw = f.read()
        # Convert millidegree Celsius to degree Celsius
        return int(temp_raw) / 1000
    except FileNotFoundError:
        print(f"{Fore.RED}Error: Unable to read temperature. Are you running this on a Raspberry Pi?{Style.RESET_ALL}")
        return None


def display_temperature(temp):
    """Displays the temperature with colors based on its value."""
    if temp < 50:
        color = Fore.GREEN
    elif 50 <= temp < 70:
        color = Fore.YELLOW
    else:
        color = Fore.RED

    print(f"{color}CPU Temperature: {temp:.2f}°C{Style.RESET_ALL}")


def main():
    while True:
        temp = get_pi_temperature()
        if temp is not None:
            # Clear the screen for better visibility
            os.system('clear' if os.name == 'posix' else 'cls')
            display_temperature(temp)
        time.sleep(5)


if __name__ == "__main__":
    main()
