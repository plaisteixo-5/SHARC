# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 16:05:58 2017

@author: edgar
"""

class ParametersImt(object):

    __instance = None
    
    def __new__(cls, val):
        """
        This is the Singleton Pattern to ensure that this class will have only
        one instance
        """
        if ParametersImt.__instance is None:
            ParametersImt.__instance = object.__new__(cls)
        ParametersImt.__instance.val = val
        return ParametersImt.__instance    
    
    ###########################################################################
    # Number of base stations per cluster (must set to 19 in macrocell network)
    num_base_stations = 19
    
    ###########################################################################
    # Number of clusters (should be 1 or 7)
    num_clusters = 1
    
    ###########################################################################
    # Configures static or dynamic positions for base stations
    static_base_stations = True
    
    ###########################################################################
    # Inter-site distance in macrocell network topology
    intersite_distance = 1500
    
    ###########################################################################
    # Defines if IMT service is the interferer or interfered-with service
    interfered_with = False
    
    ###########################################################################
    # IMT center frequency [MHz]
    frequency = 27250

    ###########################################################################
    # IMT bandwidth [MHz]
    bandwidth = 500    
    
    ###########################################################################
    # The load probability (or activity factor) models the statistical 
    # variation of the network load by defining the number of fully loaded
    # base stations that are simultaneously transmitting
    bs_load_probability = 0.5
    
    ###########################################################################
    # Number of resource blocks per UE
    num_resource_blocks = 10

    ###########################################################################
    # Maximum base station transmit power [dBm]
    bs_tx_power = 37
    
    ###########################################################################
    # Base station height [m]
    bs_height = 30

    ###########################################################################
    # Base station transmit antenna gain [dBi]
    bs_tx_antenna_gain = 30
    
    ###########################################################################
    # Base station receive antenna gain [dBi]
    bs_rx_antenna_gain = 30
    
    ###########################################################################
    # Adjacent channel leakage power Ratio of the base station [dB]
    bs_aclr = 40    

    ###########################################################################
    # Adjacent channel selectivity of the base station [dB]
    bs_acs = 30    
    
    ###########################################################################
    # Number of UE that is allocated to each cell within to handover margin.
    # Remenber that in macrocell network each base station has 3 cells (sectors)
    ue_k = 10
    
    ###########################################################################
    # Multiplication factor that is used to ensure that the sufficient number
    # of UE's will distributed throughout ths system area such that the number
    # of K users is allocated to each cell. Normally, this values varies 
    # between 2 and 10 according to the user drop method
    ue_k_m = 10
    
    ###########################################################################
    # UE maximum transmit power [dBm]
    ue_tx_power = 20
    
    ###########################################################################
    # UE height [m]
    ue_height = 1.5
    
    ###########################################################################
    # UE transmit antenna gain [dBi]
    ue_tx_antenna_gain = 0
    
    ###########################################################################
    # UE receive antenna gain [dBi]
    ue_rx_antenna_gain = 0    
    
    ###########################################################################
    # Adjacent channel leakage power Ratio of the user equipment [dB]
    ue_aclr = 35    

    ###########################################################################
    # Adjacent channel selectivity of the user equipment [dB]
    ue_acs = 25    
    
    