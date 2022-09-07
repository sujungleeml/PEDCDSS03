#https://github.com/kieferk/dfply/blob/master/README.md#the--and--pipe-operators

import pandas as pd
from pandas import Series, DataFrame
import numpy as np
from sqlalchemy import create_engine
import pprint
from datetime import datetime, timedelta
import time
from dfply import *
import matplotlib.pyplot as plt
import seaborn as sns
import impyute as impy
from impyute.imputation.cs import mice

engine = create_engine('postgresql+psycopg2://diana:love34@160.1.17.57/mimic3')

admissions = pd.read_sql("select * from mimic3.admissions", engine)
pd.DataFrame(admissions)
icustays = pd.read_sql("select * from mimic3.icustays", engine)
pd.DataFrame(icustays)

adm = admissions >> select('subject_id','hadm_id','admittime','dischtime','deathtime','ethnicity','hospital_expire_flag')
icus = pd.read_sql("select * from mimic3.icustays", engine) >> select(~X.row_id)

nicu = icus >> left_join(adm, by = ('subject_id', 'hadm_id'))

nicu