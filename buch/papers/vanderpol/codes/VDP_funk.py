def VDP_funk(z_n, t_n):
    """ 
    z_n: Aktueller Zustandsvektor [y_n, y_n']
    t_n: Zeitvariable 
    """
    mu           = 8.53
    x_n          = z_n[0]
    v_n          = z_n[1]
    stoer_funk_n = 1.2*np.sin(t_n * 2*np.pi * 0.1)
    
    f_x          = v_n
    f_v          = mu*(1 - x_n**2)*v_n - x_n + stoer_funk_n
    
    return np.array([f_x, f_v], float)