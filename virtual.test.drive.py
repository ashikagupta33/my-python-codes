import time
import random

class VirtualCar:
    def __init__(self, car_name):
        self.car_name = car_name
        self.speed = 0
        self.engine_on = False
        self.distance = 0

    def start_engine(self):
        if not self.engine_on:
            print(f"Starting {self.car_name}'s engine...")
            self.engine_on = True
            time.sleep(1)
            print("Engine started.")
        else:
            print("Engine already running.")

    def accelerate(self):
        if self.engine_on:
            increment = random.randint(5, 15)
            self.speed += increment
            print(f"Accelerating... Speed is now {self.speed} km/h")
        else:
            print("Start the engine first.")

    def brake(self):
        if self.engine_on and self.speed > 0:
            decrement = random.randint(5, 10)
            self.speed -= decrement
            if self.speed < 0:
                self.speed = 0
            print(f"Braking... Speed is now {self.speed} km/h")
        else:
            print("Car is already stopped.")

    def turn(self, direction):
        if self.engine_on:
            print(f"Turning {direction}...")
            time.sleep(0.5)
        else:
            print("Car is not running.")

    def stop_engine(self):
        if self.engine_on:
            print("Stopping engine...")
            self.speed = 0
            self.engine_on = False
            print("Engine stopped.")
        else:
            print("Engine is already off.")

    def show_status(self):
        print(f"--- {self.car_name} STATUS ---")
        print(f"Engine: {'On' if self.engine_on else 'Off'}")
        print(f"Speed: {self.speed} km/h")
        print(f"Distance Travelled: {self.distance} km")
        print("--------------------------")

    def update_distance(self):
        if self.speed > 0:
            self.distance += self.speed / 60  # per minute
        

# --------- MAIN LOOP ----------
car = VirtualCar("Acko Sedan")

def main():
    print("🚗 Welcome to Acko Drive - Virtual Test Drive 🚗")
    print("Commands: start, accelerate, brake, turn left/right, status, stop, exit")
    
    while True:
        car.update_distance()
        cmd = input("Enter command: ").lower().strip()

        if cmd == "start":
            car.start_engine()
        elif cmd == "accelerate":
            car.accelerate()
        elif cmd == "brake":
            car.brake()
        elif cmd.startswith("turn"):
            direction = cmd.split()[-1]
            if direction in ["left", "right"]:
                car.turn(direction)
            else:
                print("Please specify 'turn left' or 'turn right'")
        elif cmd == "status":
            car.show_status()
        elif cmd == "stop":
            car.stop_engine()
        elif cmd == "exit":
            car.stop_engine()
            print("Thanks for driving with Acko Drive!")
            break
        else:
            print("Invalid command. Try again.")

        time.sleep(1)

if __name__ == "__main__":
    main()
