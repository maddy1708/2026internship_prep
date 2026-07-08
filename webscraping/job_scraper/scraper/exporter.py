import pandas as pd

def save_csv(jobs):

    df = pd.DataFrame(jobs)

    df.to_csv("data/jobs.csv", index=False)
