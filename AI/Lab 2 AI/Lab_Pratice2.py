class SmartAC:
    def __init__(self, ideal_temp=25, start_temp=24):
        self.ideal = ideal_temp
        self.temperature = start_temp

    def act(self):
        if self.temperature < self.ideal - 3:
            return "Turn Heater ON"
        elif self.temperature > self.ideal + 3:
            return "Turn Cooler ON"
        else:
            return "Do Nothing"

    def update_environment(self, action):
        if action == "Turn Heater ON":
            self.temperature += 2
        elif action == "Turn Cooler ON":
            self.temperature -= 2

    def run(self, steps=5):
        print("Starting Smart AC Simulation")
        for i in range(1, steps + 1):
            print(f"Step {i}:")
            action = self.act()
            print(f"  Current Temp: {self.temperature}°C → Action: {action}")
            self.update_environment(action)
            print(f"  New Temp: {self.temperature}°C\n")


ac = SmartAC(ideal_temp=25, start_temp=10)
ac.run(steps=5)