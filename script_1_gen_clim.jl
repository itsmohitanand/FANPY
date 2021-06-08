using Pkg

Pkg.activate("FANPYjl/")

using MAT

fpath = "/data/compoundx/WG_sim/"
fname = "results_Beech_1000.mat"

julian_day = "DS"
precip = "Prs"
pressure = "Pres"
temp = "Tas"
wind = "Wss"
SW_rad = "Rsws"
cloud_cover = "Ns"
rel_humidity = "Us"


f = matopen(fpath*fname)
jd= read(f, julian_day)
pr = read(f, precip)
println(round(jd[1]*24, digits = 1))
println(round(jd[2]*24, digits = 1))
println(pr[1])

close(f)