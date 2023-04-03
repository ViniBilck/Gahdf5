import numpy as np
import unsio.input as uns_in


class Gahdf5:
    """
    Instance the data of a Gadget-2 / Gadget-1 Initial condition
    file to turn into a Hdf5 file for running a simulation code
    
    :param base_name: Name of the Gadget file
    :type base_name: srt
    """

    def __init__(self, base_name: str):
        self.base_name = base_name

    def create_data(self):
        """
        Create a dictionary with all the data of
        the initial condition file

        :return computational: A variable with all data
        """
        components = "gas,disk,halo,dm,stars,bulge,bndry"
        prop = "pos,vel,mass,acc,pot,rho,hsml,temp,age,metal,u,id,aux,keys"
        uns = uns_in.CUNS_IN(self.base_name, "all", "all", True)
        ok = uns.nextFrame("")
        computational = {}
        for all_components in components.split(","):
            computational[all_components] = {}
            for all_props in prop.split(","):
                all_data = uns.getData(all_components, all_props)[1]
                computational[all_components].update({all_props: all_data})
        return computational
