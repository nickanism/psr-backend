from django.urls    import path, include
from .views         import URLSimilarProductView

urlpatterns = [
    path('image', URLSimilarProductView.as_view())
]
