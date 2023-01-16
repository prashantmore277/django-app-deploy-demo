from django.db import models

# Create your models here.
class SanctionDetails(models.Model):
    field_name = models.CharField(max_length=200)
    field_value = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    created_by = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_by = models.IntegerField()
    updated_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'sanction_details'


        
class SanctionLetters(models.Model):
    id = models.AutoField(primary_key=True)
    filename = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    created_by = models.CharField(max_length=200)
    scheme_type = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now = True, blank = True) 
    updated_by = models.CharField(max_length=200)
    approved_by = models.CharField(max_length=200)
    updated_date = models.DateTimeField(auto_now = True, blank = True)


    class Meta:
        db_table = 'trn_sanction_letters'

class TrnDetails(models.Model):
    id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=200)
    customer_address = models.CharField(max_length=200)
    customer_email_id = models.CharField(max_length=200)
    customer_num = models.CharField(max_length=200)
    trn_time = models.DateTimeField(auto_now = True, blank = True) 
    product_name = models.CharField(max_length=200)
    product_price = models.IntegerField()
    product_quantity = models.IntegerField()
    product_amount = models.IntegerField()
    additional_details = models.CharField(max_length=200)
    trn_type = models.CharField(max_length=200)

    class Meta:
        db_table = 'trn_details'


# class TermsAndConditions(models.Model):
#     field_name = models.CharField(max_length=200)
#     field_value = models.CharField(max_length=200)

#     class Meta:
#         db_table = 'trn_sanction_fields'


