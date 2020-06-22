
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from django.views.generic.edit import FormView
from django import forms
from django.contrib import messages
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm
from django.contrib.auth.tokens import default_token_generator


from .serializers import DeactivateUserSerializer, SupervisorSerializer, UserSerializer, \
    ChangePasswordSerializer, ResetPasswordSerializer, MgtSerializer, SecureIDSerializer, \
    TellerSerializer, ChangePassSerializer, LoginSerializer,CustomerSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from django.contrib.auth import get_user_model
from django.db import connection
import collections
from django.core.mail import send_mail
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode, int_to_base36
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from rest_framework.permissions import AllowAny

UserModel = get_user_model()


class UsersViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'

    def group_names(self, request, pk=None):
        """
        Returns a list of all the group names that the given
        user belongs to.
        """
        user = self.get_object()
        groups = user.groups.all()
        return Response([group.name for group in groups])


class LoginView(views.APIView):
    permission_classes = (AllowAny,)

    def post(self, request):

        user = authenticate(
            username=request.data.get("username"),
            password=request.data.get("password"))

        if user is None or not user.is_active:
            return Response({
                'status': 'Unauthorized',
                'message': 'Username or password incorrect'
            }, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)
        return Response(LoginSerializer(user).data)


class LogoutView(views.APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        logout(request)
        return Response({}, status=status.HTTP_204_NO_CONTENT)


class CreateUserView(CreateAPIView):

    model = get_user_model()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class CreateSecureIDView(CreateAPIView):

    model = get_user_model()
    serializer_class = SecureIDSerializer
    permission_classes = (AllowAny,)


class CreateSupervisorView(CreateAPIView):

    model = get_user_model()
    serializer_class = SupervisorSerializer
    permission_classes = (AllowAny,)


class CreateCustomerView(CreateAPIView):

    model = get_user_model()
    serializer_class = CustomerSerializer
    permission_classes = (AllowAny,)


class CreateMgtView(CreateAPIView):
    model = get_user_model()
    serializer_class = MgtSerializer
    permission_classes = (AllowAny,)


class CreateTellerView(CreateAPIView):

    model = get_user_model()
    serializer_class = TellerSerializer
    permission_classes = (AllowAny,)


class DeactivateUserView(UpdateAPIView):
    model = UserModel
    serializer_class = DeactivateUserSerializer
    queryset = UserModel.objects.all()
    lookup_field = 'pk'


class UpdatePassword(APIView):
    """
    An endpoint for changing password.
    """
    permission_classes = (permissions.IsAuthenticated, )

    def get_object(self, queryset=None):
        return self.request.user

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            old_password = serializer.data.get("old_password")
            if not self.object.check_password(old_password):
                return Response({"old_password": ["Wrong password."]},
                                status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResetPassword(APIView):
   # serializer_class = ResetPasswordSerializer
    permission_classes = (AllowAny,)

    def get_object(self, queryset=None):
        return self.request

    def post(self,request, domain_override=None,use_https=False, token_generator=default_token_generator, from_email=None, html_email_template_name=None, *args, **kwargs):
        self.object = self.get_object()
        serializer = ResetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email_address = serializer.data.get("email_address")
            active_users = UserModel._default_manager.filter(
                email__iexact=email_address, is_active=True)
            for user in active_users:
                if not user.has_usable_password():
                    continue
                if not domain_override:
                    current_site = '127.0.0.1:8000'
                    site_name = 'Pally'
                    domain = current_site
                else:
                    site_name = domain = domain_override
                subject = 'Reset Your Password'
                message = render_to_string('pasword_reset.html', {
                  #  'email': user.email,
                    'domain': domain,
                    'site_name': site_name,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'user': user,
                    'token': token_generator.make_token(user),
                    'protocol': 'https' if use_https else 'http',
                })
                user.email_user(subject, message)
                from_email = settings.EMAIL_HOST_USER
                to_list = [user.email, settings.EMAIL_HOST_USER]
                # to_list = [email_address]
                send_mail(subject, message, from_email, to_list, fail_silently=True)
                print("Kindly check your mail to reset your password")

            return Response(status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ResetAfterMail(APIView):
    """
    An endpoint for changing password.
    """
   # authentication_classes = (BasicAuthentication,)
    permission_classes = (AllowAny, )

    def get_object(self, queryset=None):

        return self.request.user

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = ChangePassSerializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            user_id = serializer.data.get("user_id")
            user= User.objects.get(id=user_id)
            # username_1 =user.username
            # password_1 = user.password
            # user = authenticate(username=username_1, password=password_1)
            # login(request, user)
            old_password = serializer.data.get("old_password")
            new_password = serializer.data.get("new_password")
            if old_password != new_password:
                return Response({"Password mismatch": ["Password doesnt match."]},
                                status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            user.set_password(serializer.data.get("new_password"))
            user.save()
            logout(request)
            return Response(status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class check_user_id(object):
    def check_uid(user_id):
        try:
            uid = force_text(urlsafe_base64_decode(user_id))
            user = User.objects.get(pk=uid)

            return user
        except User.DoesNotExist:
            return None


class UserDetails(views.APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        user = check_user_id.check_uid(
            user_id=request.data.get("user_id"), )

        if user is None:
            return Response({
                'status': 'No such category',
                'message': 'Category not found'
            }, status=status.HTTP_404_NOT_FOUND)

        else:

            login(request, user)
            return Response(UserSerializer(user).data)

# class check_user_id(object):
#     def check_uid(user_id, token):
#         try:
#             uid = force_text(urlsafe_base64_decode(user_id))
#             user = User.objects.get(pk=uid)
#             password_token.check_token(user, token)
#
#             if user is not None and password_token.check_token(user,token):
#              return user
#             else:
#                 return Response({
#                 'status': 'No such user',
#                 'message': 'Token not found'
#             }, status=status.HTTP_404_NOT_FOUND)
#         except:
#             return None
#
#
# class UserDetails(views.APIView):
#  #   permission_classes = (permissions.IsAuthenticated,)
#     def post(self, request):
#         user = check_user_id.check_uid(
#             user_id=request.data.get("user_id"),
#             token=request.data.get("token")
#         )
#
#         if user is None:
#             return Response({
#                 'status': 'No such user',
#                 'message': 'Token not found'
#             }, status=status.HTTP_404_NOT_FOUND)
#
#         else:
#           #  return Response(total)
#           login(request, user)
#           return Response(UserSerializer(user).data)

class SetPasswordForm(forms.Form):
    """
    A form that lets a user change set their password without entering the old
    password
    """
    error_messages = {
        'password_mismatch': ("The two password fields didn't match."),
        }
    new_password1 = forms.CharField(label=("New password"),
                                    widget=forms.PasswordInput)
    new_password2 = forms.CharField(label=("New password confirmation"),
                                    widget=forms.PasswordInput)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                    )
        return password2

class PasswordResetConfirmView(FormView):
    template_name = "account/test_template.html"
    success_url = '/admin/'
    form_class = SetPasswordForm

    def post(self, request, uidb64=None, token=None, *arg, **kwargs):
        """
        View that checks the hash in a password reset link and presents a
        form for entering a new password.
        """

        form = self.form_class(request.POST)
        assert uidb64 is not None and token is not None  # checked by URLconf
        try:
            uid = urlsafe_base64_decode(uidb64)
            user = UserModel._default_manager.get(pk=uid)
        except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            if form.is_valid():
                new_password= form.cleaned_data['new_password2']
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Password has been reset.')
                return self.form_valid(form)
            else:
                messages.error(request, 'Password reset has not been unsuccessful.')
                return self.form_invalid(form)
        else:
            messages.error(request,'The reset password link is no longer valid.')
            return self.form_invalid(form)