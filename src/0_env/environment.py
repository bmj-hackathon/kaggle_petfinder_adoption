#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 10:32:09 2018

@author: batman
"""

#%% ===========================================================================
# Standard imports
# =============================================================================
import os
import yaml
from pathlib import Path
import sys
import zipfile
from datetime import datetime

#%% ===========================================================================
# ML imports
# =============================================================================
import pandas as pd

#%% ===========================================================================
# Logging
# =============================================================================
import logging
#Delete Jupyter notebook root logger handler
logger = logging.getLogger()
logger.handlers = []

# Set level
logger.setLevel(logging.DEBUG)

# Create formatter
#FORMAT = "%(asctime)s - %(levelno)-3s - %(module)-10s  %(funcName)-10s: %(message)s"
#FORMAT = "%(asctime)s - %(levelno)-3s - %(funcName)-10s: %(message)s"
#FORMAT = "%(asctime)s - %(funcName)-10s: %(message)s"
FORMAT = "%(asctime)s : %(message)s"
DATE_FMT = "%Y-%m-%d %H:%M:%S"
#DATE_FMT = "%H:%M:%S"
formatter = logging.Formatter(FORMAT, DATE_FMT)

# Create handler and assign
handler = logging.StreamHandler(sys.stderr)
handler.setFormatter(formatter)
logger.handlers = [handler]
logging.debug("Logging started")

# %% Globals
#
# LANDSCAPE_A3 = (16.53, 11.69)
# PORTRAIT_A3 = (11.69, 16.53)
# LANDSCAPE_A4 = (11.69, 8.27)

PATH_DATA_ROOT = r"~/DATA/petfinder_adoption"
SAMPLE_FRACTION = 0.5
# PATH_OUT = r"/home/batman/git/hack_sfpd1/Out"
# PATH_OUT_KDE = r"/home/batman/git/hack_sfpd1/out_kde"
# PATH_REPORTING = r"/home/batman/git/hack_sfpd1/Reporting"
# PATH_MODELS = r"/home/batman/git/hack_sfpd4/models"
# TITLE_FONT = {'fontname': 'helvetica'}


# TITLE_FONT_NAME = "Arial"
# plt.rc('font', family='Helvetica')
