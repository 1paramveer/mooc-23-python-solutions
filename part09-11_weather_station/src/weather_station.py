# WRITE YOUR SOLUTION HERE:

class WeatherStation:
    def __init__(self, name: str):
        self.__nameStation = name
        self.__listobs = []

    def add_observation(self,observation: str):
        self.__listobs.append(observation)

    def latest_observation(self):
        if len(self.__listobs) > 0:
            return self.__listobs[-1]
        return ""

    def number_of_observations(self):
        return len(self.__listobs)
    
    def __str__(self):
        return f"{self.__nameStation}, {self.number_of_observations()} observations"
