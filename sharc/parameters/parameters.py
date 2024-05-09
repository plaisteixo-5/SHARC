# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 19:35:52 2017

@author: edgar
"""

import sys
import os
import configparser

from sharc.parameters.parameters_general import ParametersGeneral
from sharc.parameters.parameters_imt import ParametersImt
from sharc.parameters.parameters_hotspot import ParametersHotspot
from sharc.parameters.parameters_indoor import ParametersIndoor
from sharc.parameters.parameters_antenna_imt import ParametersAntennaImt
from sharc.parameters.parameters_eess_passive import ParametersEessPassive
from sharc.parameters.parameters_fs import ParametersFs
from sharc.parameters.parameters_fss_ss import ParametersFssSs
from sharc.parameters.parameters_fss_es import ParametersFssEs
from sharc.parameters.parameters_haps import ParametersHaps
from sharc.parameters.parameters_rns import ParametersRns
from sharc.parameters.parameters_ras import ParametersRas
from sharc.parameters.parameters_arns import ParametersArns


class Parameters(object):
    """
    Reads parameters from input file.
    """

    def __init__(self):
        self.file_name = None

        self.general = ParametersGeneral()
        self.imt = ParametersImt()
        self.antenna_imt = ParametersAntennaImt()
        self.hotspot = ParametersHotspot()
        self.indoor = ParametersIndoor()
        self.eess_passive = ParametersEessPassive()
        self.fs = ParametersFs()
        self.fss_ss = ParametersFssSs()
        self.fss_es = ParametersFssEs()
        self.haps = ParametersHaps()
        self.rns = ParametersRns()
        self.ras = ParametersRas()
        self.arns = ParametersArns()


    def set_file_name(self, file_name: str):
        """sets the configuration file name

        Parameters
        ----------
        file_name : str
            configuration file path
        """
        if not os.path.isfile(file_name):
            err_msg = f"PARAMETER ERROR [{self.__class__.__name__}]: \
                Could not find the configuration file {file_name}"
            sys.stderr.write(err_msg)
            sys.exit(1)
        self.file_name = file_name


    def read_params(self):
        """Read the parameters from the config file
        """
        config = configparser.ConfigParser()
        config.read(self.file_name)

        #######################################################################
        # GENERAL
        #######################################################################
        self.general.load_parameters_from_file(self.file_name)

        #######################################################################
        # IMT
        #######################################################################
        self.imt.load_parameters_from_file(self.file_name)

        #######################################################################
        # IMT ANTENNA
        #######################################################################
        self.antenna_imt.load_parameters_from_file(self.file_name)

        #######################################################################
        # HOTSPOT
        #######################################################################
        self.hotspot.load_parameters_from_file(self.file_name)

        #######################################################################
        # INDOOR
        #######################################################################
        self.indoor.load_parameters_from_file(self.file_name)

        #######################################################################
        # FSS space station
        #######################################################################
        self.fss_ss.load_parameters_from_file(self.file_name)

        #######################################################################
        # FSS earth station
        #######################################################################
        self.fss_es.load_parameters_from_file(self.file_name)

        #######################################################################
        # Fixed wireless service
        #######################################################################
        self.fs.load_parameters_from_file(self.file_name)

        #######################################################################
        # HAPS (airbone) station
        #######################################################################
        self.haps.load_parameters_from_file(self.file_name)

        #######################################################################
        # RNS
        #######################################################################
        self.rns.load_parameters_from_file(self.file_name)

        #######################################################################
        # RAS station
        #######################################################################
        self.ras.load_parameters_from_file(self.file_name)

        #######################################################################
        # EESS passive
        #######################################################################
        self.eess_passive.load_parameters_from_file(self.file_name)

        #######################################################################
        # ARNS
        #######################################################################
        self.arns.load_parameters_from_file(self.file_name)


if __name__ == "__main__":
    from pprint import pprint
    parameters = Parameters()
    param_sections = [a for a in dir(parameters) if not a.startswith('__') and not
                callable(getattr(parameters, a))]
    print("\n#### Dumping default parameters:")
    for p in param_sections:
        print("\n")
        pprint(getattr(parameters, p))
