from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import LabelEncoder
import pandas as pd


class CatFeaturesTransformer(BaseEstimator, TransformerMixin):
    dataframe: pd.DataFrame | None = None

    def fit(self, X: pd.DataFrame) -> BaseEstimator:
        self.dataframe = X
        self.dataframe['quarter'] = self.dataframe['quarter'].replace(
            r'\d{4}Q', '', regex=True)
        scaler1 = LabelEncoder().fit(self.dataframe['region'])
        self.dataframe['region'] = scaler1.transform(self.dataframe['region'])
        return self

    def transform(self, X: None = None) -> pd.DataFrame:
        return self.dataframe


class IntegerFeaturesTransformer(BaseEstimator, TransformerMixin):
    dataframe: pd.DataFrame | None = None

    def fit(self, df: pd.DataFrame, y: None = None) -> BaseEstimator:
        self.dataframe = df
        self.dataframe['gender'] = self.dataframe['gender'].replace([1, -1],
                                                                    [1, 0])
        self.dataframe['has_communication'] = (self.dataframe['email'] == 1) |\
            (self.dataframe['phone_number'] == 1)
        self.dataframe.drop(columns=['email', 'phone_number'],
                            inplace=True)

        return self

    def transform(self, X: None = None) -> pd.DataFrame:
        return self.dataframe


def make_transformer():
    int_cols = [
        'npo_accnts_nmbr',
        'pmnts_type',
        'gender',
        'age',
        'clnt_cprtn_time_d',
        'actv_prd_d',
        'lst_pmnt_rcnc_d',
        'pmnts_nmbr',
        'pmnts_nmbr_per_qrtr',
        'pmnts_nmbr_per_year',
        'phone_number',
        'email',
        'lk',
        'assignee_npo',
        'assignee_ops',
        'citizen',
        'fact_addrss',
        'appl_mrkr',
        'evry_qrtr_pmnt'
    ]
    float_cols = [
        'balance',
        'oprtn_sum_per_qrtr',
        'oprtn_sum_per_year',
        'frst_pmnt',
        'lst_pmnt',
        'pmnts_sum',
        'pmnts_sum_per_qrtr',
        'pmnts_sum_per_year',
        'incm_sum',
        'incm_per_qrtr',
        'incm_per_year',
        'mgd_accum_period',
        'mgd_payment_period',
        'currency',
        'GDP',
        'inflation',
        'unemployment',
    ]
    cat_cols = ['quarter', 'region']
    transformer = ColumnTransformer(
        transformers=(
            ('int_trans', IntegerFeaturesTransformer(), int_cols),
            ('cat_trans', CatFeaturesTransformer(), cat_cols),
            ('float', 'passthrough', float_cols)
        )
    )

    return transformer
