#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from typing import Collection, Callable, Tuple

__all__ = ['top_feats_label', 'top_feats_all', 'plot_top_feats']

def top_feats_label(X: np.ndarray, features: Collection[str], label_idx: Collection[bool] = None,
                    min_val: float = 0.1, agg_func: Callable = np.mean)->pd.DataFrame:
    
  
    res = X[label_idx] if label_idx is not None else X
    res[res < min_val] = 0
    res_agg = agg_func(res, axis=0)
    df = pd.DataFrame([(features[i], res_agg[i]) for i in np.argsort(res_agg)[::-1]])
    df.columns = ['feature','score']
    df['ngram'] = df.feature.map(lambda x: len(set(x.split(' '))))
    return df

def top_feats_all(X: np.ndarray, y: np.ndarray, features: Collection[str], min_val: float = 0.1, 
                  agg_func: Callable = np.mean)->Collection[pd.DataFrame]:
   
    labels = np.unique(y)
    dfs = []
    for l in labels:
        label_idx = (y==l)
        df = top_feats_label(X,features,label_idx,min_val,agg_func).reset_index()
        df['label'] = l
        df.columns = ['rank','feature','score','ngram','label']
        dfs.append(df)
    return dfs

def plot_top_feats(dfs: Collection[pd.DataFrame], top_n: int = 25, ngram_range: Tuple[int,int]=(1,2),)-> None:
    
    fig = plt.figure(figsize=(12, 9), facecolor="w")
    x = np.arange(top_n)
    for i, df in enumerate(dfs):
        df = df[(df.ngram>=ngram_range[0])&(df.ngram<=ngram_range[1])][:top_n]
        ax = fig.add_subplot(1, len(dfs), i+1)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.set_frame_on(False)
        ax.get_xaxis().tick_bottom()
        ax.get_yaxis().tick_left()
        ax.set_xlabel("score", labelpad=16, fontsize=14)
        ax.set_title(f"label = {str(df.label[0])}", fontsize=16)
        ax.ticklabel_format(axis='x', style='sci', scilimits=(-2,2))
        ax.barh(x, df.score, align='center', color='#3F5D7D')
        ax.set_yticks(x)
        ax.set_ylim([-1, x[-1]+1])
        ax.invert_yaxis()
        yticks = ax.set_yticklabels(df.feature)
        plt.subplots_adjust(bottom=0.09, right=0.97, left=0.15, top=0.95, wspace=0.52)
    plt.show()


# In[ ]:




