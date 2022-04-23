
# 2019-07-23 Modified by Tran Le Anh

from django.contrib import admin
from django.urls import path
from webcam.views import index, video_feed_1, video_feed_2, camera_1, camera_2
# from webcam.views import database, search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('video_feed_1/', video_feed_1, name="video-feed-1"),
    path('video_feed_2/', video_feed_2, name="video-feed-2"),
    path('index/camera1/', camera_1),
    path('index/camera2/', camera_2),

]
