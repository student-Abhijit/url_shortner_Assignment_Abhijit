from django.shortcuts import render, redirect, get_object_or_404
from .models import URL

def home(request):
    if request.method == "POST":
        long_url = request.POST.get("long_url")
        obj, created = URL.objects.get_or_create(long_url=long_url)
        return render(request, "shortener/result.html", {"short_url": request.build_absolute_uri(f"/{obj.short_code}")})
    return render(request, "shortener/home.html")

def redirect_view(request, short_code):
    obj = get_object_or_404(URL, short_code=short_code)
    obj.click_count += 1
    obj.save()
    return redirect(obj.long_url)
