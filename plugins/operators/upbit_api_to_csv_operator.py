from airflow.models.baseoperator import BaseOperator
from airflow.hooks.base import BaseHook
import pandas as pd 

class UpbitApiToCsvOperator(BaseOperator):
    template_fields = ()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def execute(self, context):
        import requests
        from urllib.request import urlopen
        import json 

        request_url = "https://api.upbit.com/v1/candles/minutes/1?market=KRW-BTC&count=5"

        try:
            headers = {"accept": "application/json"}

            response = requests.get(request_url, headers)
            contents = json.loads(response.text)

            row_df = pd.DataFrame(contents)

        except:
            page = urlopen(request_url)

            doc = page.read().decode('utf-8')
            dic = json.loads(doc)
            row_df = pd.DataFrame(dic)

        self.log.info(row_df)