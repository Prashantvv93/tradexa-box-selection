
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import ShippingBox
from .serializers import ProductSerializer
from .services import recommend_box


@api_view(["POST"])
def recommend_shipping_box(request):
    serializer = ProductSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(
            {"errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    product = serializer.validated_data
    boxes = ShippingBox.objects.all()

    recommended_box = recommend_box(product, boxes)

    if recommended_box is None:
        return Response(
            {"message": "No suitable box found for this product."},
            status=status.HTTP_404_NOT_FOUND,
        )

    return Response({
        "message": "Suitable shipping box found.",
        "box": {
            "name": recommended_box.name,
            "length": recommended_box.length,
            "width": recommended_box.width,
            "height": recommended_box.height,
            "max_weight": recommended_box.max_weight,
            "cost": recommended_box.cost,
        },
    })
