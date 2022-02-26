using HDF5
using CairoMakie
using Statistics
using FFTW
using DSP

ENV["GKSwstype"] = "100"

DATA_FOLDER = "/p/project/hai_deep_c/project_data/forest-carbon-flux/ml_data/"


met = Array{Float64}(undef, 18000, 365, 3)

gpp = Array{Float64}(undef, 18000)


for i=1:2
    fid = h5open(DATA_FOLDER*"data_100ha_$(i-1).h5", "r") 
    x = fid["X"]
    y = fid["Y"]

    met[(i-1)*9000+1:i*9000, :,1] = permutedims(x["irradiance"][:,:], (2, 1))
    met[(i-1)*9000+1:i*9000, :,2] = permutedims(x["rain"][:,:], (2, 1))
    met[(i-1)*9000+1:i*9000, :,3] = permutedims(x["temperature"][:,:], (2, 1))


    gpp[(i-1)*9000+1:i*9000] = y["GPP"][:]
    
end

X = Array{Float64}(undef, 18000-3, 365*4, 3)

Y = Array{Float64}(undef, 18000-3)

for i=1:size(gpp)[1]-3
    X[i, :, 1] = vec(permutedims(met[i:i+3, :, 1], (2,1)))
    X[i, :, 2] = vec(permutedims(met[i:i+3, :, 2], (2,1)))
    X[i, :, 3] = vec(permutedims(met[i:i+3, :, 3], (2,1)))

    Y[i] = gpp[i+3]
end

num = 1 
gpp_1 = Array{Float64}(undef, 18000-num)

for i=1:size(gpp)[1]-num
    gpp_1[i] = gpp[i+num]
end

num = 2 
gpp_2 = Array{Float64}(undef, 18000-num)

for i=1:size(gpp)[1]-num
    gpp_2[i] = gpp[i+num]
end

num = 3 
gpp_3 = Array{Float64}(undef, 18000-num)

for i=1:size(gpp)[1]-num
    gpp_3[i] = gpp[i+num]
end

num = 4 
gpp_4 = Array{Float64}(undef, 18000-num)

for i=1:size(gpp)[1]-num
    gpp_4[i] = gpp[i+num]
end

num = 5 
gpp_5 = Array{Float64}(undef, 18000-num)

for i=1:size(gpp)[1]-num
    gpp_5[i] = gpp[i+num]
end

num = 6 
gpp_6 = Array{Float64}(undef, 18000-num)

for i=1:size(gpp)[1]-num
    gpp_6[i] = gpp[i+num]
end


mean_met = mean(X, dims = 1)


set_theme!(theme_light())


mgp = mean(gpp)*100

gpp_5p = quantile(gpp, 0.05)*100

met_low_4 = X[(Y*100).<gpp_5p,:,:]


met_not_low_4 = X[(Y*100).>=gpp_5p,:,:]

mean_low = mean(met_low_4, dims = 1)
mean_not_low = mean(met_not_low_4, dims = 1)


f = Figure(backgroundcolor = RGBf(0.98, 0.98, 0.98),
    resolution = (2000, 800))

gi = f[1,1:4] = GridLayout()
gp = f[2,1:4] = GridLayout()
gt = f[3,1:4] = GridLayout()
gg = f[1:3,5:7] = GridLayout()

gai = f[4, 1:7] = GridLayout()
gap = f[5, 1:7] = GridLayout()
gat = f[6, 1:7] = GridLayout()


w = 8
ggs1 = f[1:3, w:w+2] = GridLayout()
ggs2 = f[4:6, w:w+2] = GridLayout()
ggs3 = f[1:3, w+3:w+5] = GridLayout()
ggs4 = f[4:6, w+3:w+5] = GridLayout()
ggs5 = f[1:3, w+6:w+8] = GridLayout()
ggs6 = f[4:6, w+6:w+8] = GridLayout()


axai = Axis(gai[1,1])
axap = Axis(gap[1,1])
axat = Axis(gat[1,1])

axs1 = Axis(ggs1[1,1], xlabel = "GPP | t year", ylabel = "GPP | t-1 year")
axs2 = Axis(ggs2[1,1], xlabel = "GPP | t year", ylabel = "GPP | t-2 year")
axs3 = Axis(ggs3[1,1], xlabel = "GPP | t year", ylabel = "GPP | t-3 year")
axs4 = Axis(ggs4[1,1], xlabel = "GPP | t year", ylabel = "GPP | t-4 year")
axs5 = Axis(ggs5[1,1], xlabel = "GPP | t year", ylabel = "GPP | t-5 year")
axs6 = Axis(ggs6[1,1], xlabel = "GPP | t year", ylabel = "GPP | t-6 year")


axi = Axis(gi[1,1])
axp = Axis(gp[1,1])
axt = Axis(gt[1,1])
axg = Axis(gg[1,1])



lines!(axi, mean_met[1, :, 1])
lines!(axp, mean_met[1, :, 2])
lines!(axt, mean_met[1, :, 3])

density!(axg, gpp*100, label = "GPP")
vlines!(axg, mgp, label = "mean : $(round(mgp,digits =2))", color = :blue)
vlines!(axg, gpp_5p, label = "5th perc $(round(gpp_5p,digits =2))", color = :red)


axislegend(axg, merge = true)


lines!(axai, mean_low[1, :, 1]-mean_met[1, :, 1], label = "low")
lines!(axap, mean_low[1, :, 2]-mean_met[1, :, 2], label = "low")
lines!(axat, mean_low[1, :, 3]-mean_met[1, :, 3], label = "low")

lines!(axai, mean_not_low[1, :, 1]-mean_met[1, :, 1], label = "not_low")
lines!(axap, mean_not_low[1, :, 2]-mean_met[1, :, 2], label = "not_low")
lines!(axat, mean_not_low[1, :, 3]-mean_met[1, :, 3], label = "not_low")

axislegend(axai, merge = true)


num  = 1
scatter!(axs1, gpp[1:end-num]*100, gpp_1*100, markersize = 2.0)
lines!(axs1, [800, 1300], [800, 1400], linestyle = :dash, color = :red)

num  = 2
scatter!(axs2, gpp[1:end-num].*100, gpp_2*100, markersize = 2.0)
lines!(axs2, [800, 1300], [800, 1400], linestyle = :dash, color = :red)

num  = 3
scatter!(axs3, gpp[1:end-num]*100, gpp_3*100, markersize = 2.0)
lines!(axs3, [800, 1300], [800, 1400], linestyle = :dash, color = :red)

num  = 4
scatter!(axs4, gpp[1:end-num]*100, gpp_4*100, markersize = 2.0)
lines!(axs4, [800, 1300], [800, 1400], linestyle = :dash, color = :red)

num  = 5
scatter!(axs5, gpp[1:end-num]*100, gpp_5*100, markersize = 2.0)
lines!(axs5, [800, 1300], [800, 1400], linestyle = :dash, color = :red)

num  = 6
scatter!(axs6, gpp[1:end-num]*100, gpp_6*100, markersize = 2.0)
lines!(axs6, [800, 1300], [800, 1400], linestyle = :dash, color = :red)



save("../mean_met.png", f)



N = size(gpp)[1] -1

fs = 1

t0 = 0

tmax = t0+ N*fs

t = [t0:fs:tmax;]

signal = gpp

F = fft(signal)

freqs = fftfreq(length(t), fs)
freqs = fftshift(freqs)

f1 = Figure(backgroundcolor = RGBf(0.98, 0.98, 0.98),
    resolution = (1200, 600))

gt = f1[1,1] = GridLayout()
gf = f1[2,1] = GridLayout()

axt = Axis(gt[1,1])
axf = Axis(gf[1,1])

lines!(axt, t, signal)
lines!(axf,freqs, abs.(F))

save("../wave.png", f1)



# time_domain = plot(t, signal, title = "Signal")
# freq_domain = plot(freqs, abs.(F), title = "Spectrum")
# plot(time_domain, freq_domain, layout = 2)