class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32


# Create a new objects
human = Celsius(34)

print(human.temperature)

# Get the to_fahrenheit method
print(human.to_fahrenheit())