from django.urls    import path, include
from .views         import SimilarProductView

urlpatterns = [
    path('image', SimilarProductView.as_view())
]
