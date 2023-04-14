import numpy as np
import unsio.input as uns_in
import tables


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

        :return computational: A dictionary with all data
        """
        parttypes_in_gadget = "gas,halo,disk,bulge,stars,bndry".split(",")
        properties_in_gadget = "pos,vel,id,mass,u,rho,hsml,pot,acc".split(",")
        uns = uns_in.CUNS_IN(self.base_name, "all", "all", True)
        ok = uns.nextFrame("")
        computational = {}
        for all_parttypes in parttypes_in_gadget:
            computational[all_parttypes] = {}
            for all_props in properties_in_gadget:
                all_data = uns.getData(all_parttypes, all_props)[1]
                computational[all_parttypes].update({all_props: all_data})
        return computational

    def to_hdf5(self):
        """
        Create a hdf5 file format with all the data of
        the base Gadget-2/3 initial condition file
        """
        parttypes_in_gadget = "gas,halo,disk,bulge,stars,bndry".split(",")
        parttypes_in_hdf5 = "PartType0,PartType1,PartType2,PartType3,PartType4,PartType5".split(",")
        properties_in_gadget = "pos,vel,id,mass,u,rho,hsml,pot,acc".split(",")
        properties_in_hdf5 = "Coordinates,Velocities,ParticleIDs,Masses,InternalEnergy,Density,SmoothingLength," \
                             "Potential,Acceleration".split(",")
        gadget_file_data = self.create_data()
        with tables.open_file(f"{self.base_name}.hdf5", "w") as hdf5_file:
            for hdf5_parts, gadget_parts in zip(parttypes_in_hdf5, parttypes_in_gadget):
                hdf5_file.create_group("/", hdf5_parts)
                print(f"Translating Gadget-2/3 {gadget_parts} components to HDF5 {hdf5_parts}")
                for hdf5_props, gadget_props in zip(properties_in_hdf5, properties_in_gadget):
                    if (hdf5_props == 'Coordinates') | (hdf5_props == 'Velocities'):
                        old_vector = gadget_file_data[gadget_parts][gadget_props]
                        new_axis = int(len(old_vector) / 3)
                        new_vector = np.reshape(old_vector, (new_axis, 3))
                        hdf5_file.create_array(getattr(hdf5_file.root, hdf5_parts), hdf5_props, new_vector)
                    if (hdf5_props != 'Coordinates') & (hdf5_props != 'Velocities'):
                        new_vector = gadget_file_data[gadget_parts][gadget_props]
                        hdf5_file.create_array(getattr(hdf5_file.root, hdf5_parts), hdf5_props, new_vector)
