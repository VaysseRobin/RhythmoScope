from rythmoscope.envelope import Envelope
import numpy.typing as npt
from typing import Union


class RhythmSpectrogram:
    """
    Object

        Args:
            sr (int): Sampling rate of the signal
            signal (npt.ArrayLike[int | float]): A one dimentional array containing the raw values
                                                 of the signal.

    """

    def __init__(
        self, sr: int, signal: npt.ArrayLike[Union[int, float]], Envelope: Envelope
    ) -> None:
        pass
