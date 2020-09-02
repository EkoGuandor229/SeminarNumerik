def solve(step_input, initial_condition=(0.0,1.0)):
    t_min,t_max = 0.0,950.0
    h           = step_input
    t_points    = np.arange(t_min, t_max, h)
    x_points    = np.zeros([])
    y_points    = np.zeros([])

    # Setzen von Anfangsbedingungen fuer die Zustandsvariablen
    x_0,v_0     = initial_condition
    temp_z      = np.array([x_0, v_0], float)

    # Loesen fuer die Zeitentwicklung
    for t_n in t_points:
        x_points = np.append(x_points, [temp_z[0]])
        y_points = np.append(y_points, [temp_z[1]])
        temp_z  += RK_4(VDP_funk, temp_z, t_n, h)
        
    return (x_points, y_points, t_points)
