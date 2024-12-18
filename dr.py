import umap
import pacmap
import trimap
from MulticoreTSNE import MulticoreTSNE as TSNE
from umato import UMATO
from sklearn.decomposition import PCA, FactorAnalysis, FastICA, IncrementalPCA, SparsePCA, TruncatedSVD, KernelPCA, NMF
from sklearn.manifold import MDS, Isomap, LocallyLinearEmbedding, SpectralEmbedding
from sklearn.random_projection import GaussianRandomProjection, SparseRandomProjection

import numpy as np

import _ae as ae
import _lamp as lamp
import _lmds as lmds
import _tapkee as tapkee
import _drtoolbox as drtoolbox

from scipy.spatial.distance import cdist


def run_umap(X, n_neighbors, min_dist, init):
	n_neighbors = int(n_neighbors)
	min_dist = float(min_dist)
	reducer = umap.UMAP(n_neighbors=n_neighbors, min_dist=min_dist, n_components=2, init=init)
	return reducer.fit_transform(X)

def run_pacmap(X, n_neighbors, MN_ratio, FP_ratio, init="random"):
	n_neighbors = int(n_neighbors)
	MN_ratio = float(MN_ratio)
	FP_ratio = float(FP_ratio)

	if n_neighbors * MN_ratio < 1:
		MN_ratio = 1 / n_neighbors
	if n_neighbors * FP_ratio < 1:
		FP_ratio = 1 / n_neighbors

	reducer = pacmap.PaCMAP(n_neighbors=n_neighbors, MN_ratio=MN_ratio, FP_ratio=FP_ratio)
	return reducer.fit_transform(X, init=init)

def run_trimap(X, n_inliers, n_outliers, init=None):
	n_inliers = int(n_inliers)
	n_outliers = int(n_outliers)
	reducer = trimap.TRIMAP(n_inliers=n_inliers, n_outliers=n_outliers)
	return reducer.fit_transform(X, init=init)

def run_tsne(X, perplexity, init="random"):
	perplexity = float(perplexity)
	reducer = TSNE(perplexity=perplexity, init=init)
	return reducer.fit_transform(X)

def run_umato(X, n_neighbors, min_dist, hub_num, init="pca"):
	n_neighbors = int(n_neighbors)
	min_dist = float(min_dist)
	hub_num = int(hub_num)

	reducer = UMATO(n_neighbors=n_neighbors, min_dist=min_dist, hub_num=hub_num, init="pca")
	return reducer.fit_transform(X)

def run_pca(X):
	reducer = PCA(n_components=2)
	return reducer.fit_transform(X)

def run_mds(X):
	reducer = MDS(n_components=2)
	return reducer.fit_transform(X)

def run_isomap(X, n_neighbors):
	n_neighbors = int(n_neighbors)
	reducer = Isomap(n_neighbors=n_neighbors, n_components=2, n_jobs=-1)
	return reducer.fit_transform(X)

def run_lle(X, n_neighbors):
	n_neighbors = int(n_neighbors)
	reducer = LocallyLinearEmbedding(n_neighbors=n_neighbors, n_components=2)
	return reducer.fit_transform(X)

def run_lamp(X):
	reducer = lamp.Lamp(Xdata = X)
	return reducer.fit(X)

def run_lmds(X, hub_num):
	hub_num = int(hub_num)

	emb = []
	while len(emb) == 0:
		hub_num = np.random.randint(20, X.shape[0]-2)
		hubs = np.random.choice(X.shape[0], hub_num, replace=False)
		DI = cdist(X[hubs, :], X, "euclidean")
		emb = lmds.landmark_MDS(DI, hubs, 2)
	return emb

######
def run_ae(X, model_size):
    reducer = ae.AutoencoderProjection(model_size=model_size)
    return reducer.fit_transform(X)

def run_fa(X):
    reducer = FactorAnalysis(n_components=2)
    return reducer.fit_transform(X)

def run_fica(X):
    reducer = FastICA(n_components=2)
    return reducer.fit_transform(X)

def run_grp(X):
    reducer = GaussianRandomProjection(n_components=2)
    return reducer.fit_transform(X)

def run_hlle(X, n_neighbors):
	n_neighbors = int(n_neighbors)
	reducer = LocallyLinearEmbedding(n_neighbors=n_neighbors, n_components=2, method="hessian")
	return reducer.fit_transform(X)

def run_ipca(X):
    reducer = IncrementalPCA(n_components=2)
    return reducer.fit_transform(X)

def run_kpcapol(X, degree):
    degree = int(degree)
    reducer = KernelPCA(n_components=2, kernel="poly", degree=degree)
    return reducer.fit_transform(X)

def run_kpcarbf(X):
    reducer = KernelPCA(n_components=2, kernel="rbf")
    return reducer.fit_transform(X)

def run_kpcasig(X):
    reducer = KernelPCA(n_components=2, degree=3, kernel="sigmoid")
    return reducer.fit_transform(X)

def run_ltsa(X, n_neighbors):
	n_neighbors = int(n_neighbors)
	reducer = LocallyLinearEmbedding(n_neighbors=n_neighbors, n_components=2, method="ltsa")
	return reducer.fit_transform(X)

def run_le(X):
    reducer = SpectralEmbedding(n_components=2)
    return reducer.fit_transform(X)

def run_mlle(X, n_neighbors):
	n_neighbors = int(n_neighbors)
	reducer = LocallyLinearEmbedding(n_neighbors=n_neighbors, n_components=2, method="modified")
	return reducer.fit_transform(X)

def run_nmds(X):
    reducer = MDS(n_components=2, metric=False)
    return reducer.fit_transform(X)

def run_nmf(X, init):
    reducer = NMF(n_components=2, init=init)
    return reducer.fit_transform(X)

def run_spca(X, alpha):
    alpha = float(alpha)
    reducer = SparsePCA(n_components=2, alpha=alpha)
    return reducer.fit_transform(X)

def run_srp(X):
    reducer = SparseRandomProjection(n_components=2)
    return reducer.fit_transform(X)

def run_tsvd(X):
    reducer = TruncatedSVD(n_components=2)
    return reducer.fit_transform(X)

#tapkee
def run_tapkee_dm(X, t, width):
    t = int(t)
    width = float(width)
    reducer = tapkee.DiffusionMaps(t=t, width=width)
    return reducer.fit_transform(X)

def run_tapkee_lltsa(X, n_neighbors):
    n_neighbors = int(n_neighbors)
    reducer = tapkee.LinearLocalTangentSpaceAlignment(n_neighbors=n_neighbors)
    return reducer.fit_transform(X)

def run_tapkee_lmds(X, n_neighbors):
    n_neighbors = int(n_neighbors)
    reducer = tapkee.LandmarkMDS(n_neighbors=n_neighbors)
    return reducer.fit_transform(X)

def run_tapkee_lpp(X, n_neighbors):
    n_neighbors = int(n_neighbors)
    reducer = tapkee.LocalityPreservingProjections(n_neighbors=n_neighbors)
    return reducer.fit_transform(X)

def run_tapkee_spe(X, n_neighbors, n_updates):
    n_neighbors = int(n_neighbors)
    n_updates = int(n_updates)
    reducer = tapkee.StochasticProximityEmbedding(n_neighbors=n_neighbors, n_updates=n_updates)
    return reducer.fit_transform(X)

#drtoolbox
def run_ppca(X):
    reducer = drtoolbox.ProbPCA()
    return reducer.fit_transform(X)

def run_gda(X, kernel):
    reducer = drtoolbox.GDA(kernel=kernel)
    return reducer.fit_transform(X)

def run_mcml(X):
    reducer = drtoolbox.MCML()
    return reducer.fit_transform(X)

def run_llc(X, k, n_analyzers):
    k = int(k)
    n_analyzers = int(n_analyzers)
    reducer = drtoolbox.LLC(k=k, n_analyzers=n_analyzers)
    return reducer.fit_transform(X)

def run_lmnn(X, k):
    k = int(k)
    reducer = drtoolbox.LMNN(k=k)
    return reducer.fit_transform(X)

def run_mc(X, n_analyzers):
    n_analyzers = int(n_analyzers)
    reducer = drtoolbox.ManifoldChart(n_analyzers=n_analyzers)
    return reducer.fit_transform(X)

def run_gplvm(X, sigma):
    sigma = float(sigma)
    reducer = drtoolbox.GPLVM(sigma=sigma)
    return reducer.fit_transform(X)

def run_lmvu(X, k1, k2):
    k1 = int(k1)
    k2 = int(k2)
    reducer = drtoolbox.LandmarkMVU(k1=k1, k2=k2)
    return reducer.fit_transform(X)
