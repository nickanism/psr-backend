from django.urls    import path, include
from .views         import URLSimilarProductView, FileSimilarProductView

urlpatterns = [
    path('image', URLSimilarProductView.as_view()),
    path('file', FileSimilarProductView.as_view())
]
