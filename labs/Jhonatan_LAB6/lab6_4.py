# lab6_4.py – Jhonatan Parada

err_msg = 'Invalid search letter'
# invalid error: space characters, and no characters 

vehicles = [
    'car',
    'Truck',
    'boat',
    'PLANE'
]
print(f"Vehicles = {vehicles}")

srch_lttr = input('Enter a search letter: ')

if not srch_lttr or len(srch_lttr) > 1:
    print(err_msg)
else:
    for vehicle in vehicles:
        if not (srch_lttr.lower() in vehicle.lower()):
            print(f"{vehicle} does not contain '{srch_lttr}'.")
        else:
            print(
                f"{vehicle} contains '{srch_lttr}'",
                f"and it is in position {vehicles.index(vehicle)}.",
                sep=' '
            )