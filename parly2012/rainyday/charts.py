class LineChart:
    def __init__(self, width, height, legend, xlegend, ylegend, series, xlabels = None, spready=False):
        self.style = 'line'
        self.legend = legend
        self.xlegend = xlegend
        self.ylegend = ylegend
        self.width = width
        self.height = height
        self.xmax = max([max([item[0] for item in s]) for s in series])
        self.xmin = min([min([item[0] for item in s]) for s in series])
        self.ymax = max([max([item[1] for item in s]) for s in series])
        if spready:
            self.ymin = min([min([item[1] for item in s]) for s in series])
        else:
            self.ymin = 0
        self.gll = self.point_to_xy((self.xmin, self.ymin))
        self.glr = self.point_to_xy((self.xmax, self.ymin))
        if xlabels:
            self.xlabels = []
            for idx, l in enumerate(xlabels):
                lxy = self.point_to_xy(
                    (
                        idx * (self.xmax - self.xmin) / (len(xlabels) - 1),
                        -((self.ymax - self.ymin)/20)
                    )
                )
                self.xlabels.append({
                    'pos': lxy,
                    'label': l
                })
        else:
            self.xminlabelxy = self.point_to_xy((self.xmin, -((self.ymax - self.ymin)/20)))
            self.xmaxlabelxy = self.point_to_xy((self.xmax, -((self.ymax - self.ymin)/20)))
            self.xminlabel = str(self.xmin)
            self.xmaxlabel = str(self.xmax)
            self.xlabelxy = self.point_to_xy(((self.xmin + self.xmax) / 2, -((self.ymax - self.ymin)/20)))
            self.xlabel = self.xlegend
        colours = ["red", "green", "blue", "yellow", "magenta"]
        paths = [self.path(s) for s in series]
        self.series = [{'colour': c, 'path': p} for c, p in zip(colours, paths)]
    
    def path(self, series):
        d = "M{0}, {1}".format(*self.point_to_coord(series[0]))
        for v in series[1:]:
            l = "L{0} {1}".format(*self.point_to_coord(v))
            d = "{0}{1}".format(d, l)
        return d
    
    def point_to_xy(self, v):
        c = self.point_to_coord(v)
        return {
            'x': c[0],
            'y': c[1]
        }
        
    def point_to_coord(self, v):
        return [
            0.1 * self.width + v[0] * 0.8 * self.width / (self.xmax - self.xmin),
            ((self.ymax - self.ymin) - v[1]) * 0.9 * self.height / (self.ymax - self.ymin)
        ]
        
