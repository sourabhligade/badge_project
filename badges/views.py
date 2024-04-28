from django.shortcuts import render
from .forms import BadgeUploadForm
from .utils import validate_badge
from PIL import Image

def upload_badge(request):
    if request.method == 'POST':
        form = BadgeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            badge = request.FILES['badge']
            uploaded_image = Image.open(badge)
            width_before, height_before = uploaded_image.size   
            resized_img, validation_result = validate_badge(uploaded_image)
            if validation_result:
                width_after, height_after = resized_img.size
                
                return render(request, 'badges/success.html', {
                    'width_before': width_before,
                    'height_before': height_before,
                    'width_after': width_after,
                    'height_after': height_after
                })
            else:
                return render(request, 'badges/upload.html', {'form': form, 'error_message': "Badge validation failed"})
    else:
        form = BadgeUploadForm()
    
    return render(request, 'badges/upload.html', {'form': form})
