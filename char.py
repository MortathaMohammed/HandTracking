from fingers import method as mt
x = 1
y = 2


class character:

    def A_a(list, tipIds):
        return ((mt.thumb(list, tipIds)[0][2] > mt.thumb(list, tipIds)[1][2] > mt.thumb(list, tipIds)[2][2] > mt.thumb(list, tipIds)[3][2]) and
                (mt.thumb(list, tipIds)[3][1] < mt.index(list, tipIds)[3][1]) and (mt.index(list, tipIds)[3][2] > mt.index(list, tipIds)[0][2]) and
                (mt.middle(list, tipIds)[3][2] > mt.middle(list, tipIds)[0][2]) and (mt.ring(list, tipIds)[3][2] > mt.ring(list, tipIds)[0][2]) and
                (mt.little(list, tipIds)[3][2] > mt.little(list, tipIds)[0][2]) and (mt.index(list, tipIds)[2][2] > mt.index(list, tipIds)[0][2]) and
                (mt.middle(list, tipIds)[2][2] > mt.middle(list, tipIds)[0][2]) and (mt.ring(list, tipIds)[2][2] > mt.ring(list, tipIds)[0][2]) and
                (mt.little(list, tipIds)[2][2] > mt.little(list, tipIds)[0][2]))

    def B_b(list, tipIds):
        return ((mt.thumb(list, tipIds)[0][2] > mt.thumb(list, tipIds)[1][2] > mt.thumb(list, tipIds)[2][2] > mt.thumb(list, tipIds)[3][2]) and
                (mt.index(list, tipIds)[3][2] < mt.index(list, tipIds)[2][2] < mt.index(list, tipIds)[1][2] < mt.index(list, tipIds)[0][2]) and
                (mt.middle(list, tipIds)[3][2] < mt.middle(list, tipIds)[2][2] < mt.middle(list, tipIds)[1][2] < mt.middle(list, tipIds)[0][2]) and
                (mt.ring(list, tipIds)[3][2] < mt.ring(list, tipIds)[2][2] < mt.ring(list, tipIds)[1][2] < mt.ring(list, tipIds)[0][2]) and
                (mt.little(list, tipIds)[3][2] < mt.little(list, tipIds)[2][2] < mt.little(list, tipIds)[1][2] < mt.little(list, tipIds)[0][2]) and
                (mt.thumb(list, tipIds)[3][1] > mt.index(list, tipIds)[3][1]))

    def C_c(list, tipIds):
        return ((mt.thumb(list, tipIds)[0][2] > mt.thumb(list, tipIds)[1][2] > mt.thumb(list, tipIds)[2][2] > mt.thumb(list, tipIds)[3][2]) and
                (mt.index(list, tipIds)[1][2] < mt.index(list, tipIds)[3][2] < mt.index(list, tipIds)[0][2]) and
                (mt.middle(list, tipIds)[1][2] < mt.middle(list, tipIds)[3][2] < mt.middle(list, tipIds)[0][2]) and
                (mt.ring(list, tipIds)[1][2] < mt.ring(list, tipIds)[3][2] < mt.ring(list, tipIds)[0][2]) and
                (mt.little(list, tipIds)[1][2] < mt.little(list, tipIds)[3][2] < mt.little(list, tipIds)[0][2]) and
                (mt.thumb(list, tipIds)[0][1] > mt.thumb(list, tipIds)[3][1] > mt.thumb(list, tipIds)[2][1]))

    def D_d(list, tipIds):
        return ((mt.thumb(list, tipIds)[0][2] > mt.thumb(list, tipIds)[1][2] > mt.thumb(list, tipIds)[2][2] > mt.thumb(list, tipIds)[3][2]) and
                (mt.index(list, tipIds)[3][2] < mt.index(list, tipIds)[2][2] < mt.index(list, tipIds)[1][2] < mt.index(list, tipIds)[0][2]) and
                (mt.middle(list, tipIds)[3][2] > mt.middle(list, tipIds)[0][2]) and (mt.ring(list, tipIds)[3][2] > mt.ring(list, tipIds)[0][2]) and
                (mt.little(list, tipIds)[3][2] > mt.little(list, tipIds)[0][2]) and
                (mt.thumb(list, tipIds)[0][1] < mt.thumb(list, tipIds)[3][1]) and
                (mt.index(list, tipIds)[3][1] < mt.middle(list, tipIds)[0][1]))

    def E_e(list, tipIds):
        return ((mt.index(list, tipIds)[3][2] > mt.index(list, tipIds)[2][2] > mt.index(list, tipIds)[1][2]) and
                (mt.middle(list, tipIds)[3][2] > mt.middle(list, tipIds)[2][2] > mt.middle(list, tipIds)[1][2]) and
                (mt.ring(list, tipIds)[3][2] > mt.ring(list, tipIds)[2][2] > mt.ring(list, tipIds)[1][2]) and
                (mt.little(list, tipIds)[3][2] > mt.little(list, tipIds)[2][2] > mt.little(list, tipIds)[1][2]) and
                (mt.ring(list, tipIds)[3][1] < mt.thumb(list, tipIds)[3][1]) and (mt.ring(list, tipIds)[3][2] < mt.thumb(list, tipIds)[3][2]) and
                (mt.thumb(list, tipIds)[3][1] < mt.little(list, tipIds)[0][1]))

    def F_f(list, tipIds):
        return ((mt.ring(list, tipIds)[0][2] > mt.ring(list, tipIds)[1][2] > mt.ring(list, tipIds)[2][2] > mt.ring(list, tipIds)[3][2]) and
                (mt.little(list, tipIds)[0][2] > mt.little(list, tipIds)[1][2] > mt.little(list, tipIds)[2][2] > mt.little(list, tipIds)[3][2]) and
                (mt.middle(list, tipIds)[0][2] > mt.middle(list, tipIds)[1][2] > mt.middle(list, tipIds)[2][2] > mt.middle(list, tipIds)[3][2]) and
                (mt.index(list, tipIds)[1][2] < mt.index(list, tipIds)[3][2]) and
                (mt.thumb(list, tipIds)[2][1] < mt.thumb(list, tipIds)[3][1]))

    def G_g(list, tipIds):
        return ((mt.ring(list, tipIds)[1][1] > mt.ring(list, tipIds)[2][1] > mt.ring(list, tipIds)[3][1]) and
                (mt.little(list, tipIds)[1][1] > mt.little(list, tipIds)[2][1] > mt.little(list, tipIds)[3][1]) and
                (mt.middle(list, tipIds)[1][1] > mt.middle(list, tipIds)[2][1] > mt.middle(list, tipIds)[3][1]) and
                (mt.index(list, tipIds)[0][1] < mt.index(list, tipIds)[1][1] < mt.index(list, tipIds)[2][1] < mt.index(list, tipIds)[3][1]) and
                (mt.thumb(list, tipIds)[0][1] < mt.thumb(list, tipIds)[1][1] < mt.thumb(list, tipIds)[2][1] < mt.thumb(list, tipIds)[3][1]) and
                (mt.thumb(list, tipIds)[3][1] < mt.index(list, tipIds)[2][1]) and 
                (mt.index(list, tipIds)[3][2] > mt.index(list, tipIds)[0][2]))

    def H_h(list, tipIds):
        return ((mt.ring(list, tipIds)[1][1] > mt.ring(list, tipIds)[2][1] > mt.ring(list, tipIds)[3][1]) and
                (mt.little(list, tipIds)[1][1] > mt.little(list, tipIds)[2][1] > mt.little(list, tipIds)[3][1]) and
                (mt.middle(list, tipIds)[0][1] < mt.middle(list, tipIds)[1][1] < mt.middle(list, tipIds)[2][1] < mt.middle(list, tipIds)[3][1]) and
                (mt.index(list, tipIds)[0][1] < mt.index(list, tipIds)[1][1] < mt.index(list, tipIds)[2][1] < mt.index(list, tipIds)[3][1]) and
                (mt.thumb(list, tipIds)[0][1] < mt.thumb(list, tipIds)[1][1] < mt.thumb(list, tipIds)[2][1] < mt.thumb(list, tipIds)[3][1]) and
                (mt.thumb(list, tipIds)[3][1] > mt.ring(list, tipIds)[2][1]))

    def I_i(list, tipIds):
        return ((mt.little(list, tipIds)[0][2] > mt.little(list, tipIds)[1][2] > mt.little(list, tipIds)[2][2] > mt.little(list, tipIds)[3][2]) and
                (mt.middle(list, tipIds)[1][2] < mt.middle(list, tipIds)[2][2] < mt.middle(list, tipIds)[3][2]) and
                (mt.ring(list, tipIds)[1][2] < mt.ring(list, tipIds)[2][2] < mt.ring(list, tipIds)[3][2]) and
                (mt.index(list, tipIds)[1][2] < mt.index(list, tipIds)[2][2] < mt.index(list, tipIds)[3][2]) and
                (mt.thumb(list, tipIds)[0][2] > mt.thumb(list, tipIds)[1][2] > mt.thumb(list, tipIds)[2][2] > mt.thumb(list, tipIds)[3][2]) and
                (mt.thumb(list, tipIds)[3][1] > mt.index(list, tipIds)[2][1]) and (mt.thumb(list, tipIds)[3][2] < mt.index(list, tipIds)[2][2]))

    def J_j(list, tipIds):
        return (mt.little(list, tipIds)[3][1] < (mt.little(list, tipIds)[0][1]) and
                (mt.middle(list, tipIds)[3][1] > mt.middle(list, tipIds)[1][1]) and
                (mt.ring(list, tipIds)[3][1] > mt.ring(list, tipIds)[1][1]) and
                (mt.index(list, tipIds)[3][1] > mt.index(list, tipIds)[1][1]) and
                (mt.thumb(list, tipIds)[3][1] < mt.thumb(list, tipIds)[1][1]))

    def K_k(list, tipIds):
        return ((mt.index(list, tipIds)[0][2] > mt.index(list, tipIds)[1][2] > mt.index(list, tipIds)[2][2] > mt.index(list, tipIds)[3][2]) and
                (mt.middle(list, tipIds)[0][2] > mt.middle(list, tipIds)[1][2] > mt.middle(list, tipIds)[2][2] > mt.middle(list, tipIds)[3][2]) and
                (mt.ring(list, tipIds)[1][2] < mt.ring(list, tipIds)[2][2] < mt.ring(list, tipIds)[3][2]) and
                (mt.little(list, tipIds)[1][2] < mt.little(list, tipIds)[2][2] < mt.little(list, tipIds)[3][2]) and
                (mt.middle(list, tipIds)[1][1] > mt.thumb(list, tipIds)[3][1] > mt.index(list, tipIds)[1][1]) and
                (mt.thumb(list, tipIds)[3][2] < mt.index(list, tipIds)[0][2]))

    def L_l(list, tipIds):
        return ((mt.index(list, tipIds)[3][2] < mt.index(list, tipIds)[2][2] < mt.index(list, tipIds)[1][2] < mt.index(list, tipIds)[0][2]) and
                (mt.middle(list, tipIds)[3][2] > mt.middle(list, tipIds)[0][2]) and (mt.ring(list, tipIds)[3][2] > mt.ring(list, tipIds)[0][2]) and
                (mt.little(list, tipIds)[2][2] > mt.little(list, tipIds)[0][2]) and
                (mt.thumb(list, tipIds)[3][1] <= mt.middle(list, tipIds)[3][1]) and
                (mt.thumb(list, tipIds)[3][1] < mt.thumb(list, tipIds)[1][1]))

    def M_m(list, tipIds):
        return ((mt.index(list, tipIds)[1][2] < mt.index(list, tipIds)[2][2] < mt.index(list, tipIds)[3][2]) and
                (mt.middle(list, tipIds)[1][2] < mt.middle(list, tipIds)[2][2] < mt.middle(list, tipIds)[3][2]) and
                (mt.ring(list, tipIds)[1][2] < mt.ring(list, tipIds)[2][2] < mt.ring(list, tipIds)[3][2]) and
                (mt.little(list, tipIds)[1][2] < mt.little(list, tipIds)[2][2] < mt.little(list, tipIds)[3][2]) and
                (mt.index(list, tipIds)[0][1] < mt.thumb(list, tipIds)[3][1] < mt.middle(list, tipIds)[0][1]) and
                ((mt.thumb(list, tipIds)[3][2] < mt.index(list, tipIds)[2][2])))

    def N_n(list, tipIds):
        return ((mt.index(list, tipIds)[1][2] < mt.index(list, tipIds)[2][2] < mt.index(list, tipIds)[3][2]) and
                (mt.middle(list, tipIds)[1][2] < mt.middle(list, tipIds)[2][2] < mt.middle(list, tipIds)[3][2]) and
                (mt.ring(list, tipIds)[1][2] < mt.ring(list, tipIds)[2][2] < mt.ring(list, tipIds)[3][2]) and
                (mt.little(list, tipIds)[1][2] < mt.little(list, tipIds)[2][2] < mt.little(list, tipIds)[3][2]) and
                (mt.middle(list, tipIds)[0][1] < mt.thumb(list, tipIds)[3][1] < mt.ring(list, tipIds)[0][1]) and
                ((mt.thumb(list, tipIds)[3][2] < mt.index(list, tipIds)[2][2])))

    def O_o(list, tipIds):
        return ((mt.thumb(list, tipIds)[3][2] < mt.thumb(list, tipIds)[2][2] < mt.thumb(list, tipIds)[1][2] < mt.thumb(list, tipIds)[0][2]) and 
                (mt.thumb(list, tipIds)[3][1] > mt.thumb(list, tipIds)[2][1] > mt.thumb(list, tipIds)[1][1] > mt.thumb(list, tipIds)[0][1]) and
                (mt.index(list, tipIds)[3][2] > mt.index(list, tipIds)[0][2]) and 
                (mt.middle(list, tipIds)[3][2] > mt.middle(list, tipIds)[0][2]) and 
                (mt.ring(list, tipIds)[3][2] > mt.ring(list, tipIds)[0][2]) and 
                (mt.little(list, tipIds)[3][2] > mt.little(list, tipIds)[0][2]) and 

                (mt.index(list, tipIds)[3][2] < mt.thumb(list, tipIds)[3][2]) and
                (mt.middle(list, tipIds)[3][2] < mt.thumb(list, tipIds)[3][2]) and
                (mt.ring(list, tipIds)[3][2] < mt.thumb(list, tipIds)[3][2]) and
                (mt.little(list, tipIds)[3][2] < mt.thumb(list, tipIds)[3][2]) and
                (mt.thumb(list, tipIds)[0][1] > mt.index(list, tipIds)[0][1]))

    def P_p(list, tipIds):
        return ((mt.thumb(list, tipIds)[0][2] < mt.thumb(list, tipIds)[1][2] < mt.thumb(list, tipIds)[2][2] < mt.thumb(list, tipIds)[3][2]) and
                (mt.index(list, tipIds)[3][1] < mt.index(list, tipIds)[2][1] < mt.index(list, tipIds)[1][1] < mt.index(list, tipIds)[0][1]) and
                (mt.middle(list, tipIds)[3][2] > mt.middle(list, tipIds)[0][2]) and
                (mt.ring(list, tipIds)[3][2] > mt.ring(list, tipIds)[0][2]) and
                (mt.little(list, tipIds)[2][2] > mt.little(list, tipIds)[0][2]) and
                (mt.thumb(list, tipIds)[3][2] >= mt.middle(list, tipIds)[2][2]))

    def Q_q(list, tipIds):
        return ((mt.thumb(list, tipIds)[0][2] < mt.thumb(list, tipIds)[1][2] < mt.thumb(list, tipIds)[2][2] < mt.thumb(list, tipIds)[3][2]) and
                (mt.index(list, tipIds)[3][2] > mt.index(list, tipIds)[0][2]) and
                (mt.middle(list, tipIds)[1][2] > mt.middle(list, tipIds)[0][2]) and (mt.middle(list, tipIds)[1][2] > mt.middle(list, tipIds)[3][2]) and
                (mt.ring(list, tipIds)[1][2] > mt.ring(list, tipIds)[0][2]) and (mt.ring(list, tipIds)[1][2] > mt.ring(list, tipIds)[3][2]) and
                (mt.little(list, tipIds)[1][2] > mt.little(list, tipIds)[0][2]) and (mt.little(list, tipIds)[1][2] > mt.little(list, tipIds)[3][2]) and
                (mt.thumb(list, tipIds)[3][2] >= mt.index(list, tipIds)[2][2]))

    def R_r(list, tipIds):
        return ((mt.thumb(list, tipIds)[0][2] > mt.thumb(list, tipIds)[1][2] > mt.thumb(list, tipIds)[2][2] > mt.thumb(list, tipIds)[3][2]) and
                (mt.index(list, tipIds)[3][2] < mt.index(list, tipIds)[2][2] < mt.index(list, tipIds)[1][2] < mt.index(list, tipIds)[0][2]) and
                (mt.middle(list, tipIds)[3][2] < mt.middle(list, tipIds)[2][2] < mt.middle(list, tipIds)[1][2] < mt.middle(list, tipIds)[0][2]) and
                (mt.ring(list, tipIds)[3][2] > mt.ring(list, tipIds)[0][2]) and
                (mt.little(list, tipIds)[3][2] > mt.little(list, tipIds)[0][2]) and
                (mt.thumb(list, tipIds)[3][2] <= mt.ring(list, tipIds)[2][2]) and
                (mt.index(list, tipIds)[3][1] > mt.middle(list, tipIds)[3][1]))

    def S_s(list, tipIds):
        return ((mt.index(list, tipIds)[3][2] > mt.index(list, tipIds)[0][2]) and
                (mt.middle(list, tipIds)[3][2] > mt.middle(list, tipIds)[0][2]) and
                (mt.ring(list, tipIds)[3][2] > mt.ring(list, tipIds)[0][2]) and
                (mt.little(list, tipIds)[3][2] > mt.little(list, tipIds)[0][2]) and
                (mt.thumb(list, tipIds)[0][1] < mt.thumb(list, tipIds)[3][1]) and
                (mt.thumb(list, tipIds)[3][1] < mt.ring(list, tipIds)[1][1]))

    def T_t(list, tipIds):
        return ((mt.index(list, tipIds)[3][2] > mt.index(list, tipIds)[0][2]) and
                (mt.middle(list, tipIds)[3][2] > mt.middle(list, tipIds)[0][2]) and
                (mt.ring(list, tipIds)[3][2] > mt.ring(list, tipIds)[0][2]) and
                (mt.little(list, tipIds)[3][2] > mt.little(list, tipIds)[0][2]) and
                (mt.thumb(list, tipIds)[0][1] < mt.middle(list, tipIds)[3][1]) and
                (mt.thumb(list, tipIds)[3][1] < mt.ring(list, tipIds)[1][1]))

    def U_u(list, tipIds):
        return ((mt.thumb(list, tipIds)[0][2] > mt.thumb(list, tipIds)[1][2] > mt.thumb(list, tipIds)[2][2] > mt.thumb(list, tipIds)[3][2]) and
                (mt.index(list, tipIds)[3][2] < mt.index(list, tipIds)[2][2] < mt.index(list, tipIds)[1][2] < mt.index(list, tipIds)[0][2]) and
                (mt.middle(list, tipIds)[3][2] < mt.middle(list, tipIds)[2][2] < mt.middle(list, tipIds)[1][2] < mt.middle(list, tipIds)[0][2]) and
                (mt.ring(list, tipIds)[3][2] > mt.ring(list, tipIds)[0][2]) and
                (mt.little(list, tipIds)[3][2] > mt.little(list, tipIds)[0][2]) and
                (mt.thumb(list, tipIds)[3][2] <= mt.ring(list, tipIds)[2][2]) and not (mt.index(list, tipIds)[3][1] > mt.middle(list, tipIds)[3][1]) and 
                (mt.index(list, tipIds)[3][1] >= mt.index(list, tipIds)[0][1]) and 
                (mt.middle(list, tipIds)[3][1] > mt.index(list, tipIds)[0][1]))
    
    def V_v(list, tipIds):
        return ((mt.thumb(list, tipIds)[0][2] > mt.thumb(list, tipIds)[1][2] > mt.thumb(list, tipIds)[2][2] > mt.thumb(list, tipIds)[3][2]) and
                (mt.index(list, tipIds)[3][2] < mt.index(list, tipIds)[2][2] < mt.index(list, tipIds)[1][2] < mt.index(list, tipIds)[0][2]) and
                (mt.middle(list, tipIds)[3][2] < mt.middle(list, tipIds)[2][2] < mt.middle(list, tipIds)[1][2] < mt.middle(list, tipIds)[0][2]) and
                (mt.ring(list, tipIds)[3][2] > mt.ring(list, tipIds)[0][2]) and
                (mt.little(list, tipIds)[3][2] > mt.little(list, tipIds)[0][2]) and
                (mt.thumb(list, tipIds)[3][2] <= mt.ring(list, tipIds)[2][2]) and not (mt.index(list, tipIds)[3][1] > mt.middle(list, tipIds)[3][1]) and
                (mt.index(list, tipIds)[3][1] < mt.index(list, tipIds)[0][1]) and 
                (mt.middle(list, tipIds)[3][1] > mt.index(list, tipIds)[0][1]))

    def W_w(list, tipIds):
        return ((mt.thumb(list, tipIds)[0][2] > mt.thumb(list, tipIds)[1][2] > mt.thumb(list, tipIds)[2][2] > mt.thumb(list, tipIds)[3][2]) and
                (mt.index(list, tipIds)[3][2] < mt.index(list, tipIds)[2][2] < mt.index(list, tipIds)[1][2] < mt.index(list, tipIds)[0][2]) and
                (mt.middle(list, tipIds)[3][2] < mt.middle(list, tipIds)[2][2] < mt.middle(list, tipIds)[1][2] < mt.middle(list, tipIds)[0][2]) and
                (mt.ring(list, tipIds)[3][2] < mt.ring(list, tipIds)[0][2]) and
                (mt.little(list, tipIds)[3][2] > mt.little(list, tipIds)[0][2]) and
                (mt.thumb(list, tipIds)[3][2] <= mt.little(list, tipIds)[2][2]))

    def X_x(list, tipIds):
        return (
            (mt.index(list, tipIds)[3][2] < mt.index(list, tipIds)[0][2]) and (mt.index(list, tipIds)[3][2] > mt.index(list, tipIds)[1][2]) and
            (mt.thumb(list, tipIds)[0][2] > mt.thumb(list, tipIds)[1][2] > mt.thumb(list, tipIds)[2][2] > mt.thumb(list, tipIds)[3][2]) and
            (mt.middle(list, tipIds)[3][2] > mt.middle(list, tipIds)[0][2]) and
            (mt.ring(list, tipIds)[3][2] > mt.ring(list, tipIds)[0][2]) and
            (mt.little(list, tipIds)[3][2] > mt.little(list, tipIds)[0][2]))

    def Y_y(list, tipIds):
        return ((mt.little(list, tipIds)[0][2] > mt.little(list, tipIds)[1][2] > mt.little(list, tipIds)[2][2] > mt.little(list, tipIds)[3][2]) and
                (mt.middle(list, tipIds)[1][2] < mt.middle(list, tipIds)[2][2] < mt.middle(list, tipIds)[3][2]) and
                (mt.ring(list, tipIds)[1][2] < mt.ring(list, tipIds)[2][2] < mt.ring(list, tipIds)[3][2]) and
                (mt.index(list, tipIds)[1][2] < mt.index(list, tipIds)[2][2] < mt.index(list, tipIds)[3][2]) and
                (mt.thumb(list, tipIds)[0][2] > mt.thumb(list, tipIds)[1][2] > mt.thumb(list, tipIds)[2][2] > mt.thumb(list, tipIds)[3][2]) and
                (mt.thumb(list, tipIds)[3][1] < mt.thumb(list, tipIds)[2][1]))

    def Z_z(list, tipIds):
        return ((mt.thumb(list, tipIds)[0][2] > mt.thumb(list, tipIds)[1][2] > mt.thumb(list, tipIds)[2][2] > mt.thumb(list, tipIds)[3][2]) and
                (mt.middle(list, tipIds)[3][2] > mt.middle(list, tipIds)[0][2]) and 
                (mt.ring(list, tipIds)[3][2] > mt.ring(list, tipIds)[0][2]) and
                (mt.little(list, tipIds)[3][2] > mt.little(list, tipIds)[0][2]) and
                (mt.thumb(list, tipIds)[0][1] < mt.thumb(list, tipIds)[3][1]) and
                 (mt.index(list, tipIds)[3][1] > mt.middle(list, tipIds)[0][1]) and
                 (mt.index(list, tipIds)[3][2] < mt.middle(list, tipIds)[0][2])
        )
