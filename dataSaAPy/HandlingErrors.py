'''
Created on Jul 6, 2024

@author: shadowmons
'''

def main():
    lecture()
    lecture2()
    readingText()
    try:
        water_left(5, 100, 2)
    except RuntimeError as err:
        print('alert_navigation_system',err)
    
def lecture():
    try:
        configuration = open('config.txt')
        print(configuration)
        #handle multiple exceptions to give the proper feedback
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")
        #When errors are of a similar nature and there's no need to handle them 
        #individually, you can group the exceptions together as one by using parentheses
    except (BlockingIOError, TimeoutError):
        print("Filesystem under heavy load, can't complete reading configuration file")
        #

    
def lecture2():
    try:
        open("mars.jpg")
        #to access the error that's associated with the exception, include the as keyword. 
        #Useful when an exception is too generic and the error message can be useful:
    except FileNotFoundError as err:
        print("Got a problem trying to read the file:", err)
    
    #sometimes it's necessary to use less readable code to offer a better user experience when an error happens.

def readingText():
    loaded_config = """# Rocket Ship Configuration File!
    fuel_tanks=4
    oxygen_tanks=3
    initial_propulsion_level=84
    $ End of file"""
    parsed_config = {}
    for line in loaded_config.split('\n'):
        try:
            key,value = line.split('=')
            parsed_config[key] = value
        except ValueError:
            print(f'Unable to parse: {line}')
    print(parsed_config)
    
    
def water_left(astronauts, water_left, days_left):
    #The error from TypeError is not very friendly in the context of what the function expects. 
    #updated to prevent passing unsupported types
    for argument in [astronauts, water_left, days_left]:
        try:
            # If argument is an int, the following operation will work
            argument / 10
        except TypeError:
            # TypeError will be raised only if it isn't the right type 
            # Raise the same exception but with a better error message
            raise TypeError(f"All arguments must be of type int, but received: '{argument}'")
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    #Raise exceptions
    #it's useful to raise exceptions that let other code realize what the problem is.
    if total_water_left < 0:
        raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
    return f"Total water left after {days_left} days is: {total_water_left} liters"

    
if __name__ == '__main__':
    main()
