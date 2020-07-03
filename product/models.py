from django.db import models
"""
class Gender(models.Model):
    name                = models.CharField(max_length=45, null=True)

    class Meta:
        db_table        = 'genders'

class MainCategory(models.Model):
    name                = models.CharField(max_length=45, null= True)
    gender              = models.ForeignKey(Gender, on_delete=models.CASCADE,related_name='main_categories')

    class Meta:
        db_table        = 'main_categories'

class Category(models.Model):
    name                = models.CharField(max_length=45, null=True)
    main_category       = models.ForeignKey(MainCategory, on_delete=models.CASCADE, related_name='categories')

    class Meta:
        db_table        = 'categories'

class Clothes(models.Model):
    name                = models.CharField(max_length=100, null=True)
    category            = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='clothes')
    color               = models.CharField(max_length=45, null=True)
    product_pattern     = models.CharField(max_length=45, null=True)
    brand               = models.CharField(max_length=100, null=True)
    product_color       = models.CharField(max_length=45, null=True)
    sleeve_length       = models.CharField(max_length=45, null=True)
    neckline            = models.CharField(max_length=45, null=True)
    sleeve_style        = models.CharField(max_length=45, null=True)
    upper_body_length   = models.CharField(max_length=45, null=True)
    lower_body_length   = models.CharField(max_length=45, null=True)
    price               = models.IntegerField(null=True)
    from_date           = models.DateField(auto_now=False, auto_now_add=False, null=True)
    to_date             = models.DateField(auto_now=False, auto_now_add=False, null=True)

    class Meta:
        db_table        = 'clothes'

class Shoes(models.Model):
    category            = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='shoes')
    name                = models.CharField(max_length=100, null=True)
    shoe_type           = models.CharField(max_length=45, null=True)
    show_decoration     = models.CharField(max_length=45, null=True)
    toe_type            = models.CharField(max_length=45, null=True)
    shoe_closure        = models.CharField(max_length=45, null=True)
    heel_height         = models.CharField(max_length=45, null=True)
    heel_type           = models.CharField(max_length=45, null=True)
    brand               = models.CharField(max_length=100, null=True)
    price               = models.IntegerField(null=True)
    from_date           = models.DateField(auto_now=False, auto_now_add=False, null=True)
    to_date             = models.DateField(auto_now=False, auto_now_add=False, null=True)

    class Meta:
        db_table        = 'shoes'
"""
class ProductList(models.Model):
    img_url             = models.CharField(max_length=200, null=True)
    product_id          = models.CharField(max_length=100, null=True)
    site_id             = models.CharField(max_length=100, null=True)
    cat_key             = models.CharField(max_length=200, null=True)
    product_name        = models.CharField(max_length=200, null=True)
    category1           = models.CharField(max_length=200, null=True)
    category2           = models.CharField(max_length=200, null=True)
    category3           = models.CharField(max_length=200, null=True)
    category4           = models.CharField(max_length=200, null=True)
    p_key               = models.CharField(max_length=200, null=True)
    p_category          = models.CharField(max_length=200, null=True)
    click_url           = models.CharField(max_length=200, null=True)
    click_url_m         = models.CharField(max_length=200, null=True)
    product_price       = models.CharField(max_length=40, null=True)
    price_pc            = models.CharField(max_length=200, null=True)
    price_mobile        = models.CharField(max_length=200, null=True)
    brand               = models.CharField(max_length=200, null=True)
    import_flag         = models.CharField(max_length=200, null=True)
    save_path           = models.CharField(max_length=100, null=True)
    save_name           = models.CharField(max_length=100, null=True)
    status              = models.IntegerField()
    imp_cnt             = models.IntegerField()
    click_cnt           = models.IntegerField()
    cre_tt              = models.DateTimeField(auto_now=False, auto_now_add=False)
    appr_tt             = models.DateTimeField(auto_now=False, auto_now_add=False)
    rej_tt              = models.DateTimeField(auto_now=False, auto_now_add=False)

    class Meta:
        db_table        = 'product_list'
