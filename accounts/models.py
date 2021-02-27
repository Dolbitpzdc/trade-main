from django.db import models
from django.db.models import signals
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

class buyer_individ(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)

    kind_of_activity = models.CharField(max_length=200)
    VAT_payer = models.CharField(max_length=200)

    count_of_outlets = models.CharField(max_length=200)
    trading_area = models.CharField(max_length=200)

    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)

    delivery = models.CharField(max_length=200)
    deferment_of_payment = models.CharField(max_length=200)

    certificate_of_registration = models.CharField(max_length=200)
    payment_form = models.CharField(max_length=200)

    short_desc = models.CharField(max_length=200)


class buyer_entity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)

    kind_of_activity = models.CharField(max_length=200)
    VAT_payer = models.CharField(max_length=200)

    count_of_outlets = models.CharField(max_length=200)
    trading_area = models.CharField(max_length=200)

    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)

    inn = models.CharField(max_length=200)

    short_desc = models.CharField(max_length=200)


class provider_individ(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)

    kind_of_activity = models.CharField(max_length=200)
    VAT_payer = models.CharField(max_length=200)

    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)

    delivery = models.CharField(max_length=200)
    deferment_of_payment = models.CharField(max_length=200)

    certificate_of_registration = models.CharField(max_length=200)

    min_order = models.CharField(max_length=200)
    warranty = models.CharField(max_length=200)
    availability_of_certificates = models.CharField(max_length=200)

    short_desc = models.CharField(max_length=200)


class provider_entity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)

    kind_of_activity = models.CharField(max_length=200)
    VAT_payer = models.CharField(max_length=200)

    count_of_outlets = models.CharField(max_length=200)
    trading_area = models.CharField(max_length=200)

    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)

    delivery = models.CharField(max_length=200)
    deferment_of_payment = models.CharField(max_length=200)

    certificate_of_registration = models.CharField(max_length=200)
    payment_form = models.CharField(max_length=200)

    min_order = models.CharField(max_length=200)
    warranty = models.CharField(max_length=200)
    availability_of_certificates = models.CharField(max_length=200)

    inn = models.CharField(max_length=200)

    short_desc = models.CharField(max_length=200)



class Complaint(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()

    def __unicode__(self):
        return self.name


class Payment_detail(models.Model):
    document = models.ForeignKey(Complaint, related_name='comments', on_delete=models.DO_NOTHING,)
    text = models.TextField()


class Message_to_user(models.Model):
    message = models.TextField()


def notify_admin(sender, instance, created, **kwargs):
    if created:
       subject = 'New user created'
       message = 'User %s was added' % instance.username
       from_addr = None
       recipient_list = ('biwuxqpolp33.org@gmail.com')
       # send_mail(subject, message, from_addr, recipient_list)

signals.post_save.connect(notify_admin, sender=User)
