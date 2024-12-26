from django.shortcuts import render

# Create your views here.
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import Video

def get_videos(request):
    page = request.GET.get("page", 1)
    videos = Video.objects.all()
    paginator = Paginator(videos, 10)
    paginated_videos = paginator.get_page(page)

    return JsonResponse({
        "videos": [
            {
                "title": video.title,
                "description": video.description,
                "published_at": video.published_at,
                "thumbnails": video.thumbnails,
            }
            for video in paginated_videos
        ],
        "total_pages": paginator.num_pages,
    })

# def dashboard_view(request):
#     search_query = request.GET.get("search", "")
#     videos = Video.objects.filter(title__icontains=search_query)
#     #videos = Video.objects.all()
#     return render(request, "dashboard.html", {"videos": videos})


from django.shortcuts import render
from .models import Video
from django.db.models import Q

def dashboard_view(request):
    search_query = request.GET.get('search', '')
    sort_by = request.GET.get('sort_by', 'published_at')
    order = request.GET.get('order', 'desc')

    videos = Video.objects.all()

    if search_query:
        videos = videos.filter(
            Q(title__icontains=search_query) | Q(description__icontains=search_query)
        )

    if order == 'desc':
        videos = videos.order_by(f'-{sort_by}')
    else:
        videos = videos.order_by(sort_by)

    return render(request, 'dashboard.html', {'videos': videos, 'search_query': search_query, 'sort_by': sort_by, 'order': order})