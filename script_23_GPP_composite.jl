using HDF5
using CairoMakie
using Statistics
using FFTW
using DSP

ENV["GKSwstype"] = "100"

DATA_FOLDER = "/p/project/hai_deep_c/project_data/forest-carbon-flux/ml_data/"

num_files = 10

met = Array{Float64}(undef, 9000*num_files, 365, 3)

gpp = Array{Float64}(undef, 9000*num_files,)


for i=1:num_files
    fid = h5open(DATA_FOLDER*"data_100ha_$(i-1).h5", "r") 
    x = fid["X"]
    y = fid["Y"]

    met[(i-1)*9000+1:i*9000, :,1] = permutedims(x["irradiance"][:,:], (2, 1))
    met[(i-1)*9000+1:i*9000, :,2] = permutedims(x["rain"][:,:], (2, 1))
    met[(i-1)*9000+1:i*9000, :,3] = permutedims(x["temperature"][:,:], (2, 1))


    gpp[(i-1)*9000+1:i*9000] = y["GPP"][:]
    
end

X = Array{Float64}(undef, 9000*num_files-3, 365*4, 3)

Y = Array{Float64}(undef, 9000*num_files-3)

for i=1:size(gpp)[1]-3
    X[i, :, 1] = vec(permutedims(met[i:i+3, :, 1], (2,1)))
    X[i, :, 2] = vec(permutedims(met[i:i+3, :, 2], (2,1)))
    X[i, :, 3] = vec(permutedims(met[i:i+3, :, 3], (2,1)))

    Y[i] = gpp[i+3]
end


mean_met = mean(X, dims = 1)


set_theme!(theme_light())


mgp = mean(gpp)*100

gpp_5p = quantile(gpp, 0.05)*100

met_low_4 = X[(Y*100).<gpp_5p,:,:]


met_not_low_4 = X[(Y*100).>=gpp_5p,:,:]

mean_low = mean(met_low_4, dims = 1)
std_low = std(met_low_4, dims = 1)

mean_not_low = mean(met_not_low_4, dims = 1)
std_not_low = std(met_not_low_4, dims = 1)


f = Figure(backgroundcolor = RGBf(0.98, 0.98, 0.98),
    resolution = (4000, 1200))

gi = f[1,1:4] = GridLayout()
gp = f[2,1:4] = GridLayout()
gt = f[3,1:4] = GridLayout()
gg = f[1:3,5:7] = GridLayout()

gai = f[4, 1:7] = GridLayout()
gap = f[5, 1:7] = GridLayout()
gat = f[6, 1:7] = GridLayout()

axai = Axis(gai[1,1])
axap = Axis(gap[1,1])
axat = Axis(gat[1,1])

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

x = [1:365*4;]

band!(axai, x, mean_not_low[1, :, 1]-mean_met[1, :, 1] - std_low[1, :, 1], mean_not_low[1, :, 1]-mean_met[1, :, 1] + std_not_low[1, :, 1], color = (:slategray2), label = "not_low +/- 1 std"  )
band!(axai, x, mean_low[1, :, 1]-mean_met[1, :, 1] - std_low[1, :, 1], mean_low[1, :, 1]-mean_met[1, :, 1] + std_low[1, :, 1], color = (:brown1, 0.4), label = "low +/- 1 std" )
lines!(axai, mean_low[1, :, 1]-mean_met[1, :, 1], label = "mean low", color = :yellow)


band!(axap, x, mean_not_low[1, :, 2]-mean_met[1, :, 2] - std_low[1, :, 2], mean_not_low[1, :, 2]-mean_met[1, :, 2] + std_not_low[1, :, 2], color = (:slategray2), label = "not_low +/- 1 std" )
band!(axap, x, mean_low[1, :, 2]-mean_met[1, :, 2] - std_low[1, :, 2], mean_low[1, :, 2]-mean_met[1, :, 2] + std_low[1, :, 2], color = (:brown1, 0.4), label = "low +/- 1 std" )
lines!(axap, mean_low[1, :, 2]-mean_met[1, :, 2], label = "mean low", color = :blue)


band!(axat, x, mean_not_low[1, :, 3]-mean_met[1, :, 3] - std_low[1, :, 3], mean_not_low[1, :, 3]-mean_met[1, :, 3] + std_not_low[1, :, 3], color = (:slategray2), label = "not_low +/- 1 std")
band!(axat, x, mean_low[1, :, 3]-mean_met[1, :, 3] - std_low[1, :, 3], mean_low[1, :, 3]-mean_met[1, :, 3] + std_low[1, :, 3], color = (:brown1, 0.4), label = "low +/- 1 std")
lines!(axat, mean_low[1, :, 3]-mean_met[1, :, 3], label = "mean low", color = :green)

axislegend(axai, merge = true)
axislegend(axap, merge = true)
axislegend(axat, merge = true)


# lines!(axat, mean_low[1, :, 3]-mean_met[1, :, 3] + std_low[1, :, 3], label = "+ 1 std deviation")



# lines!(axap, mean_not_low[1, :, 2]-mean_met[1, :, 2], label = "not_low")
# lines!(axat, mean_not_low[1, :, 3]-mean_met[1, :, 3], label = "not_low")



for i=1:5

    w = 8+3*(i-1)
    
    s1 = f[1:3, w:w+2] = GridLayout()
    s2 = f[4:6, w:w+2] = GridLayout()

    axs1 = Axis(s1[1,1], xlabel = "GPP | t year", ylabel = "GPP | t-$i year")
    axs2 = Axis(s2[1,1], xlabel = "GPP | t year", ylabel = "GPP | t-$(i+1) year")
   

    n  = 2*(i)-1
    scatter!(axs1, gpp[1:end-n]*100, gpp[1+n:end]*100, markersize = 2.0)
    lines!(axs1, [800, 1400], [800, 1400], linestyle = :dash, color = :black)
    vlines!(axs1, gpp_5p, label = "5th perc $(round(gpp_5p,digits =2))", linestyle = :dash, color = :red)
    hlines!(axs1, gpp_5p, label = "5th perc $(round(gpp_5p,digits =2))", linestyle = :dash, color = :red)

    n  = 2*(i)
    scatter!(axs2, gpp[1:end-n]*100, gpp[1+n:end]*100, markersize = 2.0)
    lines!(axs2, [800, 1400], [800, 1400], linestyle = :dash, color = :red)

    vlines!(axs2, gpp_5p, label = "5th perc $(round(gpp_5p,digits =2))", linestyle = :dash, color = :red)
    hlines!(axs2, gpp_5p, label = "5th perc $(round(gpp_5p,digits =2))", linestyle = :dash, color = :red)
end


# save("../mean_met.pdf", f, px_per_unit = 2)

save("../mean_met.png", f)



# N = size(gpp)[1] -1

# fs = 1

# t0 = 0

# tmax = t0+ N*fs

# t = [t0:fs:tmax;]

# signal = gpp

# F = fft(signal)

# freqs = fftfreq(length(t), fs)
# freqs = fftshift(freqs)

# f1 = Figure(backgroundcolor = RGBf(0.98, 0.98, 0.98),
#     resolution = (1200, 600))

# gt = f1[1,1] = GridLayout()
# gf = f1[2,1] = GridLayout()

# axt = Axis(gt[1,1])
# axf = Axis(gf[1,1])

# lines!(axt, t, signal)
# lines!(axf,freqs, abs.(F))

# save("../wave.png", f1)



# time_domain = plot(t, signal, title = "Signal")
# freq_domain = plot(freqs, abs.(F), title = "Spectrum")
# plot(time_domain, freq_domain, layout = 2)