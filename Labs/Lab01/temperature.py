def convert_to_f(celcius):
    return (celcius * 9 / 5) + 32

celcius = 10
fahrenheit = convert_to_f(celcius)

print("{} degrees celcius == {} degrees fahrenheit".format(celcius, fahrenheit))