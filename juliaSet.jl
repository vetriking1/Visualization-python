using GLMakie
using Colors

# Set up the initial parameters
fig = Figure(Scene=(800, 800))
ax = Axis(fig[1, 1])

# Function to calculate Julia set
function julia(z, c, max_iter)
    for n in 1:max_iter
        if abs(z) > 2
            return n
        end
        z = z * z + c
    end
    return max_iter
end

# Function to draw the Julia set
function draw_julia(xmin, xmax, ymin, ymax, width, height, max_iter, c)
    x = LinRange(xmin, xmax, width)
    y = LinRange(ymin, ymax, height)

    julia_set_values = zeros(Int, height, width)

    for i in 1:height
        for j in 1:width
            z = complex(x[j], y[i])
            julia_set_values[i, j] = julia(z, c, max_iter)
        end
    end

    return julia_set_values, x, y
end

# Initial plot
realX, imgY = 0.0, 0.0
image_j, x, y = draw_julia(-2.0, 2.0, -2.0, 2.0, 8000, 8000, 200, complex(realX, imgY))

img_plot = image!(ax, x, y, image_j; colormap=:viridis)
ax.title = "Julia Set"
ax.xlabel = "Re"
ax.ylabel = "Im"
xlims!(ax, -2.0, 2.0)
ylims!(ax, -2.0, 2.0)

# Slider setup
slider_real = Slider(fig[2, 1], range=-2:0.01:2, startvalue=realX)
slider_img = Slider(fig[3, 1], range=-2:0.01:2, startvalue=imgY)

# Update function
function update!()
    realX = slider_real.value[]
    imgY = slider_img.value[]
    c = complex(realX, imgY)
    image_j, _, _ = draw_julia(-2.0, 2.0, -2.0, 2.0, 8000, 8000, 200, c)
    img_plot[1] = image!(ax, x, y, image_j; colormap=:viridis)[1]
end

# Connect sliders to update function
on(slider_real.value) do _
    update!()
end

on(slider_img.value) do _
    update!()
end

fig
