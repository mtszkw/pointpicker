"""Image Annotator

Usage:
  annotate.py <images_dir>
  annotate.py (-h | --help)
  annotate.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.
"""

import pandas as pd
from docopt import docopt

from annotation import DirectoryReader
from annotation.annotators import PointAnnotator

if __name__ == '__main__':
    arguments = docopt(__doc__, version='Point Annotator 0.1')
 
    # D:/GitLab/simplecalib/test/test_data/calibration/test_data/BLK2GO_invalid_masks_number/01/
    reader = DirectoryReader(images_dir=arguments['<images_dir>'])
    annotator = PointAnnotator()

    for img_absolute_path in reader.all():
        points = annotator.run(img_absolute_path)
        print(f'Annotated points ({len(points)}): {points}')

        # ground_truth_dir = os.path.join(reader.base_path, 'annotations')
        # if not os.path.exists(ground_truth_dir):
            # os.mkdir(ground_truth_dir)
        # full_gt_path = os.path.join(ground_truth_dir, img_filename.split('.')[0] + '.csv')
        # df_points = pd.DataFrame(centroids)
        # df_points.to_csv(full_gt_path, header=False, index=False)
