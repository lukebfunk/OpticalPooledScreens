# common imports for interactive work

import os
import re
from natsort import natsorted
from collections import OrderedDict, Counter, defaultdict
from functools import partial
from glob import glob
from itertools import product

import warnings
warnings.filterwarnings("ignore", message="numpy.dtype size changed")

import numpy as np
import pandas as pd
import skimage
import scipy.stats

import ops.io
import ops.process
import ops.utils
from ops.io import BLUE, GREEN, RED, MAGENTA, GRAY, CYAN, GLASBEY 
from ops.io import grid_view
from ops.filenames import name_file as name
from ops.filenames import parse_filename as parse
from ops.filenames import timestamp
from ops.io import read_stack as read
from ops.io import save_stack as save

from ops.utils import or_join, and_join, groupby_reduce_concat, groupby_histogram
from ops.utils import pile, montage, make_tiles, trim, join_stacks

from ops.plates import add_global_xy

from ops.pool_design import reverse_complement as rc

