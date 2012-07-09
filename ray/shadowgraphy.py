import itertools

import numpy as np
import yt.mods

from . import yt_derived_fields


class Shadowgraphy(object):

    def __init__(self, filename, field='nele', resolution=(800, 600)):
        self.filename = filename
        self.field = field 
        self.resolution = resolution

    def simulate(self):
        pf = yt.mods.load(self.filename)
        irange = np.linspace(pf.domain_left_edge[0], pf.domain_right_edge[0], self.resolution[0])
        jrange = np.linspace(pf.domain_left_edge[1], pf.domain_right_edge[1], self.resolution[1])
        i, j = np.meshgrid(irange, jrange)
        raybeg = np.array((i, j, pf.domain_left_edge[2] * np.ones_like(i))).T
        rayend = np.array((i, j, pf.domain_right_edge[2] * np.ones_like(i))).T

        img = np.empty(self.resolution, dtype=float)
        img.fill(np.nan)

        for ind, jnd in itertools.product(range(self.resolution[0]), range(self.resolution[1])):
            img[ind,jnd] = self._render_ray(raybeg[ind,jnd], rayend[ind,jnd])

        print img
        print img.shape

    def _render_ray(self, coord0, coord1):
        return 42.0
