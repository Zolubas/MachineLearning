import numpy as np
import matplotlib.pyplot as plt
import sklearn as skl
import pandas as pd

adult = pd.read_csv(r"C:\Users\Fernando\Desktop\Poli Usp\4 semestre\Machine Learning\adult.csv",
        names=[
        "Age", "Workclass", "fnlwgt", "Education", "Education-Num", "Martial Status",
        "Occupation", "Relationship", "Race", "Sex", "Capital Gain", "Capital Loss",
        "Hours per week", "Country", "Target"],
        sep=r'\s*,\s*',
        engine='python',
        na_values="?")
adult.shape
adult.head() #printei o "cabecalho dos dados" para visualizar como seria a minha base de dados.
