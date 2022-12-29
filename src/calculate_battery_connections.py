from colorama import Fore, Back, Style


class CalculateBatteryConnections:
    def __init__(
        self,
        length: int,
        width: int,
        mA_cm2: int,
        voltage_per_cell: float,
        number_of_cells: int,
    ):
        """This program calculates the total power of a battery pack based on the number of cells in series or parallel.

        Parameters
        ----------
        - length: int
            - length of the battery pack in cm
        - width: int
            - width of the battery pack in cm
        - mA_cm2: int
            - current density in mA/cm2
        - voltage_per_cell: int
            - voltage per cell in V
        - number_of_cells: int
            - number of cells in the battery pack
        """
        self.length = length
        self.width = width
        self.mA_cm2 = mA_cm2
        self.voltage_per_cell = voltage_per_cell
        self.number_of_cells = number_of_cells

    def __calculate_area(self):
        area = self.length * self.width
        print(Fore.GREEN + f"Area of the battery pack is {area} cm2")
        return area

    def __calculate_cell_amps(self, area: int):
        total_power = area * self.mA_cm2
        total_power /= 1000
        print(Fore.GREEN + f"Total Amps per cell is {total_power} A")
        return total_power

    def __calculate_series(self, amps: int):
        series_voltage = self.voltage_per_cell * self.number_of_cells
        series_power = amps * series_voltage
        print(Fore.GREEN + f"Total voltage of the battery pack is {series_voltage} V")
        print(Fore.GREEN + f"Total Amps of the battery pack is {amps} A")
        return series_power

    def __calculate_parallel(self, amps: int):
        parallel_capacity = amps * self.number_of_cells
        parallel_power = parallel_capacity * self.voltage_per_cell
        print(
            Fore.GREEN
            + f"Total voltage of the battery pack is {self.voltage_per_cell} V"
        )
        print(Fore.GREEN + f"Total Amps of the battery pack is {parallel_capacity} A")
        return parallel_power

    # create a function to calculate the total power of the battery pack using the series and parallel functions based on the number of cells
    def __calculate_total_power(self, parallel: bool):
        area: int = self.__calculate_area()
        amps: int = self.__calculate_cell_amps(area)

        return (
            self.__calculate_parallel(amps)
            if parallel
            else self.__calculate_series(amps)
        )

    def display(self, parallel: bool):
        total_power = self.__calculate_total_power(parallel)
        if total_power > 1000:
            total_power /= 1000
            print(f"Total power of the battery pack is {total_power} kW")
            return
        print(f"Total power of the battery pack is {total_power} W")


def handle_input(args):
    for key, value in args.items():
        if not key:
            return False
        print(Fore.YELLOW + value)
        print(Fore.BLUE + "")
        if key == "parallel":
            input_values["parallel"]: True if input() == "p" else False
        elif key == "voltage_per_cell":
            input_values[key] = float(input())
        else:
            input_values[key] = int(input())
    return True


# create a dictionary to store the input messages
input_messages = {
    "length": "Enter the length of the battery pack in cm: ",
    "width": "Enter the width of the battery pack in cm: ",
    "mA_cm2": "Enter the current density per cm2 of a single cell (mA/cm2): ",
    "voltage_per_cell": "Enter the voltage for a single cell: ",
    "number_of_cells": "Enter the total number of cells: ",
    "parallel": "Are the cells in series or parallel? (s/p): ",
}

input_values = {
    "length": 0,
    "width": 0,
    "mA_cm2": 0,
    "voltage_per_cell": 0.0,
    "number_of_cells": 0,
    "parallel": False,
}

if __name__ == "__main__":
    print(Fore.RED + "Battery Pack Calculator")
    print(
        Fore.BLUE
        + "This program calculates the total power of a battery pack based on the number of cells in series or parallel."
    )

    handle_input(input_messages)
    battery = CalculateBatteryConnections(
        input_values["length"],
        input_values["width"],
        input_values["mA_cm2"],
        input_values["voltage_per_cell"],
        input_values["number_of_cells"],
    )
    battery.display(input_values["parallel"])
