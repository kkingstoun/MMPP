import parameters
import visualizeFMRModes as vm
import ovf

if __name__ == "__main__":
    parms = parameters.ovfParms(head="m_y",comp=0)
    M_txyz = ovf.OvfFile(
        r"C:/Users/Mateusz/Desktop/Radek/circular_10.out", parms)
    Mfft = vm.VisualizeModes(M_txyz, eachX=True)
