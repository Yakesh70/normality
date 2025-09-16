
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import NumbersForm
import numpy as np
from scipy import stats
import matplotlib
matplotlib.use('Agg')   # use non-interactive backend for servers
import matplotlib.pyplot as plt
import io, base64

def _arr_stats(arr):
    # arr: numpy array
    n = int(arr.size)
    mean = float(arr.mean())
    median = float(np.median(arr))
    # sample standard deviation
    std_sample = float(arr.std(ddof=1))
    skewness = float(stats.skew(arr, bias=False))
    # fisher=True returns excess kurtosis (0 for normal)
    kurtosis = float(stats.kurtosis(arr, fisher=True, bias=False))
    # Shapiro-Wilk (good for small samples)
    sh_stat, sh_p = stats.shapiro(arr)
    # D'Agostino K^2 normaltest (requires n>=8)
    k2_stat, k2_p = stats.normaltest(arr)

    return {
        "n": n,
        "mean": mean,
        "median": median,
        "std_sample": std_sample,
        "skewness": skewness,
        "kurtosis_excess": kurtosis,
        "shapiro_stat": float(sh_stat),
        "shapiro_p": float(sh_p),
        "dagostino_stat": float(k2_stat),
        "dagostino_p": float(k2_p),
    }

def _fig_to_base64(fig):
    buf = io.BytesIO()
    try:
        fig.tight_layout()
        fig.savefig(buf, format='png', dpi=150, bbox_inches='tight')
        buf.seek(0)
        img_bytes = buf.getvalue()
        return base64.b64encode(img_bytes).decode('ascii')
    finally:
        plt.close(fig)
        buf.close()

@login_required
def analyze_view(request):
    form = NumbersForm(request.POST or None)
    results = None
    hist_img = None
    qq_img = None

    if request.method == "POST" and form.is_valid():
        nums = form.cleaned_data["numbers"]
        arr = np.array(nums)
        results = _arr_stats(arr)

        # Interpretations (alpha = 0.05)
        alpha = 0.05
        results["interpretation_shapiro"] = (
            "No evidence against normality (fail to reject H0)"
            if results["shapiro_p"] > alpha
            else "Evidence of non-normality (reject H0)"
        )
        results["interpretation_dagostino"] = (
            "No evidence against normality (fail to reject H0)"
            if results["dagostino_p"] > alpha
            else "Evidence of non-normality (reject H0)"
        )

        # Histogram
        fig1, ax1 = plt.subplots(figsize=(8, 6))
        ax1.hist(arr, bins='auto', edgecolor='black', alpha=0.7, color='skyblue')
        ax1.set_title("Histogram", fontsize=14, fontweight='bold')
        ax1.set_xlabel("Value", fontsize=12)
        ax1.set_ylabel("Frequency", fontsize=12)
        ax1.grid(True, alpha=0.3)
        hist_img = _fig_to_base64(fig1)

        # Q-Q plot using scipy.stats.probplot
        fig2, ax2 = plt.subplots(figsize=(8, 6))
        stats.probplot(arr, dist="norm", plot=ax2)
        ax2.set_title("Q-Q Plot (Normal Distribution)", fontsize=14, fontweight='bold')
        ax2.grid(True, alpha=0.3)
        qq_img = _fig_to_base64(fig2)

    return render(request, "stats/analyze.html", {
        "form": form,
        "results": results,
        "hist_img": hist_img,
        "qq_img": qq_img,
    })

# Create your views here.
