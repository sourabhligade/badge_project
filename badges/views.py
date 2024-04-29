from django.shortcuts import render
from .forms import BadgeUploadForm
from .utils import make_badge, remove_background_with_rembg
from PIL import Image
import io

def upload_badge(request):
    if request.method == 'POST':
        form = BadgeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            badge = request.FILES['badge']
            uploaded_image = Image.open(badge)
            
            with io.BytesIO() as output_bytes:
                uploaded_image.save(output_bytes, format='PNG')
                image_bytes = output_bytes.getvalue()
            
            processed_image = remove_background_with_rembg(image_bytes)
            
            resized_img, validation_result = make_badge(processed_image)

            if validation_result:
                width_after, height_after = resized_img.size
                
                return render(request, 'badges/success.html', {
                    'width_before': uploaded_image.width,
                    'height_before': uploaded_image.height,
                    'width_after': width_after,
                    'height_after': height_after
                })
            else:
                return render(request, 'badges/upload.html', {'form': form, 'error_message': "Badge validation failed"})
    else:
        form = BadgeUploadForm()
    
    return render(request, 'badges/upload.html', {'form': form})
