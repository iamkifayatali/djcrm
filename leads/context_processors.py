from .models import Lead
def lead_count(request):
    count=Lead.objects.count()
    return {"lead_count": count }