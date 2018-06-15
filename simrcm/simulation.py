import sim_tools 
import cantera as ct
import numpy as np

def simulation1(file):

    inputs = sim_tools.Inputs(file)
    
    bore = inputs.bore
    t0 = inputs.t0
    z = inputs.z
    v_rcm = inputs.v_rcm
    a_rcm = inputs.a_rcm
    t_wall = inputs.t_wall
    temp0 = inputs.temp0
    p0 = inputs.p0
    mechanism = inputs.mechanism
    mixture = inputs.mixture
    keywords = inputs.vprofile
    
    zone = sim_tools.def_zones(z, bore, t0, v_rcm, a_rcm)
    
    v_factor = [0]
    for x in range(1,z+1):
        v_factor.append(zone[x].r_volume*a_rcm)
        
    r, env, contents = sim_tools.def_reactors(z, zone, temp0, p0, mechanism, mixture)
    wq , wv = sim_tools.def_walls(r, env, zone, z, v_factor, keywords, t_wall, a_rcm)
    
    netw =[0]        
    for x in range(1,z+1):        
        netw.append(ct.ReactorNet([r[x]]))
        
    time = []
    pressure = []
    temperature = []
    #OH_y = []
    #for x in range(1,z+1):
        #pressure.append(sim_tools.State
        
    while netw[1].time < 0.05:
        time.append(netw[1].time)
        temperature.append(r[1].thermo.T)
        pressure.append(r[6].thermo.P)
        #OH_y.append(sim_tools.get_species_mass(5, r, z))
        for x in range(1,z+1):
            netw[x].step()   
        zone, r = sim_tools.cell_rezone(z, r, zone, contents) 
        wq = sim_tools.modify_walls(wq, z, zone, r, t_wall) 
    
    
    dpdt = np.gradient(pressure, time, edge_order=2) 
    ignition_delay = time[np.argmax(dpdt)]
    
    
    
    return ignition_delay, pressure, temperature, time