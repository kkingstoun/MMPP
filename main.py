import parameters
import visualizeFMRModes
import ovf

if __name__ == "__main__":
    parms = parameters.ovfParms(head="m_y",comp=0)

    M_txyz = ovf.OvfFile(
        r"C:/Users/Mateusz/Desktop/Radek/circular_10.out", parms).array
    print(M_txyz.shape)
    # vm = visualizeFMRModes.VisualizeModes()
    # Mfft = vm.calculateModes(M_txyz, eachX=True)
