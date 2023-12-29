import sys
import time

def generate_beep_sound(beeps_per_second):
    if sys.platform.startswith('win'):
        import winsound
        duration = int(1000 / beeps_per_second) # Calculate duration in milliseconds
        frequency = 440 # Default frequency for beep sound
        winsound.Beep(frequency, duration)
    elif sys.platform.startswith('darwin'):
        duration = 1 / beeps_per_second # Calculate duration in seconds
        for _ in range(beeps_per_second):
            print('\a', end='', flush=True) # Print ASCII bell character to produce beep sound
            time.sleep(duration)
    else:
        print("Beep sound not supported on this platform.")

# Example usage
generate_beep_sound(2) # Generates 2 beeps per second