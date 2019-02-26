import parameters
from ovf import OvfFile
import matplotlib.pyplot as plt

if __name__ == "__main__":
    parms = parameters.ovfParms(head="m_y",comp=0)

    mtzyxc = OvfFile(
        r"C:/Users/Mateusz/Desktop/Radek/circular_10.out2", parms)
    mtzyxc.calculateModes(eachX=True, eachY=True, comp=0)
    # vm.calculateModes()
