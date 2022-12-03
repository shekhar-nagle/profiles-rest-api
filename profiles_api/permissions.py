from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user o edit their own permission"""
    def has_object_permission(self, request, view, obj):
        """check user is trying to update their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id==request.user.id
        """if request.method contain GET request it will show all the profiles
        means readable mode.
        if request.method contain editable request like PUT,PATCH,DELETE etc then it will check
        request.user.id === obj.id if both are same it will return true else fale means not allow to
        perform put, PATCH kind of operarion. you will not see the option their."""
