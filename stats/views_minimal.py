from django.shortcuts import render
from django.http import HttpResponse
from .forms import NumbersForm
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def analyze_view(request):
    """Ultra-minimal view for Vercel"""
    if request.method == "POST":
        form = NumbersForm(request.POST)
        if form.is_valid():
            nums = form.cleaned_data["numbers"]
            n = len(nums)
            mean = sum(nums) / n
            
            html = f"""
            <!DOCTYPE html>
            <html>
            <head><title>Results</title></head>
            <body>
                <h1>Analysis Results</h1>
                <p>Sample Size: {n}</p>
                <p>Mean: {mean:.4f}</p>
                <p>Data: {nums}</p>
                <a href="/">Back</a>
            </body>
            </html>
            """
            return HttpResponse(html)
    else:
        form = NumbersForm()
    
    html = f"""
    <!DOCTYPE html>
    <html>
    <head><title>Normality Testing</title></head>
    <body>
        <h1>Normality Testing Tool</h1>
        <form method="post">
            <input type="hidden" name="csrfmiddlewaretoken" value="{request.META.get('CSRF_COOKIE', '')}">
            <label>Enter 10-15 numbers:</label><br>
            <textarea name="numbers" rows="4" cols="50" required></textarea><br>
            <button type="submit">Analyze</button>
        </form>
    </body>
    </html>
    """
    return HttpResponse(html)