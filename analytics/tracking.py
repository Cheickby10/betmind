import pandas as pd

def log_session(file,entry):
    df=pd.DataFrame([entry])
    try:
        old=pd.read_csv(file)
        df=pd.concat([old,df])
    except:
        pass
    df.to_csv(file,index=False)
