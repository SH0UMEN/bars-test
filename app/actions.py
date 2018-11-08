from objectpack.actions import ObjectPack
from objectpack.ui import ModelEditWindow
from django.contrib.auth import models
from django.contrib.contenttypes.models import ContentType
from .ui import UserAddAndEditWindow


class UserPack(ObjectPack):
    add_to_desktop = True
    add_to_menu = True
    model = models.User
    add_window = edit_window = UserAddAndEditWindow


class CTPack(ObjectPack):
    add_to_desktop = True
    add_to_menu = True
    model = ContentType
    add_window = edit_window = ModelEditWindow.fabricate(model=ContentType)


class GroupPack(ObjectPack):
    add_to_desktop = True
    add_to_menu = True
    model = models.Group
    add_window = edit_window = ModelEditWindow.fabricate(model=models.Group)


class PermissionPack(ObjectPack):
    add_to_desktop = True
    add_to_menu = True
    model = models.Permission
    add_window = edit_window = ModelEditWindow.fabricate(model=models.Permission)
