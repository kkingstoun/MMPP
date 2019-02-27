import numpy as np
import colorsys

class Hslcolormap():

    @staticmethod
    def hue_to_rgb(p, q, t):
            t += 1 if t < 0 else 0
            t -= 1 if t > 1 else 0
            if t < 1/6:
                    return p + (q - p) * 6 * t
            if t < 1/2:
                    return q
            if t < 2/3:
                    p + (q - p) * (2/3 - t) * 6
            return(p)

    @staticmethod
    def hsl_to_rgb(h, s, l):
        if s == 0:
            r, g, b = l, l, l
        else:
            q = l * (1 + s) if l < 0.5 else l + s - l * s
            p = 2 * l - q
            r = self.hue_to_rgb(p, q, h + 1/3)
            g = self.hue_to_rgb(p, q, h)
            b = self.hue_to_rgb(p, q, h - 1/3)


    def TransformToColor(self):
        M_szer_N = np.zeros([self.shape[1], self.shape[0], 3])
        print(M_szer_N.shape)

        # print(M_szer_0.T.shape)
        # print(M_szer_0.T[0, 0])
        # print(M_szer_N.shape)

        for x in range(self.shape[1]):
            for y in range(self.shape[0]):

                # print(x,y)
                cords = self[y, x]

                c_x = cords[1]
                c_y = cords[0]
                c_z = cords[2]

                angle = np.arctan2(c_x, c_y)*180/np.pi

                if (angle < 0):
                    angle = angle + 360

                if c_z < 0:

                    l = 0.5 - abs(c_z)/2
                    #l=0
                if c_z == 0:
                    l = 0.5
                if c_z > 0:
                    l = (1 - (1-c_z)/2)

                if c_z > 0.97:

                    l = (1 - (1-c_z)/2)

                color = colorsys.hls_to_rgb(angle/360, l, 1)

                if (c_x == 0 and c_y == 0 and c_y == 0):
                    M_szer_N[x, y, :] = (0.3, 0.3, 0.3)
                else:
                    M_szer_N[x, y, :] = color
                # print(color)
        return(M_szer_N)
