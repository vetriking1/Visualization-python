using GLMakie
using Colors

# Define the function to compute the Mandelbrot set
function mandelbrot(c, max_iter)
    z = 0.0 + 0.0im
    for n in 1:max_iter
        if abs(z) > 2
            return n
        end
        z = z^2 + c
    end
    return max_iter
end

# Function to draw the Mandelbrot set
function draw_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter)
    x = LinRange(xmin, xmax, width)
    y = LinRange(ymin, ymax, height)

    mandelbrot_set_values = zeros(Int, height, width)

    for i in 1:height
        for j in 1:width
            c = complex(x[j], y[i])
            mandelbrot_set_values[i, j] = mandelbrot(c, max_iter)
        end
    end

    return mandelbrot_set_values, (xmin, xmax), (ymin, ymax)
end

@time begin
    fig = Figure(Scene=(800, 800))
    ax = Axis(fig[1, 1])

    # Generate the Mandelbrot set
    xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
    width, height = 10000, 10000
    max_iter = 200

    mandelbrot_set_values, x_range, y_range = draw_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter)

    image!(ax, mandelbrot_set_values; colormap=:viridis)
    # Create scatter plot
    ax.title = "Mandelbrot Set"
    ax.xlabel = "Re"
    ax.ylabel = "Im"
end
fig
