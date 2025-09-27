from datetime import datetime
from collections.abc import Mapping
from enum import Enum
from math import exp, log


class InterpolationMethod(Enum):
    LINEAR = 'linear'
    STEP = 'step'
    LOG_LINEAR = 'log_linear'

def interpolate(d: datetime, d_1: datetime, v_1: float, d_2: datetime, v_2: float,
                method: InterpolationMethod = InterpolationMethod.LINEAR) -> float:
    """
    Interpolate the value at date `d` given two known points (d_1, v_1) and (d_2, v_2)
    using the specified interpolation method.
    :param d: The date at which to interpolate the value.
    :param d_1: The first known date.
    :param v_1: The value at the first known date.
    :param d_2: The second known date.
    :param v_2: The value at the second known date.
    :param method: The interpolation method to use (linear, step, log-linear).
    :return: The interpolated value at date `d`."""
    match(method):
        case InterpolationMethod.LINEAR:
            return v_1 + (v_2 - v_1) * (d - d_1).days / (d_2 - d_1).days
        case InterpolationMethod.STEP:
            return v_1
        case InterpolationMethod.LOG_LINEAR:
            return exp(log(v_1) + (log(v_2) - log(v_1)) * (d - d_1).days / (d_2 - d_1).days)
    raise ValueError(f"Unknown interpolation method: {method}")

class Curve:
    def __init__(self, nodes: Mapping[datetime, float], interpolation: InterpolationMethod = InterpolationMethod.LINEAR):
        """
        Initialize a Curve with given nodes and interpolation method.

        :param nodes: A mapping of x-coordinates to y-coordinates.
        :param interpolation: The interpolation method to use ('linear', 'step', etc.).
        """
        self.nodes = dict(nodes.items())
        self.node_dates = list(self.nodes.keys())
        self.interpolation = interpolation
    
    def __repr__(self):
        return f"Curve(nodes={self.nodes}, interpolation='{self.interpolation}')"
    
    def __getitem__(self, date: datetime):
        # Check if date is out of bounds
        if date <= self.node_dates[0] or date >= self.node_dates[-1]:
            raise ValueError(f"Date {date!r} is out of the bounds of the curve nodes.")
        # Check if date matches a node
        if date in self.nodes:
            return self.nodes[date]
        # Interpolate between the two surrounding nodes
        for i, node_date in enumerate(self.node_dates[1:]):
            if date <= node_date:
                node_date_0 = self.node_dates[i-1]
                return interpolate(date, node_date_0, self.nodes[node_date_0],
                                   node_date, self.nodes[node_date], self.interpolation)
