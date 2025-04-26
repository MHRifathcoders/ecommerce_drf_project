from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order
from django.core.mail import send_mail

@receiver(post_save, sender=Order)
def notify_vendors_on_order(sender, instance, created, **kwargs):
    if created:
        vendors = set()
        for item in instance.items.all():
            vendors.add(item.product.vendor.user.email)
        for email in vendors:
            send_mail(
                subject='New Order Notification',
                message=f'You have a new order containing your product(s).',
                from_email='no-reply@ecommerce.com',
                recipient_list=[email],
                fail_silently=True
            )
