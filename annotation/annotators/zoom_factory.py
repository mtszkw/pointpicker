import matplotlib.pyplot as plt

# https://stackoverflow.com/questions/11551049/matplotlib-plot-zooming-with-scroll-wheel
def zoom_factory(ax, base_scale = 2.):
    def zoom_fun(event):
        cur_xlim = ax.get_xlim()
        cur_ylim = ax.get_ylim()
        cur_xrange = (cur_xlim[1] - cur_xlim[0])*.5
        cur_yrange = (cur_ylim[1] - cur_ylim[0])*.5
        xdata = event.xdata # get event x location
        ydata = event.ydata # get event y location
        if event.button == 'down':
            # deal with zoom in
            scale_factor = 1/base_scale
        elif event.button == 'up':
            # deal with zoom out
            scale_factor = base_scale
        else:
            # deal with something that should never happen
            scale_factor = 1
        # set new limits
        ax.figure.canvas.toolbar.push_current()
        ax.set_xlim([xdata - (xdata-cur_xlim[0]) / scale_factor, xdata + (cur_xlim[1]-xdata) / scale_factor])
        ax.set_ylim([ydata - (ydata-cur_ylim[0]) / scale_factor, ydata + (cur_ylim[1]-ydata) / scale_factor])
        plt.draw() # force re-draw
    fig = ax.get_figure() # get the figure of interest
    # attach the call back
    fig.canvas.mpl_connect('scroll_event',zoom_fun)
    #return the function
    return zoom_fun