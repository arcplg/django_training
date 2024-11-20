from django.http import HttpResponse
import pathlib
from django.shortcuts import render
from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    ps = PageVisit.objects.all()
    page_ps = PageVisit.objects.filter(path = request.path)
    # html_file_path = this_dir / "home.html"
    # html_ = html_file_path.read_text()
    my_content = {
        "page_title": 'My Title',
        "page_visit_count": page_ps.count(),
        "percent": (page_ps.count() * 100.0) / ps.count(),
        "total_visit_count": ps.count()
    }
    html_template = "home.html"
    PageVisit.objects.create(path = request.path)
    return render(request, html_template, my_content)