from django.core.exceptions import ValidationError
from django.test import TestCase
from .models import PaymentInfo

class PaymentInfoModelTests(TestCase):

    def test_swift_code_validator_must_raise_error_unless_code_length_is_8_or_11(self):
        info = PaymentInfo(
            bank_name = 'Woori',
            bank_branch = 'KAIST',
            account_number = '1002-346-661619',
            recipient = '박준우'
        )
        try:
            info.swift_code = '123456789'
            info.clean_fields()
        except ValidationError:
            pass
        else:
            self.fail("Swift Code Validator must raise an error if the code length is not 8 or 11.")

        try:
            info.swift_code = '12345678'
            info.clean_fields()
        except ValidationError:
            self.fail("Swift Code Validator must not raise an error if the code length is 8 or 11.")

