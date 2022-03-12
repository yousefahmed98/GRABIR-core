from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import redirect
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


class StripeCheckoutView(APIView):
    def post(self, request):
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                        'price': 'price_1KcVRbBi4CtX5YUJolsLUZ4r',
                        'quantity': 1,
                    },
                ],
                payment_method_types=[
                    'card',
                ],
                mode='payment',
                success_url="http://localhost:3000/PaymentTest" + '?success=true&session_id={CHECKOUT_SESSION_ID}',
                cancel_url="http://localhost:3000/PaymentTest" + '?canceled=true',
            )
            return redirect(checkout_session.url)
        except:
            return  Response(
                {'error':'somthing went wrong creating stripe checkout session'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        
