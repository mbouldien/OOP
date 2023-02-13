import InsectClass as c

def main():

    mosquito = c.Insect('mosquito', 2, 4)
    housefly = c.Insect('housefly',2,4)

    mosquito.calculate_flight()
    housefly.calculate_flight()

    print('The', mosquito.get_name(), 'can fly', mosquito.get_flight_miles(), 'miles')
    print('The', housefly.get_name(), 'can fly', housefly.get_flight_miles(), 'miles')


main()