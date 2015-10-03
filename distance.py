#Written by Selyce Bynes
#Based on formulas provided by Chris Veness here:
#http://www.movable-type.co.uk/scripts/latlong.html
import math

N_S = raw_input("N or S?\n")
N_S_degrees = int(input("Enter degrees: \n"))
N_S_minutes = int(input("Enter minutes: \n"))
N_S_seconds = int(input("Enter seconds: \n"))

E_W = raw_input("E or W?")
E_W_degrees = int(input("Enter degrees: \n"))
E_W_minutes = int(input("Enter minutes: \n"))
E_W_seconds = int(input("Enter seconds: \n"))

lat1 = (N_S_degrees + (N_S_minutes/60.0) + (N_S_seconds/3600.0))
if N_S == "S" or N_S == "s":
    lat1 *= -1
lon1 = (E_W_degrees + (E_W_minutes/60.0) + (E_W_seconds/3600.0))
if E_W == "W" or E_W == "w":
    lon1 *= -1

N_S = raw_input("N or S? \n")
N_S_degrees = int(input("Enter degrees: \n"))
N_S_minutes = int(input("Enter minutes: \n"))
N_S_seconds = int(input("Enter seconds: \n"))

E_W = raw_input("E or W?")
E_W_degrees = int(input("Enter degrees: \n"))
E_W_minutes = int(input("Enter minutes: \n"))
E_W_seconds = int(input("Enter seconds: \n"))

lat2 = (N_S_degrees + (N_S_minutes/60.0) + (N_S_seconds/3600.0))
if N_S == "S" or N_S == "s":
    lat2 *= -1
lon2 = (E_W_degrees + (E_W_minutes/60.0) + (E_W_seconds/3600.0))
if E_W == "W" or E_W == "w":
    lon2 *= -1

print "Lat 1: ", lat1, "Lon 1: ", lon1
print "Lat 2: ", lat2, "Lon 2: ", lon2

#Haversine Formula:
#a = sin²(Δφ/2) + cos φ1 ⋅ cos φ2 ⋅ sin²(Δλ/2)
#c = 2 ⋅ atan2( √a, √(1−a) )
#d = R ⋅ c

R = 6371000 #radius of Earth
sig_1 = math.radians(lat1)
sig_2 = math.radians(lat2)
delta_sig = math.radians(lat2-lat1)
delta_phi = math.radians(lon2-lon1)

a = math.sin(delta_sig/2) * math.sin(delta_sig/2) + math.cos(sig_1) * math.cos(sig_2) * math.sin(delta_phi/2) * math.sin(delta_phi/2)
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

d = R * c

print "Distance = ", d/1000, " km"
