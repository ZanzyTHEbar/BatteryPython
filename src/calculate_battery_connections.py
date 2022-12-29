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
        print(f"Area of the battery pack is {area} cm2")
        return area

    def __calculate_cell_amps(self):
        total_power = self.__calculate_area() * self.mA_cm2
        total_power /= 1000
        print(f"Total power of the battery pack is {total_power} A")
        return total_power

    def __calculate_series(self):
        series_voltage = self.voltage_per_cell * self.number_of_cells
        series_power = self.__calculate_cell_amps() * series_voltage
        print(f"Total power of the battery pack is {series_power} W")
        return series_power

    def __calculate_parallel(self):
        parallel_capacity = self.__calculate_cell_amps() * self.number_of_cells
        parallel_power = parallel_capacity * self.voltage_per_cell
        print(f"Total power of the battery pack is {parallel_power} W")
        return parallel_power

    # create a function to calculate the total power of the battery pack using the series and parallel functions based on the number of cells
    def __calculate_total_power(self, parallel: bool):
        if parallel:
            total_power = self.__calculate_parallel()
        else:
            total_power = self.__calculate_series()
        return total_power

    def display(self, parallel: bool):
        total_power = self.__calculate_total_power(parallel)
        if total_power > 1000:
            total_power /= 1000
            print(f"Total power of the battery pack is {total_power} kW")
            return
        print(f"Total power of the battery pack is {total_power} W")


if __name__ == "__main__":
    battery = CalculateBatteryConnections(17, 8, 215, 1.25, 50)
    battery.display(True)
