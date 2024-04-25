from django.shortcuts import render
from PIL import Image  # Import the Image module

# Create your views here.
# badges/views.py
from django.shortcuts import render
from .forms import BadgeUploadForm
from .utils import validate_badge

def upload_badge(request):
    if request.method == 'POST':
        form = BadgeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            badge = request.FILES['badge']
            validation_result, message = validate_badge(Image.open(badge))
            if validation_result:
                # Save the validated badge to a permanent location
                with open('static/validated_badge.png', 'wb+') as destination:
                    for chunk in badge.chunks():
                        destination.write(chunk)
                return render(request, 'success.html')
            else:
                return render(request, '/Users/sourabhligade/badge_project/badges/templates/badges/upload.html', {'form': form, 'error_message': message})
    else:
        form = BadgeUploadForm()
    return render(request, '/Users/sourabhligade/badge_project/badges/templates/badges/upload.html', {'form': form})
