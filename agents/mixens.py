from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect , render
from django.http import HttpResponse


class OrganisiorAndLoginRequireMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_organizer:
            return redirect("landing")
        return super().dispatch(request, *args, **kwargs)
# class SuperUserRequiredMixin(AccessMixin):
#     def dispatch(self, request, *args, **kwargs):
#         print(request.user.is_superuser)
#         if not request.user.is_superuser:
#             return HttpResponse("<h1> 400 bad request </h1>", status=400)
#         return super().dispatch(request, *args, **kwargs)
