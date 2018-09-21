# This script is part of the workflow to assess
# navigability in the Baro-Akobo-Sobat region
# 
# Project carried out by HYDROC GmbH, 2018-2019 
# for the World Food Programme
#
# Authors: 
# Jens Kiesel - jenskiesel@gmail.com
# Claas Faber - claas.faber@posteo.de
#
# 
# This script:
# - connects to ...
# - moves the previous files to the Archive
# - downloads the new files since last download
# - saves the files in the RawClimateData folder
#
# Python 3.6.6

# -------
# IMPORTS
# -------
import os


# ------
# INPUTS
# ------
URL_str = ""
cur_dir_str = os.path.dirname(os.path.abspath(__file__))  # get current path, may not work when compiling to an exe
archive_path_str = os.path.join(cur_dir_str, "RawClimateData", "Archive", "TMP")
out_path_str = os.path.join(cur_dir_str, "RawClimateData", "TMP")
