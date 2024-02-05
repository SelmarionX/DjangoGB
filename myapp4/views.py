from django.shortcuts import redirect

from django.shortcuts import render
from django.contrib import messages

from myapp4.form import ProductPhotoForm


def upload_product_photo(request):
    if request.method == 'POST':
        form = ProductPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ProductPhotoForm()
    return render(request, 'product_photo_upload.html', {'form': form})


def success_view(request):
    messages.success(request, 'Фотография продукта успешно загружена!')
    return render(request, 'success.html')
