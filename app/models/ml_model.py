from io import StringIO
import os
import joblib
import numpy as np
import pandas as pd
import xgboost


class MLModel:

    def __init__(self):
        target_cols = ['ind_ahor_fin_ult1', 'ind_aval_fin_ult1', 'ind_cco_fin_ult1', 'ind_cder_fin_ult1',
                       'ind_cno_fin_ult1', 'ind_ctju_fin_ult1', 'ind_ctma_fin_ult1', 'ind_ctop_fin_ult1',
                       'ind_ctpp_fin_ult1', 'ind_deco_fin_ult1', 'ind_deme_fin_ult1', 'ind_dela_fin_ult1',
                       'ind_ecue_fin_ult1', 'ind_fond_fin_ult1', 'ind_hip_fin_ult1', 'ind_plan_fin_ult1',
                       'ind_pres_fin_ult1', 'ind_reca_fin_ult1', 'ind_tjcr_fin_ult1', 'ind_valo_fin_ult1',
                       'ind_viv_fin_ult1', 'ind_nomina_ult1', 'ind_nom_pens_ult1', 'ind_recibo_ult1']
        self.target_cols = target_cols[2:]

    def predict(self, data):
        xgtest = xgboost.DMatrix(data)
        preds = self.model.predict(xgtest)

        target_cols = np.array(self.target_cols)
        preds = np.argsort(preds, axis=1)
        preds = np.fliplr(preds)[:, :7]
        return [" ".join(list(target_cols[pred])) for pred in preds]
        
   

    def load(self):
        # get the current directory
        current_dir = os.getcwd()

        # specify the filename
        filename = "model.joblib"

        # join the current directory and filename to get the absolute path
        abs_path = os.path.join(current_dir, filename)
        self.model = joblib.load(abs_path)
