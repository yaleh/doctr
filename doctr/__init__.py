"""
DocTr: Document Image Transformer for Geometric Unwarping and Illumination Correction
"""

from .GeoTr import GeoTr
from .IllTr import IllTr
from .seg import U2NETP
from .inference import rec, GeoTr_Seg, reload_model, reload_segmodel

__version__ = "0.1.0"