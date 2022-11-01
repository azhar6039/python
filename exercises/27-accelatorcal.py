#Create a function that calculates acceleration given initial velocity v1, final velocity v2, start time t1, and end time t2. The formula for acceleration is:



def accelator(v1,v2,t1,t2):
    diffVelocity=v2-v1
    difftime=t2-t1
    acceleration= diffVelocity/difftime  if difftime else 0
    return acceleration
value=accelator(0,10,0,20)
print(value)