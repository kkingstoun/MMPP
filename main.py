import parameters
import ovf 

if __name__ == "__main__":
    parms = parameters.ovfParms(head="m_y")
    M_txyz = ovf.OvfFile("C:/Users/Mateusz/Desktop/Radek/circular_10.out", parms)
    # print(M_txyz.array.shape)
