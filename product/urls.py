from django.urls    import path, include
from .views         import URLSimilarProductView, FileSimilarProductView, MainProductView

urlpatterns = [
    path('image', URLSimilarProductView.as_view()),
    path('file', FileSimilarProductView.as_view()),
    path('', MainProductView.as_view())
]
