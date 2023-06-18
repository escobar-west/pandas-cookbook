from functools import singledispatch
from typing import Any, Callable

import polars as pl
import seaborn as sns


def seaborn_polars(func: Callable[[Any], Any]):
    @singledispatch
    def wrapper(data: pl.DataFrame, *args, **kwargs):
        temp = data.to_pandas()
        func(temp, *args, **kwargs)
    
    @wrapper.register
    def _(data: pl.LazyFrame, *args, **kwargs):
        temp = data.collect().to_pandas()
        func(temp, *args, **kwargs)
        
    return wrapper


@seaborn_polars
def relplot(data, *args, **kwargs):
    sns.relplot(data, *args, **kwargs)

@seaborn_polars
def lineplot(data, *args, **kwargs):
    sns.lineplot(data, *args, **kwargs)    

@seaborn_polars
def scatterplot(data, *args, **kwargs):
    sns.scatterplot(data, *args, **kwargs)
    
@seaborn_polars
def displot(data, *args, **kwargs):
    sns.displot(data, *args, **kwargs)
    
@seaborn_polars
def histplot(data, *args, **kwargs):
    sns.histplot(data, *args, **kwargs)
    
@seaborn_polars
def kdeplot(data, *args, **kwargs):
    sns.kdeplot(data, *args, **kwargs)
    
@seaborn_polars
def ecdfplot(data, *args, **kwargs):
    sns.ecdfplot(data, *args, **kwargs)
    
@seaborn_polars
def rugplot(data, *args, **kwargs):
    sns.rugplot(data, *args, **kwargs)
    
@seaborn_polars
def catplot(data, *args, **kwargs):
    sns.catplot(data, *args, **kwargs)
    
@seaborn_polars
def stripplot(data, *args, **kwargs):
    sns.stripplot(data, *args, **kwargs)
    
@seaborn_polars
def swarmplot(data, *args, **kwargs):
    sns.swarmplot(data, *args, **kwargs)
    
@seaborn_polars
def boxplot(data, *args, **kwargs):
    sns.boxplot(data, *args, **kwargs)
    
@seaborn_polars
def violinplot(data, *args, **kwargs):
    sns.violinplot(data, *args, **kwargs)
    
@seaborn_polars
def boxenplot(data, *args, **kwargs):
    sns.boxenplot(data, *args, **kwargs)
    
@seaborn_polars
def pointplot(data, *args, **kwargs):
    sns.pointplot(data, *args, **kwargs)
    
@seaborn_polars
def barplot(data, *args, **kwargs):
    sns.barplot(data, *args, **kwargs)
    
@seaborn_polars
def countplot(data, *args, **kwargs):
    sns.countplot(data, *args, **kwargs)
    
@seaborn_polars
def lmplot(data, *args, **kwargs):
    sns.lmplot(data, *args, **kwargs)
    
@seaborn_polars
def regplot(data, *args, **kwargs):
    sns.regplot(data, *args, **kwargs)
    
@seaborn_polars
def residplot(data, *args, **kwargs):
    sns.residplot(data, *args, **kwargs)
    
@seaborn_polars
def heatmap(data, *args, **kwargs):
    sns.heatmap(data, *args, **kwargs)
    
@seaborn_polars
def clustermap(data, *args, **kwargs):
    sns.clustermap(data, *args, **kwargs)
    
@seaborn_polars
def pairplot(data, *args, **kwargs):
    sns.pairplot(data, *args, **kwargs)
    
@seaborn_polars
def jointplot(data, *args, **kwargs):
    sns.jointplot(data, *args, **kwargs)