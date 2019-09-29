from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """ Allow all safe methods and allow himself to edit """
    """ 
        Django identify a user using a Token in HTTP.header
        request.user --> AnonymousUser if he is not logged-in
                    --> vikram1@gmail.com if he is logged in
        request.user.id --> <his id> if logged in
                        --> None if not logged in
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id