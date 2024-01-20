from .models import Chapter

def chapters(request):
    return {'chapters': Chapter.objects.all()}
