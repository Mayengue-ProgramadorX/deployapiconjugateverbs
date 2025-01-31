from django.urls import path
from .views import get_conjugations
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions



#configurate swagg
schema_view = get_schema_view(
    openapi.Info(
        title="Conjugation API Documentation",
        default_version="v1",
        description="API to get word conjugation",
        contact=openapi.Contact(email="josemayengue51@gmail.com"),
        license=openapi.License(name="License MIT"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    re_path(r'swagger(?P<format>\.json|\.yaml$)', schema_view.without_ui(cache_tomeout=0), name='schema-json'),
    path("conjugate/", get_conjugations, name="conjugate"),
    
    #route for documentation swagger ui and test or endpoints request(post,get etc..)
    path("swagger/", schema_view.with_ui('swagger', cache_timeout=0), name="schema-swagger-ui"),
    #route for documentation redoc for
    path("redoc/", schema_view.with_ui('redoc', cache_timeout=0), name="schema-redoc"), 
]

