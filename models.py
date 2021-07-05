# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AccountsCustomer(models.Model):
    user = models.ForeignKey('AccountsUser', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'accounts_customer'


class AccountsFarmer(models.Model):
    user = models.ForeignKey('AccountsUser', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'accounts_farmer'


class AccountsGuestemail(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    email = models.CharField(max_length=254)
    active = models.BooleanField()
    update = models.DateTimeField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'accounts_guestemail'


class AccountsUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    email = models.CharField(unique=True, max_length=255)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField()
    staff = models.BooleanField()
    timestamp = models.DateTimeField()
    admin = models.BooleanField()
    is_customer = models.BooleanField()
    is_farmer = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'accounts_user'


class AddressesAddress(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    address_type = models.CharField(max_length=120)
    address_line_1 = models.CharField(max_length=120)
    address_line_2 = models.CharField(max_length=120, blank=True, null=True)
    city = models.CharField(max_length=120)
    country = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    postal_code = models.CharField(max_length=120)
    billing_profile = models.ForeignKey('BillingBillingprofile', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'addresses_address'


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    username = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BillingBillingprofile(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    email = models.CharField(max_length=254)
    active = models.BooleanField()
    update = models.DateTimeField()
    timestamp = models.DateTimeField()
    user = models.ForeignKey(AccountsUser, models.DO_NOTHING, unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'billing_billingprofile'


class CartsCart(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    subtotal = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    total = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    updated = models.DateTimeField()
    timestamp = models.DateTimeField()
    user = models.ForeignKey(AccountsUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'carts_cart'


class CartsCartProducts(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    cart = models.ForeignKey(CartsCart, models.DO_NOTHING)
    product = models.ForeignKey('ProductsProduct', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'carts_cart_products'
        unique_together = (('cart', 'product'),)


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class OrdersOrder(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    order_id = models.CharField(max_length=120)
    shipping_total = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    total = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cart = models.ForeignKey(CartsCart, models.DO_NOTHING)
    active = models.BooleanField()
    billing_address = models.ForeignKey(AddressesAddress, models.DO_NOTHING, blank=True, null=True)
    billing_profile = models.ForeignKey(BillingBillingprofile, models.DO_NOTHING, blank=True, null=True)
    shipping_address = models.ForeignKey(AddressesAddress, models.DO_NOTHING, blank=True, null=True)
    status = models.CharField(max_length=120)

    class Meta:
        managed = False
        db_table = 'orders_order'


class Predict(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    date = models.TextField(blank=True, null=True)  # This field type is a guess.
    quantity = models.TextField(blank=True, null=True)  # This field type is a guess.
    item_no = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'predict'


class Predicted(models.Model):
    date = models.TextField(blank=True, null=True)  # This field type is a guess.
    quantity = models.TextField(blank=True, null=True)  # This field type is a guess.
    item_no = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'predicted'


class ProductsProduct(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    image = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField()
    slug = models.CharField(unique=True, max_length=50)
    availability = models.BooleanField()
    price_unit = models.CharField(max_length=120)
    added_by = models.ForeignKey(AccountsUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'products_product'
