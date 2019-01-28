from django.shortcuts import render, get_object_or_404

from .models import Blogs


# Create your views here.
def blogs_page(request):
    blogss = Blogs.objects
    return render(request, 'blogs.html', {'blogss':blogss})


def blogs_text(request, blogs_id):
        blogs = get_object_or_404(Blogs, pk=blogs_id)
        return render(request, 'blogs_text.html', {'blogs': blogs})


