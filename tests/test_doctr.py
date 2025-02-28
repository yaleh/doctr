#!/usr/bin/env python
"""
Test script for DocTr package
"""

# Import components from the package
try:
    from doctr import GeoTr, IllTr, U2NETP, GeoTr_Seg, rec

    # Check if modules were imported properly
    print("Successfully imported GeoTr:", GeoTr)
    print("Successfully imported IllTr:", IllTr)
    print("Successfully imported U2NETP:", U2NETP)
    print("Successfully imported GeoTr_Seg:", GeoTr_Seg)
    print("Successfully imported rec function:", rec)
    
    print("\nDocTr package is working correctly!")
except ImportError as e:
    print(f"Error importing from doctr package: {e}") 