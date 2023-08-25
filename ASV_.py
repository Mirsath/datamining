import scanpy as sc
import anndata as ad
import numpy as np


def calculate_asv_metrics(adata):
    sc.pp.calculate_qc_metrics(adata ,percent_top=None, log1p=False, inplace=True) 
    return

def plt_highest_expr_asv(adata2, num):
    sc.pl.highest_expr_genes(adata2, n_top=num)
    return

def normalize_per_sample(adata, target_sum):
    sc.pp.normalize_per_cell(adata, counts_per_cell_after = target_sum)
    return