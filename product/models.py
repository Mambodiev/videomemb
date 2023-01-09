from itertools import product
from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
from django.shortcuts import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class Pricing(models.Model):
    name = models.CharField(max_length=100)  # Basic / Pro / Premium

    def __str__(self):
        return self.name


class Subscription(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pricing = models.ForeignKey(Pricing, on_delete=models.CASCADE, related_name='subscriptions')
    created = models.DateTimeField(auto_now_add=True)
    stripe_subscription_id = models.CharField(max_length=50)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.user.email


# class Video(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='videos')
#     vimeo_id = models.CharField(max_length=50)
#     title = models.CharField(max_length=150)
#     slug = models.SlugField(unique=True)
#     description = models.TextField()
#     order = models.IntegerField(default=1)

#     class Meta:
#         ordering = ["order"]    

#     def __str__(self):
#         return self.title

#     def get_absolute_url(self):
#         return reverse("product:video-detail", kwargs={
#             "video_slug": self.slug,
#             "slug": self.product.slug
#         })


class Product(models.Model):
    option_ads = [
        ('faceBook', 'FaceBook'),
        ('instagram', 'Instagram'),
        ('Tiktok', 'Tiktok'),
    ]
    option_ads_type = [
        ('video', 'Video'),
        ('photo', 'Photo'),
        ('both', 'Both'),
    ]

    gender_options = [
        ('male or Female', 'Male or Female'),
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    option_language = [
        ('english', 'English'),
        ('armenian', 'Armenian'),
        ('belarusian', 'Belarusian'),
        ('bengali', 'Bengali'),
        ('bosnia', 'Bosnia'),
        ('bulgarian', 'Bulgarian'),
        ('bumese', 'Bumese'),
        ('catalan', 'Catalan'),
        ('central Kurdish', 'Central Kurdish'),
        ('croatian', 'Croatian'),
        ('czech', 'Czech'),
        ('danish', 'Danish'),
        ('dutch', 'Dutch'),
        ('estonian', 'Estonian'),
        ('finnish', 'Finnish'),
        ('french', 'French'),
        ('georgian', 'Georgian'),
        ('german', 'German'),
        ('gujarati', 'Gujarati'),
        ('haitian', 'Haitian'),
        ('hebrew', 'Hebrew'),
        ('hindi', 'Hindi'),
        ('hungarian', 'Hungarian'),
        ('indonesian', 'Indonesian'),
        ('italian', 'Italian'),
        ('japanese', 'Japanese'),
        ('javanese', 'Javanese'),
        ('kannada', 'Kannada'),
        ('kazakh', 'Kazakh'),
        ('khmer', 'Khmer'),
        ('korean', 'Korean'),
        ('latvian', 'Latvian'),
        ('lithuanian', 'Lithuanian'),
        ('maithili', 'Maithili'),
        ('malay', 'Malay'),
        ('malayalam', 'Malayalam'),
        ('mandarin Chinese', 'Mandarin Chinese'),
        ('marathi', 'Marathi'),
        ('modern Greek', 'Modern Greek'),
        ('nepali', 'Nepali'),
        ('north Azerbaijani', 'North Azerbaijani'),
        ('northern Uzbek', 'Northern Uzbek'),
        ('norwegian bokmål', 'Norwegian bokmål'),
        ('norwegian Nynorsk', 'Norwegian Nynorsk'),
        ('oriya', 'Oriya'),
        ('persian', 'Persian'),
        ('polish', 'Polish'),
        ('portuguese', 'Portuguese'),
        ('romanian', 'Romanian'),
        ('russian', 'Russian'),
        ('Serbian', 'Serbian'),
        ('slovak', 'Slovak'),
        ('slovenian', 'Slovenian'),
        ('somali', 'Somali'),
        ('spanish', 'Spanish'),
        ('sudanese', 'Sudanese'),
        ('swahili', 'Swahili'),
        ('swedish', 'Swedish'),
        ('tagalog', 'Tagalog'),
        ('tajik', 'Tajik'),
        ('tamil', 'Tamil'),
        ('telugu', 'Telugu'),
        ('thai', 'Thai'),
        ('tibetan', 'Tibetan'),
        ('turkish', 'Turkish'),
        ('turkmen', 'Turkmen'),
        ('uighur', 'Uighur'),
        ('ukrainian', 'Ukrainian'),
        ('urdu', 'Urdu'),
        ('vietnamese', 'Vietnamese'),
    ]
    option_button = [
        ('buy now', 'Buy Now'),
        ('shop now', 'Shop Now'),
        ('learn more', 'Learn More'),
        ('sign up', 'Sign Up'),
        ('send message', 'Send Message'),
        ('book now', 'Book Now'),
        ('install now', 'Install Now'),
        ('get directions', 'Get Directions'),
        ('watch more', 'Watch More'),
        ('view', 'View'),
        ('apply now', 'Apply Now'),
        ('like this page', 'Like This Page'),
        ('download', 'Download'),
        ('get offer', 'Get Offer'),
        ('get tickets', 'Get Tickets'),
        ('play game', 'Play Game'),
        ('try it', 'Try It'),
        ('contact us', 'Contact Us'),
        ('send whatsapp message', 'Send Whatsapp Message'),
        ('get quote', 'Get Quote'),
        ('call now', 'Call Now'),
        ('donate now', 'Donate Now'),
        ('buy tickets', 'Buy Tickets'),
        ('listen now', 'Listen Now'),
        ('subscribe', 'Subscribe'),
        ('get show times', 'Get Show Times'),
        ('view event', 'View Event'),
        ('see menu', 'See Menu'),
        ('read', 'Read'),
        ('use app', 'Use App'),
        ('order now', 'Order Now'),
        ('request time', 'Request Time'),
        ('join', 'Join'),
        ('open link', 'Open Link'),
        ('start order', 'Start Order'),
        ('install app', 'Install App'),
        ('get your code', 'Get Your Code'),
        ('see more', 'See More'),
        ('play now', 'Play Now'),
        ('see details', 'See Details'),
        ('open camera', 'Open Camera'),
        ('sell now', 'Sell Now'),
        ('buy', 'Buy'),
        ('about this website', 'About This Website'),
        ('messsage', 'Messsage'),
        ('follow', 'Follow'),
        ('try it', 'Try it'),
        ('like page', 'Like Page'),
        ('donate', 'Donate'),
        ('watch video', 'Watch Video'),
        ('visit website', 'Visit Website'),
        ('register now', 'Register Now'),
        ('email now', 'Email Now'),
        ('use offer', 'Use Offer'),
        ('add to profil', 'Add To Profil'),
        ('turn on', 'Turn On'),
        ('invite friends', 'Invite Friends'),
        ('see more', 'see more'),
        ('visit instagram profile', 'Visit Instagram Profile'),
        ('go live', 'go live'),
        ('add to cart', 'Add To Cart'),
        ('vote now', 'Vote Now'),
        ('intrested', 'Intrested'),
        ('see all events', 'See All Events'),
        ('save', 'Save'),
        ('search', 'Search'),
        ('remind me', 'Remind Me'),
        ('watch yours', 'Watch Yours'),
        ('save offer', 'Save Offer'),
        ('get deal', 'Get Deal'),
        ('get reminded', 'Get Reminded'),
        ('book test drive', 'Book Test Drive'),
        ('call', 'Call'),
    ]
    country_choices = [
        ('united States', 'United States'),
        ('United Kingdom', 'United Kingdom'),
        ('Canada', 'Canada'),
        ('Australia', 'Australia'),
        ('New Zealand', 'New Zealand'),
        ('Sweden', 'Sweden'),
        ('Denmark', 'Denmark'),
        ('Iceland', 'Iceland'),
        ('Norway', 'Norway'),
        ('Finland', 'Finland'),
        ('The Netherlands', 'The Netherlands'),
        ('Ireland', 'Ireland'),
        ('Germany', 'Germany'),
        ('South Korea', 'South Korea'),
        ('Switzerland', 'Switzerland'),
        ('Belgium', 'Belgium'),
        ('Israel', 'Israel'),
        ('Italy', 'Italy'),
        ('France', 'France'),
        ('Spain', 'Spain'),
        ('Portugal', 'Portugal'),
        ('Austria', 'Austria'),
        ('Hungary', 'Hungary'),
        ('Poland', 'Poland'),
        ('Czech Republic', 'Czech Republic'),
        ('UAE', 'UAE'),
        ('South Africa', 'South Africa'),
        ('The Philippines', 'The Philippines'),
        ('Japan', 'Japan'),
        ('Singapore', 'Singapore'),
        ('Argentina', 'Argentina'),
        ('Mexico', 'Mexico'),
    ]
    technology_options = [
        ('shopify', 'Shopify'),
        ('wooCommerce', 'WooCommerce'),
        ('cart functionality', 'Cart Functionality'),
        ('magento', 'magento'),
        ('salesforce commerce cloud', 'Salesforce Commerce Cloud'),
        ('prestashop', 'PrestaShop'),
        ('vtex', 'VTEX'),
        ('bigcommerce', 'Bigcommerce'),
        ('ibm websphere commerce', 'IBM Websphere Commerce'),
        ('sap commerce cloud', 'SAP Commerce Cloud'),
        ('shopware', 'Shopware'),
        ('shoptet', 'Shoptet'),
        ('opencart', 'OpenCart'),
        ('nopcommerce', 'nopcommerce'),
        ('oracle commerce', 'Oracle Commerce'),
        ('intershop', 'Intershop'),
        ('hybris', 'Hybris'),
        ('zen cart', 'Zen Cart'),
        ('oracle commerce cloud', 'Oracle Commerce Cloud'),
        ('lightspeed ecom', 'Lightspeed eCom'),
        ('epages', 'EPages'),
        ('cloudcart', 'CloudCart'),
        ('kajabi', 'Kajabi'),
        ('loja integrada', 'Loja Integrada'),
        ('oxid eshop', 'OXID eShop'),
        ('riskified', 'Riskified'),
        ('x-cart', 'X-Cart'),
        ('commerce server', 'Commerce Server'),
        ('drupal commerce', 'Drupal Commerce'),
        ('oscommerce', 'osCommerce'),
        ('91app', '91App'),
        ('nuvemshop', 'Nuvemshop'),
        ('mycashflow', 'Mycashflow'),
        ('ticimax', 'Ticimax'),
        ('ecwid', 'Ecwid'),
        ('gambio', 'Gambio'),
        ('craft commerce', 'Craft Commerce'),
        ('ideasoft', 'Ideasoft'),
        ('ceres', 'Ceres'),
        ('t-soft', 'T-Soft'),
        ('storeden', 'Storeden'),
        ('vtex integrated store', 'VTEX Integrated Store'),
        ('ccv shop', 'CCV Shop'),
        ('big cartel', 'Big Cartel'),
        ('miva', 'Miva'),
        ('irroba', 'Irroba'),
        ('volusion', 'Volusion'),
        ('yepcomm', 'Yepcomm'),
        ('xtcommerce', 'xtCommerce'),
        ('ec-cube', 'EC-CUBE'),
    ]
   
   
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    aliexpress_price = models.FloatField(default=0, help_text = "Product price from aliexpress")
    slug = models.SlugField(unique=True)
    thumbnail = models.ImageField(upload_to="thumbnails/", default='products/defaut_image_store_light_blue_bag.jpg')
    image_store = models.ImageField(upload_to="image_store/",default='products/defaut_image_store.png',
        blank=True)
    aliexpress_order = models.IntegerField(default=0, help_text = "Amount of aliexpress order generated")
    number_of_store_selling = models.IntegerField(default=0, help_text = "Amount of store selling the product")
    number_of_suppliers_selling= models.IntegerField(default=0, help_text = "Amount of suppliers selling the product")
    aliexpress_total_sale = models.IntegerField(default=0, help_text = "Amount of aliexpress sale generated")
    likes = models.IntegerField(default=0, help_text = "Amount of likes generated")
    comment = models.IntegerField(default=0, help_text = "Amount of comment generated")
    share = models.IntegerField(default=0, help_text = "Amount of share generated")
    shopify_price = models.IntegerField(blank=True, null=True, help_text = "Product price from shopify")
    price_margin = models.IntegerField(blank=True, null=True, help_text = "Profit you get from this product")
    aliexpress_url = models.URLField(blank=True)
    product_vimeo_id = models.CharField(max_length=50, blank=True, null=True,) 
    last_seen = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    countries = models.CharField(max_length=100, choices=country_choices, default='United States')
    ads_type = models.CharField(max_length=250, choices=option_ads_type, default='Video')
    media_type = models.CharField(max_length=250, choices=option_ads, default='video')
    gender = models.CharField(max_length=250, choices=gender_options, default='Male or Female')
    technology = models.CharField(max_length=250, choices=technology_options, default='Shopify')
    language= models.CharField(max_length=250, choices=option_language, default='English')
    button = models.CharField(max_length=250, choices=option_button, default='Buy Now')
    store_name = models.CharField(max_length=500, help_text = "store or ads name",  blank=True, null=True,)
    links_to_ads = models.CharField(blank=True, null=True, max_length=500, help_text = "A link that will take to ads")
    links_to_a_single_store = models.CharField(blank=True, null=True, max_length=500, help_text = "A link that will take to a single the store")
    text_that_comes_with_ads = RichTextUploadingField(blank=True, null=True)
    links_to_others_stores = RichTextUploadingField(blank=True, null=True,help_text = "A link that will take to the store", )
    links_to_others_suppliers = RichTextUploadingField(blank=True, null=True,)
    is_faceBook = models.BooleanField(default=True)
    is_instagram = models.BooleanField(default=False)
    is_tiktok = models.BooleanField(default=False)
    

    def get_absolute_url(self):
        return reverse("product:product-detail", kwargs={"slug": self.slug})
    
    # def get_margin(self):
    #     return "{:.2f}".format(self.price_margin / 100)

    # def get_aliexpres(self):
    #     return "{:.2f}".format(self.aliexpress_price / 100)

    # def get_shopify(self):
    #     return "{:.2f}".format(self.shopify_price / 100)

    @property
    def imageURL(self):
        try:
            url = self.image_store.url
        except:
            url = ''
        print('URL:', url)
        return url

    def __str__(self):
        return f'{self.name} (${self.aliexpress_price})' 
    

class Sale(models.Model):


    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # month_name = models.CharField(max_length=50)
    total_number_of_sale = models.IntegerField(blank=True, null=True, help_text = "")
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time']

    def __str__(self):
        return f' ({self.product.name}), {self.total_number_of_sale}'

        
class Video(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='videos')
    vimeo_id = models.CharField(max_length=50)
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    order = models.IntegerField(default=1)

    class Meta:
        ordering = ["order"]    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("product:video-detail", kwargs={
            "video_slug": self.slug,
            "slug": self.product.slug
        })


def pre_save_product(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)


def pre_save_video(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)


def post_save_user(sender, instance, created, *args, **kwargs):
    if created:
        free_trial_pricing = Pricing.objects.get(name='Free Trial')
        Subscription.objects.create(user=instance, pricing=free_trial_pricing)





# class Country(models.Model):
#     title = models.ForeignKey(Product, on_delete=models.CASCADE)
#     country_number = models.IntegerField(blank=True, null=True, help_text = "ads country_number group range")
#     name = models.CharField(max_length=100, blank=True, null=True, )

#     class Meta:
#         verbose_name_plural = "Countries"

#     def __str__(self):
#         return self.name



class Order(models.Model):

    order_choices = [
        ('Jan', 'Jan'),
        ('Feb', 'Feb'),
        ('Mar', 'Mar'),
        ('Apr', 'Apr'),
        ('May', 'May'),
        ('Jun', 'Jun'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    name = models.CharField(max_length=100, blank=True, null=True, choices=order_choices,)

    def __str__(self):
        return  self.name



class Country(models.Model):
    country_choices = [
        ('United States', 'United States'),
        ('United Kingdom', 'United Kingdom'),
        ('Canada', 'Canada'),
        ('Australia', 'Australia'),
        ('New Zealand', 'New Zealand'),
        ('Sweden', 'Sweden'),
        ('Denmark', 'Denmark'),
        ('Iceland', 'Iceland'),
        ('Norway', 'Norway'),
        ('Finland', 'Finland'),
        ('The Netherlands', 'The Netherlands'),
        ('Ireland', 'Ireland'),
        ('Germany', 'Germany'),
        ('South Korea', 'South Korea'),
        ('Switzerland', 'Switzerland'),
        ('Belgium', 'Belgium'),
        ('Israel', 'Israel'),
        ('Italy', 'Italy'),
        ('France', 'France'),
        ('Spain', 'Spain'),
        ('Portugal', 'Portugal'),
        ('Austria', 'Austria'),
        ('Hungary', 'Hungary'),
        ('Poland', 'Poland'),
        ('Czech Republic', 'Czech Republic'),
        ('UAE', 'UAE'),
        ('South Africa', 'South Africa'),
        ('The Philippines', 'The Philippines'),
        ('Japan', 'Japan'),
        ('Singapore', 'Singapore'),
        ('Argentina', 'Argentina'),
        ('Mexico', 'Mexico'),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    country_number = models.IntegerField(blank=True, null=True, help_text = "ads country number group range")
    name = models.CharField(max_length=100, blank=True, null=True,choices=country_choices, default='United States')

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name



class Gender(models.Model):

    gender_choices = [
        ('Female', 'Female'),
        ('Male', 'Male'),
        ('Unkwon', 'Unknown'),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='genders')
    gender_number = models.IntegerField(blank=True, null=True, help_text = "ads gender number group range")
    name = models.CharField(max_length=100, blank=True, null=True,choices=gender_choices, default='Female' )

    def __str__(self):
        return  self.name



class Age(models.Model):

    age_choices = [
        ('13-17', '13-17'),
        ('18-24', '18-24'),
        ('25-34', '25-34'),
        ('35-44', '35-44'),
        ('45-54', '45-54'),
        ('55-64', '55-64'),
        ('65+', '65+'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    age = models.IntegerField(blank=True, null=True, help_text = "ads age group range")
    name = models.CharField(max_length=100, blank=True, null=True, choices=age_choices, default='25-34')

    def __str__(self):
        return str(self.name) 


class Like(models.Model):

    like_choices = [
        ('Jan', 'Jan'),
        ('Feb', 'Feb'),
        ('Mar', 'Mar'),
        ('Apr', 'Apr'),
        ('May', 'May'),
        ('Jun', 'Jun'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    like = models.IntegerField(blank=True, null=True, help_text = "ads like range")
    name = models.CharField(max_length=100, blank=True, null=True, choices=like_choices, default='Jan')

    def __str__(self):
        return str(self.name)



# class Item(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField(null=True)
#     price = models.FloatField(default=0)

#     def __str__(self):
#         return f'{self.name} (${self.price})'





post_save.connect(post_save_user, sender=User)
pre_save.connect(pre_save_product, sender=Product)
# pre_save.connect(pre_save_video, sender=Video)