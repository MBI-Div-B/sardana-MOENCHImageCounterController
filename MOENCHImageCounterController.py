from sardana.pool.controller import PseudoCounterController
from sardana.pool.controller import Type
import numpy as np

__all__ = ["MOENCHImageCounterController"]


class MOENCHImageCounterController(PseudoCounterController):
    counter_roles = ("moench",)

    def __init__(self, inst, props, *args, **kwargs):
        """Constructor"""
        self._log.debug("Initialize...")
        PseudoCounterController.__init__(self, inst, props, *args, **kwargs)

    def GetAxisAttributes(self, axis):
        self._log.debug("Enter GetAxisAttributes")
        axis_attrs = PseudoCounterController.GetAxisAttributes(self, axis)
        axis_attrs = dict(axis_attrs)
        axis_attrs["Value"][Type] = ((int,),)
        axis_attrs["Value"][MaxDimSize] = (400, 4000)
        return axis_attrs

    def GetAxisPar(self, axis, par):
        self._log.debug("Enter GetAxisPar")
        if par == "shape":
            return [400, 400]

    def Calc(self, axis, counter_values):
        self._log.debug("Enter Calc")
        image = np.array(counter_values[0])
        return image
