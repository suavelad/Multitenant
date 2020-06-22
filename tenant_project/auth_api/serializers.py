from django.contrib.auth.models import User, Group
from django.http import HttpResponse, JsonResponse
from rest_framework import serializers, status
from django.contrib.auth import get_user_model  # If used custom user model
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from rest_framework.response import Response
from django.db import connection
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib.auth.password_validation import validate_password
from django.core.validators import EmailValidator

UserModel = get_user_model()
my_current_site = '192.241.156.61'


class ChangePasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value


class ChangePassSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """
    user_id = serializers.IntegerField()
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value


class ResetPasswordSerializer(serializers.Serializer):
    """
        Serializer for password reset endpoint.
    """

    email_address = serializers.CharField(required=True)

    def validate_email(self, value):
        EmailValidator(value)
        return value


class SecureIDSerializer(serializers.ModelSerializer):
    """
    Serializer for SecureID Admin Registration.
    """
    class Meta:
        model = UserModel
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'groups')
        read_only_fields = ('id',)
        write_only_fields = ('password',)

    def create(self, validated_data):
        user = UserModel.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']

        )

        user.set_password(validated_data['password'])
        user.groups.set([1])
        user.is_active = False
        user.save()

        current_site = my_current_site
        mail_subject = 'Activate your account.'
        message = render_to_string('acc_active_email.html', {
            'user': user,
            'domain': current_site,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })

        from_email = settings.EMAIL_HOST_USER
        to_list = [user.email, settings.EMAIL_HOST_USER]
        send_mail(mail_subject, message, from_email, to_list, fail_silently=True)
        print("Kindly check your mail")
        return user


class MgtSerializer(serializers.ModelSerializer):
    """
    Serializer for Management Registration.
    """
    class Meta:
        model = UserModel
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'groups')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = UserModel.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']

        )

        user.set_password(validated_data['password'])
        user.groups.set([2])
        user.is_active = False
        user.save()

        current_site = my_current_site
        mail_subject = 'Activate your account.'
        message = render_to_string('acc_active_email.html', {
            'user': user,
            'domain': current_site,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })

        from_email = settings.EMAIL_HOST_USER
        to_list = [user.email, settings.EMAIL_HOST_USER]
        send_mail(mail_subject, message, from_email, to_list, fail_silently=True)
        print("Kindly check your mail")
        return user


class SupervisorSerializer(serializers.ModelSerializer):
    """
    Serializer for Supervisor Registration.
    """
    class Meta:
        model = UserModel
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'groups')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    #  depth = 2

    def create(self, validated_data):
        user = UserModel.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],

        )

        user.set_password(validated_data['password'])
        user.groups.set([3])
        user.is_active = False
        user.save()

        current_site = my_current_site
        mail_subject = 'Activate your account.'
        message = render_to_string('acc_active_email.html', {
            'user': user,
            'domain': current_site,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })

        from_email = settings.EMAIL_HOST_USER
        to_list = [user.email, settings.EMAIL_HOST_USER]
        send_mail(mail_subject, message, from_email, to_list, fail_silently=True)
        print("Kindly check your mail")
        return user


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User Registration.
    """
    class Meta:
        model = UserModel
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'groups')
        write_only_fields = ('password',)
        read_only_fields = ('id',)
        # depth = 2

    def create(self, validated_data):
        user = UserModel.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],

        )

        user.set_password(validated_data['password'])
        user.is_active = False
        user.save()

        current_site = my_current_site
        mail_subject = 'Activate your account.'
        message = render_to_string('acc_active_email.html', {
            'user': user,
            'domain': current_site,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })

        from_email = settings.EMAIL_HOST_USER
        to_list = [user.email, settings.EMAIL_HOST_USER]
        send_mail(mail_subject, message, from_email, to_list, fail_silently=True)
        print("Kindly check your mail")

        return user


class LoginSerializer(serializers.ModelSerializer):
    """
    Serializer for Login
    """
    class Meta:
        model = UserModel
        fields = ('id', 'groups')
#        exclude = ('username', 'password', 'email', 'first_name', 'last_name', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined', 'user_permissions')


class TellerSerializer(serializers.ModelSerializer):
    """
    Serializer for Teller Registration.
    """
    class Meta:
        model = UserModel
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'groups')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = UserModel.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']

        )

        user.set_password(validated_data['password'])
        user.groups.set([4])
        user.is_active = False
        user.save()

        current_site = my_current_site
        mail_subject = 'Activate your account.'
        message = render_to_string('acc_active_email.html', {
            'user': user,
            'domain': current_site,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })

        from_email = settings.EMAIL_HOST_USER
        to_list = [user.email, settings.EMAIL_HOST_USER]
        send_mail(mail_subject, message, from_email, to_list, fail_silently=True)
        print("Kindly check your mail")
        return user


class CustomerSerializer(serializers.ModelSerializer):
    """
    Serializer for Passenger Registration.
    """
    class Meta:
        model = UserModel
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'groups')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = UserModel.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']

        )

        user.set_password(validated_data['password'])
        user.groups.set([5])
        user.is_active = True
        user.save()

        current_site = my_current_site
        mail_subject = 'Activate your account.'
        message = render_to_string('acc_active_email.html', {
            'user': user,
            'domain': current_site,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })

        from_email = settings.EMAIL_HOST_USER
        to_list = [user.email, settings.EMAIL_HOST_USER]
        send_mail(mail_subject, message, from_email, to_list, fail_silently=True)
        print("Kindly check your mail")
        return user




class DeactivateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        exclude = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'groups', 'is_superuser', 'is_staff', 'user_permissions', 'last_login', 'date_joined')

        def update(self, instance, validated_data):
            instance.is_active = validated_data.get('is_active', instance.is_active)

            instance.save()
            return instance
