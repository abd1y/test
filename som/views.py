from rest_framework.response import Response
from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import AllowAny
from .models import testImage
# Create your views here.
@api_view(["GET"])
@permission_classes([AllowAny])
def test(req):
    text='its work'
    print(text)
    return Response(text)

@api_view(["GET"])
@permission_classes([AllowAny])
def get_images(req):
    image=testImage.objects.all()
    data=[]
    for img in image:
        data.append({
            "id":img.id,
            "title":img.title,
            "image": img.image.url if img.image else None
        })
        return Response({"data":data})