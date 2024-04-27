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
            resized_img, validation_result = validate_badge(Image.open(badge))
            message="Badge validation successful"
            if validation_result:
                # Save the validated badge to a permanent location
                resized_img.save('badges/static/resized_image.png')
                return render(request, '/Users/sourabhligade/badge_project/badges/templates/badges/success.html')
            else:
                return render(request, '/Users/sourabhligade/badge_project/badges/templates/badges/upload.html', {'form': form, 'error_message': message})
    else:
        form = BadgeUploadForm()
    return render(request, '/Users/sourabhligade/badge_project/badges/templates/badges/upload.html', {'form': form})