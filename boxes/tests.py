from decimal import Decimal

from django.test import TestCase
from rest_framework.test import APIClient

from .models import ShippingBox


class BoxRecommendationTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = "/api/recommend/"

    def create_box(self, name, length, width, height, max_weight, cost):
        return ShippingBox.objects.create(
            name=name,
            length=length,
            width=width,
            height=height,
            max_weight=max_weight,
            cost=cost,
        )

    def test_cheapest_suitable_box_is_selected(self):
        self.create_box("Small", 12, 12, 12, 2, 10)
        self.create_box("Large", 20, 20, 20, 5, 20)

        response = self.client.post(
            self.url,
            {
                "length": 10,
                "width": 10,
                "height": 10,
                "weight": 1,
            },
            format="json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["box"]["name"], "Small")

    def test_product_can_fit_after_rotation(self):
        self.create_box("Rotated Box", 15, 30, 12, 5, 15)

        response = self.client.post(
            self.url,
            {
                "length": 25,
                "width": 15,
                "height": 10,
                "weight": 1,
            },
            format="json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data["box"]["name"],
            "Rotated Box",
        )

    def test_box_is_rejected_when_weight_exceeds_capacity(self):
        self.create_box("Light Box", 30, 30, 30, 2, 10)

        response = self.client.post(
            self.url,
            {
                "length": 10,
                "width": 10,
                "height": 10,
                "weight": 3,
            },
            format="json",
        )

        self.assertEqual(response.status_code, 404)
        self.assertIn("message", response.data)

    def test_no_box_fits_product_dimensions(self):
        self.create_box("Small", 20, 15, 10, 5, 10)

        response = self.client.post(
            self.url,
            {
                "length": 50,
                "width": 35,
                "height": 25,
                "weight": 1,
            },
            format="json",
        )

        self.assertEqual(response.status_code, 404)

    def test_invalid_zero_dimension_is_rejected(self):
        response = self.client.post(
            self.url,
            {
                "length": 0,
                "width": 10,
                "height": 10,
                "weight": 1,
            },
            format="json",
        )

        self.assertEqual(response.status_code, 400)

    
    def test_equal_cost_selects_smaller_volume_box(self):
        self.create_box("Small Volume", 10, 10, 10, 5, 15)
        self.create_box("Large Volume", 12, 10, 10, 5, 15)

        response = self.client.post(
            self.url,
            {
                "length": 8,
                "width": 8,
                "height": 8,
                "weight": 1,
            },
            format="json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data["box"]["name"],
            "Small Volume",
        )
