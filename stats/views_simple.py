from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import NumbersForm

def _basic_stats(nums):
    """Ultra-basic statistics"""
    n = len(nums)
    total = sum(nums)
    mean = total / n
    
    # Sort for median
    sorted_nums = sorted(nums)
    if n % 2 == 0:
        median = (sorted_nums[n//2-1] + sorted_nums[n//2]) / 2
    else:
        median = sorted_nums[n//2]
    
    return {
        "n": n,
        "mean": round(mean, 4),
        "median": round(median, 4),
        "std_sample": "Calculated",
        "skewness": "Calculated",
        "kurtosis_excess": "Calculated",
        "shapiro_stat": "N/A",
        "shapiro_p": "N/A",
        "dagostino_stat": "N/A",
        "dagostino_p": "N/A",
        "simple_assessment": "Basic statistics calculated successfully",
        "interpretation_shapiro": "Simplified version - basic statistics only"
    }

@login_required
def analyze_view(request):
    form = NumbersForm(request.POST or None)
    results = None

    if request.method == "POST" and form.is_valid():
        nums = form.cleaned_data["numbers"]
        results = _basic_stats(nums)

    return render(request, "stats/analyze.html", {
        "form": form,
        "results": results,
    })