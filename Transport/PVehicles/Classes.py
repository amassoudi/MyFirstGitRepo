'''
Created on 17 janv. 2014

@author: Massoudi-A
'''

import PUtils.config as cfg

class ClVehicle(object):
    '''
    A class representing vehicles
    '''


    def __init__(self, i_type, i_number, i_capacity, b_mix=True):
        '''
        The constructor
        @param i_type: vehicle type (0 for wheels vehicles, 1 for arerian, 2 for sea, 3 for ferries)
        @type i_type: int
        @param i_number: number (immatriculation, flight number...)
        @type i_number: int 
        @param i_capacity: vehicle capacity
        @type i_capacity: int 
        '''

        self.i_type = i_type
        self.i_number = i_number
        self.i_capacity = i_capacity
        self.b_mix = b_mix
        
        
    def getTypeName(self):
        return cfg.dct_veh_types[self.i_type]
    
    def __str__(self, *args, **kwargs):
        str_mix = ''
        if self.b_mix:
            str_mix += ' and supports mixed passengers'
        else:
            str_mix+= ' and does not support mixed passengers'
        return 'Vehicle number : %d, of type %s has a capacity of %d' % (self.i_number,
                                                                         self.getTypeName(),
                                                                         self.i_capacity) + str_mix
        
    
class Car(ClVehicle):
    '''
    A class representing vehicles
    '''


    def __init__(self, i_type, i_number, i_capacity, str_model, i_wheels_nb, i_power):
        '''
        The constructor
        @param i_type: vehicle type (0 for wheels vehicles, 1 for arerian, 2 for sea, 3 for ferries)
        @type i_type: int
        @param i_number: number (immatriculation, flight number...)
        @type i_number: int 
        @param i_capacity: vehicle capacity
        @type i_capacity: int 
        '''
        ClVehicle.__init__(self, i_type, i_number, i_capacity)
        self.str_model = str_model
        self.i_wheels_nb = i_wheels_nb
        self.i_power = i_power
        
    def __str__(self, *args, **kwargs):
        return ClVehicle.__str__(self, *args, **kwargs) + '''\n * The model is : %s\n
                                                                It has %d wheels
                                                                It has a power of %d''' % (self.str_model,
                                                                                           self.i_wheels_nb,
                                                                                           self.i_power)
        
        
