from django.conf.urls import url
from objectpack import desktop
from .controller import controller
from .actions import *


def register_urlpatterns():
   return [url(*controller.urlpattern)]


def register_desktop_menu():
   desktop.uificate_the_controller(
       controller,
       menu_root=desktop.MainMenu.SubMenu('Demo')
   )


def register_actions():
    controller.extend_packs([
        UserPack(),
        PermissionPack(),
        CTPack(),
        GroupPack(),
    ])