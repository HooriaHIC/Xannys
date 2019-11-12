from django.urls import path
from .views import (
    ItemDetailView,
    CheckoutView,
    HomeView,
    FavView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView,
    RequestRefundView,
    shop,
    fav_update,
    men_category_view,
    women_category_view,
    faq,
    about,
    contact,
    success_send,
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('shop/', shop, name='shop'),
    path('success_send/', success_send, name='success_send'),
    path('about/', about, name='about'),
    path('faq/', faq, name='faq'),
    path('contact/', contact, name='contact'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('favorites/', FavView, name='fav'),
    path('favorites/<slug>/', fav_update, name='fav_update'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('boys/', men_category_view, name='men'),
    path('girls/', women_category_view, name='women'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund')
]
