from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import NumbersForm
import statistics
import math

def _simple_stats(nums):
    """Calculate basic statistics without NumPy/SciPy"""
    n = len(nums)
    mean = statistics.mean(nums)
    median = statistics.median(nums)
    
    # Sample standard deviation
    if n > 1:
        variance = sum((x - mean) ** 2 for x in nums) / (n - 1)
        std_sample = math.sqrt(variance)
    else:
        std_sample = 0
    
    # Simple skewness approximation
    if std_sample > 0:
        skewness = sum(((x - mean) / std_sample) ** 3 for x in nums) / n
    else:
        skewness = 0
    
    # Simple kurtosis approximation
    if std_sample > 0:
        kurtosis = sum(((x - mean) / std_sample) ** 4 for x in nums) / n - 3
    else:
        kurtosis = 0
    
    return {
        "n": n,
        "mean": round(mean, 4),
        "median": round(median, 4),
        "std_sample": round(std_sample, 4),
        "skewness": round(skewness, 4),
        "kurtosis_excess": round(kurtosis, 4),
        "shapiro_stat": "N/A (requires SciPy)",
        "shapiro_p": "N/A",
        "dagostino_stat": "N/A (requires SciPy)",
        "dagostino_p": "N/A",
    }

@login_required
def analyze_view(request):
    form = NumbersForm(request.POST or None)
    results = None

    if request.method == "POST" and form.is_valid():
        nums = form.cleaned_data["numbers"]
        results = _simple_stats(nums)
        
        # Simple normality interpretation based on skewness and kurtosis
        results["interpretation_shapiro"] = "Statistical tests require SciPy (not available in this deployment)"
        results["interpretation_dagostino"] = "Statistical tests require SciPy (not available in this deployment)"
        
        # Simple normality assessment
        if abs(results["skewness"]) < 0.5 and abs(results["kurtosis_excess"]) < 0.5:
            results["simple_assessment"] = "Data appears roughly normal (low skewness and kurtosis)"
        else:
            results["simple_assessment"] = "Data may not be normal (high skewness or kurtosis)"

    return render(request, "stats/analyze_simple.html", {
        "form": form,
        "results": results,
    })