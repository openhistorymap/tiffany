from django.shortcuts import render

# Create your views here.

import tempfile

def index(request):
	return render(request, "index.html")


def handle_uploaded_file(f):
	d = tempfile.NamedTemporaryFile(suffix=".geotiff", delete=False)
	for chunk in f.chunks():
		d.write(chunk)
	d.close()

	

from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render_to_response('upload.html', {'form': form})


