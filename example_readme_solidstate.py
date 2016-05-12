import sp


# ----- ORBIT TYPE ------- #
orbit='circle'         # the orbit 'abrupt' or 'circle' determines the phase interpolating function used to generate error                               superoperator from spin misalignment

# ----- POSITIONAL ERROR DISTRIBUTION ------- #
# ------------------------------------------------------------#
# ------- (distance from probe to data qubit is unity) ------- #
errortype= 'pillbox'   # the shape of the error distribution for qubit position on lattice
                      #     'normal' - a 3D normal distribution of errors. Standard
                      #         deviation in each dimension specified by parameters: sdInX, sdInY and sdInZ 
                   #     'disc' - a 2D uniform circlular distribution, the radius is specified by sdInX, sdInY
                      #     'pillbox' - a 3D cylindrical (in z-dimension) uniform distribution
                      #           the radius of the cylinder is specified by sdInX & sdInY, and the half-height of the
                      #           cylinder by sdInZ
sdInX=0.1              # in-plane (x) error parameter for qubit position
sdInY=0.1              # in-plane (y) error parameter for qubit position
sdInZ=0.05             # z-dirn or height error parameter for qubit position //note: physical location errors where average                     
# ----- ERROR PARAMETERS ------- #                      
pJ=0.0004              # Phase Jitter - pJ = O(delta^2)
                       # where delta is a small error in the phase accumulation on the probe, ideal phase being pi/2 with   
                       # a symmetric distribution of possible phase errors parametrised by delta. This arises from an error in
                       # the  interaction time between probe qubit and data qubit. The constants in front of delta^2 depend on 
                       #the  type of random distribution being considered. E.g. for a bimodal distribution {+delta ,-delta}
                       #then pJ~delta^2/4, for a uniform distribution (-delta,+delta) then pJ~delta^2/12.  This manifests
                       #itself as a phase error on both the data qubit and the probe qubit occuring with probability pJ.
                       # This is described by an error map: 
                       # E(rho) = (1-pJ) rho + pJ* Z_data.Z_probe (rho) Z_data.Z_probe
                       # where rho is the state after the ideal interaction.

pX=0.001/3              
pY=0.001/3
pZ=0.001/3             #three components (Pauli-X,Y,Z) of the probe flip error

prep=0.01              #probe initialisation error - phi_probe = (1-prep) |+> + prep |->

pLie=0.05              # probability of a measurment error. Applies a measurement operator of the form
                       #M_even(rho) = (1-pLie)|even><even| + pLie |odd><odd|

pErr=0.002             # data qubit decoherence - randomly apply an X,Y or Z with this probability between cycles             


tSteps=20
timespace=[1,1]
boundary=1

#added to make it work
meas=pLie
data=pErr


#displacement R
dR=[0.09, 0.095, 0.1, 0.105, 0.11]
probability=[]

n_trials=1000

size=14                 # The size of the lattic12

for j in range(len(dR)):
    sdInX=dR[j]
    sdInY=dR[j]
    sdInZ=dR[j]/2.

    success_count=0
    
    for i in range(n_trials):
        #x,z = sp.run3Drandom(size,tSteps,p,pLie)

        x,z = sp.run3Dspin(size,errortype,orbit,tSteps,[sdInX,sdInY,sdInZ,pJ,pX,pY,pZ,prep,meas,data],timespace,boundary)
#        print [x,z]
        if x==1 and z==1: success_count+=1

    probability.append(success_count)   

    print j

print probability


#
# size 12, 1000
# [1000, 999, 999, 998, 994]
#


