def RK_4(func, z_n, t_n, h):
    """ 
    z_n: Aktueller Zustandsvektor [y_n, y_n']
    t_n: Zeitvariable 
    h  : Integrationsschritt
    """
    k1 = h*func(z_n, t_n)                     
    k2 = h*func(z_n + 0.5*k1, t_n + 0.5*h)
    k3 = h*func(z_n + 0.5*k2, t_n + 0.5*h)
    k4 = h*func(z_n + k3, t_n + h)
    
    return (k1 + 2*k2 + 2*k3 + k4)/6