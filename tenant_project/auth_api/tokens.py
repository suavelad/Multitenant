from django.contrib.auth.tokens import PasswordResetTokenGenerator
# from django.utils import six
import six
from django.utils.crypto import salted_hmac
from django.utils.http import int_to_base36


def _make_token_with_timestamp(self, user, timestamp):
    # timestamp is number of days since 2001-1-1.  Converted to
    # base 36, this gives us a 3 digit string until about 2121
    ts_b36 = int_to_base36(timestamp)

    hash = salted_hmac(
        self.key_salt,
        self._make_hash_value(user, timestamp),
    ).hexdigest()[::2]
    return "%s-%s" % (ts_b36, hash)


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
                six.text_type(user.pk) + six.text_type(timestamp) +
                six.text_type(user.is_active)
        )


account_activation_token = AccountActivationTokenGenerator()


class PasswordTokenGenerator(PasswordResetTokenGenerator):
    def _make_token_with_timestamp(self, user, timestamp):
        return (
                six.text_type(user.pk) + six.text_type(timestamp)
        )


password_token = PasswordTokenGenerator()
