from django.db import models

class Gender(models.Model):
    name                = CharField(max_length=45, null=True)

    class Meta:
        db_table        = 'genders'

class MainCategory(models.Model):
    name                = CharField(max_length=45, null= True)
    gender              = ForeignKey(Gender, on_delete=models.CASCADE,related_name='main_categories')

    class Meta:
        db_table        = 'main_categories'

class Category(models.Model):
    name                = CharField(max_length=45, null=True)
    main_category       = ForeignKey(MainCategory, on_delete=models.CASCADE, related_name='categories')

    class Meta:
        db_table        = 'categories'

class Clothes(models.Model):
    name                = CharField(max_length=100, null=True)
    category            = ForeignKey(Category, on_delete=models.CASCADE, related_name='clothes')
    color               = CharField(max_length=45, null=True)
    product_pattern     = CharField(max_length=45, null=True)
    brand               = CharField(max_length=100, null=True)
    product_color       = CharField(max_length=45, null=True)
    sleeve_length       = CharField(max_length=45, null=True)
    neckline            = CharField(max_length=45, null=True)
    sleeve_style        = CharField(max_length=45, null=True)
    upper_body_length   = CharField(max_length=45, null=True)
    lower_body_length   = CharField(max_length=45, null=True)
    price               = IntegerField(null=True)
    from_date           = DateField(auto_now=False, auto_now_add=False, null=True)
    to_date             = DateField(auto_now=False, auto_now_add=False, null=True)

    class Meta:
        db_table        = 'clothes'

class Shoes(models.Model):
    category            = ForeignKey(Category, on_delete=models.CASCADE, related_name='shoes')
    name                = CharField(max_length=100, null=True)
    shoe_type           = CharField(max_length=45, null=True)
    show_decoration     = CharField(max_length=45, null=True)
    toe_type            = CharField(max_length=45, null=True)
    shoe_closure        = CharField(max_length=45, null=True)
    heel_height         = CharField(max_length=45, null=True)
    heel_type           = CharField(max_length=45, null=True)
    brand               = CharField(max_length=100, null=True)
    price               = IntegerField(null=True)
    from_date           = DateField(auto_now=False, auto_now_add=False, null=True)
    to_date             = DateField(auto_now=False, auto_now_add=False, null=True)

    class Meta:
        db_table        = 'shoes'

class ProductList(models.Model):
    img_url             = CharField(max_length=200, null=True)
    product_id          = CharField(max_length=100, null=True)
    site_id             = CharField(max_length=100, null=True)
    cat_key             = CharField(max_length=200, null=True)
    product_name        = CharField(max_length=200, null=True)
    category1           = CharField(max_length=200, null=True)
    category2           = CharField(max_length=200, null=True)
    category3           = CharField(max_length=200, null=True)
    category4           = CharField(max_length=200, null=True)
    p_key               = CharField(max_length=200, null=True)
    p_category          = CharField(max_length=200, null=True)
    click_url           = CharField(max_length=200, null=True)
    click_url_m         = CharField(max_length=200, null=True)
    product_price       = CharField(max_length=40, null=True)
    price_pc            = CharField(max_length=200, null=True)
    price_mobile        = CharField(max_length=200, null=True)
    brand               = CharField(max_length=200, null=True)
    import_flag         = CharField(max_length=200, null=True)
    save_path           = CharField(max_length=100, null=True)
    save_name           = CharField(max_length=100, null=True)
    status              = IntegerField()
    imp_cnt             = IntegerField()
    click_cnt           = IntegerField()
    cre_tt              = DateTimeField(auto_now=False, auto_now_add=False)
    appr_tt             = DateTimeField(auto_now=False, auto_now_add=False)
    rej_tt              = DateTimeField(auto_now=False, auto_now_add=False)

    class Meta:
        db_table        = 'product_list'
