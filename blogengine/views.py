from django.shortcuts import redirect

def redirect_blog(request):
    return redirect('post_lists_url', permanent=True)