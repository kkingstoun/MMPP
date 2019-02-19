import parameters
import ovf 

if __name__ == "__main__":
    parms = parameters.ovfParms(head="m_y")
    M = ovf.OvfFile("X:\Projekty\Radek\circular_10.out", parms)
    # print(M.array.shape)
