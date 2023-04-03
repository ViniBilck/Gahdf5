import numpy as np
import unsio.input as uns_in


class Gahdf5:
    """"
    Instance the data of a Gadget-2 / Gadget-1 Initial condition
    file to turn into a Hdf5 file for running a simulation code
    
    :param base_name: Name of the Gadget file
    :type base_name: srt
    """

    def __init__(self, base_name: str):
        self.base_name = base_name

    def create_data(self):
        return
