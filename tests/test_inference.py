import unittest
import os
import shutil
from doctr.inference import rec  # Assuming 'rec' is the function you want to test
from PIL import Image  # Import PIL for image creation
import numpy as np # Import numpy for creating image data

class TestInference(unittest.TestCase):
    def setUp(self):
        # Create dummy directories and files for testing
        self.test_dir = 'test_tmp_doctr'
        self.distorted_path = os.path.join(self.test_dir, 'distorted/')
        self.geo_rec_path = os.path.join(self.test_dir, 'geo_rec/')
        self.ill_rec_path = os.path.join(self.test_dir, 'ill_rec/')
        os.makedirs(self.distorted_path, exist_ok=True)
        os.makedirs(self.geo_rec_path, exist_ok=True)
        os.makedirs(self.ill_rec_path, exist_ok=True)

        # Create a dummy image file
        image_array = np.zeros((10, 10, 3), dtype=np.uint8) # Create a small black image array
        dummy_image = Image.fromarray(image_array) # Create a PIL Image from the array
        dummy_image.save(os.path.join(self.distorted_path, 'test_image.png')) # Save as PNG

    def tearDown(self):
        # Clean up dummy directories and files
        shutil.rmtree(self.test_dir)

    def test_rec_function(self):
        class Options:
            def __init__(self, distorted_path, gsave_path, isave_path, Seg_path, GeoTr_path, IllTr_path, ill_rec):
                self.distorrted_path = distorted_path
                self.gsave_path = gsave_path
                self.isave_path = isave_path
                self.Seg_path = Seg_path
                self.GeoTr_path = GeoTr_path
                self.IllTr_path = IllTr_path
                self.ill_rec = ill_rec

        opt = Options(
            distorted_path=self.distorted_path,
            gsave_path=self.geo_rec_path,
            isave_path=self.ill_rec_path,
            Seg_path='./model_pretrained/seg.pth', # You might need dummy model paths
            GeoTr_path='./model_pretrained/geotr.pth',
            IllTr_path='./model_pretrained/illtr.pth',
            ill_rec=False
        )

        try:
            rec(opt)
            self.assertTrue(True) # If rec function runs without error, pass the test
            # Add more assertions here to check for expected outputs if needed
            # For example, check if output files are created in geo_rec_path and ill_rec_path
        except Exception as e:
            self.fail(f"rec function raised an exception: {e}")

if __name__ == '__main__':
    unittest.main() 