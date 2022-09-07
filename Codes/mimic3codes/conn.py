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

print("connected!")

# admissions = pd.read_sql("select * from mimic3.admissions", engine)
# callout = pd.read_sql("select * from mimic3.callout", engine)
# caregivers = pd.read_sql("select * from mimic3.caregivers", engine)
# #chartevents = pd.read_sql("select * from mimic3.chartevents", engine)
# chartevents_1 = pd.read_sql("select * from mimic3.chartevents_1", engine)
# chartevents_2 = pd.read_sql("select * from mimic3.chartevents_2", engine)
# chartevents_3 = pd.read_sql("select * from mimic3.chartevents_3", engine)
# chartevents_4 = pd.read_sql("select * from mimic3.chartevents_4", engine)
# chartevents_5 = pd.read_sql("select * from mimic3.chartevents_5", engine)
# chartevents_6 = pd.read_sql("select * from mimic3.chartevents_6", engine)
# chartevents_7 = pd.read_sql("select * from mimic3.chartevents_7", engine)
# chartevents_8 = pd.read_sql("select * from mimic3.chartevents_8", engine)
# chartevents_9 = pd.read_sql("select * from mimic3.chartevents_9", engine)
# chartevents_10 = pd.read_sql("select * from mimic3.chartevents_10", engine)
# chartevents_11 = pd.read_sql("select * from mimic3.chartevents_11", engine)
# chartevents_12 = pd.read_sql("select * from mimic3.chartevents_12", engine)
# chartevents_13 = pd.read_sql("select * from mimic3.chartevents_13", engine)
# chartevents_14 = pd.read_sql("select * from mimic3.chartevents_14", engine)
# chartevents_15 = pd.read_sql("select * from mimic3.chartevents_15", engine)
# chartevents_16 = pd.read_sql("select * from mimic3.chartevents_16", engine)
# chartevents_17 = pd.read_sql("select * from mimic3.chartevents_17", engine)
# cptevents = pd.read_sql("select * from mimic3.cptevents", engine)
# d_cpt = pd.read_sql("select * from mimic3.d_cpt", engine)
# d_icd_diagnoses = pd.read_sql("select * from mimic3.d_icd_diagnoses", engine)
# d_icd_precedures = pd.read_sql("select * from mimic3.d_icd_precedures", engine)
# d_items = pd.read_sql("select * from mimic3.d_items", engine)
# d_labitems = pd.read_sql("select * from mimic3.d_labitems", engine)
# datetimeevents = pd.read_sql("select * from mimic3.datetimeevents", engine)
# diagnoses_icd = pd.read_sql("select * from mimic3.diagnoses_icd", engine)
# drgcodes = pd.read_sql("select * from mimic3.drgcodes", engine)
# icustays = pd.read_sql("select * from mimic3.icustays", engine)
# inputevents_cv = pd.read_sql("select * from mimic3.inputevents_cv", engine)
# inputevents_mv = pd.read_sql("select * from mimic3.inputevents_mv", engine)
# labevents = pd.read_sql("select * from mimic3.labevents", engine)
# microbiologyevents = pd.read_sql("select * from mimic3.microbiologyevents", engine)
# noteevents = pd.read_sql("select * from mimic3.noteevents", engine)
# outputevents = pd.read_sql("select * from mimic3.outputevents", engine)
# patients = pd.read_sql("select * from mimic3.patients", engine)
# prescriptions = pd.read_sql("select * from mimic3.prescriptions", engine)
# procedureevents_mv = pd.read_sql("select * from mimic3.procedureevents_mv", engine)
# procedures_icd = pd.read_sql("select * from mimic3.procedures_icd", engine)
# services = pd.read_sql("select * from mimic3.services", engine)
# transfers = pd.read_sql("select * from mimic3.transfers", engine)