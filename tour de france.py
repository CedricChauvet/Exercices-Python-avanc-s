import pandas as pd
import altair as alt
#from pathlib import Path

dir = "C:/Users/chauv/OneDrive/Documents/Python Scripts/"
df = pd.read_csv(dir +"tour_de_france.csv",parse_dates=["timestamp"])
#print(df)
alt.Chart(df.sample(1000)).encode(
    alt.X("timestamp",title=None, axis = alt.Axis(format = "d %b"))).mark_point()

c = alt.Chart(df.assign( timestamp_diff = lambda df : df.timestamp.diff().dt.total_seconds()).query("timestamp_diff > 3600")).encode(alt.X("timestamp_diff",bin = alt.Bin(maxbins = 30), title = "Intervalle (en heures) sas données",),alt.Y("count()",title = None),).mark_bar()


from typing import Iterator

def itere_trajectoires(data: pd.DataFrame) -> Iterator[pd.DataFrame]:
    df = data.sort_values("timestamp").assign(timestamp_diff = lambda df: df.timestamp.diff().dt.total_seconds())
    seuil = df.query("timestamp_diff > 3600")
    if seuil.shape[0]==0:
        return df
    else:
        yield df.query("timestamp < @seuil.timestamp.min()")
        yield from itere_trajectoires(df.query("timestamp >= @seuil.timestamp.min()"))

print(sum(1 for _ in itere_trajectoires(df)))


from cartopy.crs import PlateCarree

class Trajectoire:
    def __init__(self, data: pd.DataFrame):
        self.data=data

    @property
    def start(self) -> pd.Timestamp:
        return self.data.timestamp.min()
    
    @property
    def stop(self) -> pd.Timestamp:
        return self.data.timestamp.max()
    
    @property
    def duree(self) -> pd.Timedelta:
        return self.stop - self.start
    
    def plot(self,ax,**kwargs):
        return self.data.plot( ax = ax, x="longitude",y="latitude",legend=False,transform = PlateCarree(),**kwargs)
    
class Collection:
    def __init__(self, data: pd.DataFrame):
        self.data=data

    def __iter__(self) -> Iterator[Trajectoire]:
        df = self.data.sort_values("timestamp").assign(timestamp_diff = lambda df: df.timestamp.diff().dt.total_seconds())
        seuil = df.query("timestamp_diff > 3600")
        if seuil.shape[0] == 0:
            return Trajectoire(self.data)
        else:
            yield Trajectoire(df.query("timestamp < @seuil.timestamp.min()"))
            yield from Collection(df.query("timestamp >= @seuil.timestamp.min()"))
    def __len__(self):
        return sum(1 for _ in self)
    

print(pd.DataFrame.from_records(
    {"start" : traj.start, "stop" : traj.stop, "durée" : traj.duree} for traj in Collection(df)
))


import matplotlib.pyplot as plt
from cartes.crs import Lambert93

fig,ax =plt.subplots(
    figsize=(7,7), subplot_kw=dict(projection=Lambert93())
)

ax.coastlines("50m")



for trajectoire in Collection(df):
    trajectoire.plot(ax=ax)

plt.show()