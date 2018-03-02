from django.conf.urls import url
from dj-swagger.views import SwaggerResourcesView, SwaggerApiView, SwaggerUIView


urlpatterns = [
    url(r'^$', SwaggerUIView.as_view(), name="django.swagger.base.view"),
    url(r'^api-docs/$', SwaggerResourcesView.as_view(), name="django.swagger.resources.view"),
    url(r'^api-docs/(?P<path>.*)/?$', SwaggerApiView.as_view(), name='django.swagger.api.view'),
]
