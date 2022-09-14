# Generated by Django 3.2 on 2022-09-13 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_site_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='site_type',
            new_name='ads_type',
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='button',
            field=models.CharField(choices=[('buy now', 'Buy Now'), ('shop now', 'Shop Now'), ('learn more', 'Learn More'), ('sign up', 'Sign Up'), ('send message', 'Send Message'), ('book now', 'Book Now'), ('install now', 'Install Now'), ('get directions', 'Get Directions'), ('watch more', 'Watch More'), ('view', 'View'), ('apply now', 'Apply Now'), ('like this page', 'Like This Page'), ('download', 'Download'), ('get offer', 'Get Offer'), ('get tickets', 'Get Tickets'), ('play game', 'Play Game'), ('try it', 'Try It'), ('contact us', 'Contact Us'), ('send whatsapp message', 'Send Whatsapp Message'), ('get quote', 'Get Quote'), ('call now', 'Call Now'), ('donate now', 'Donate Now'), ('buy tickets', 'Buy Tickets'), ('listen now', 'Listen Now'), ('subscribe', 'Subscribe'), ('get show times', 'Get Show Times'), ('view event', 'View Event'), ('see menu', 'See Menu'), ('read', 'Read'), ('use app', 'Use App'), ('order now', 'Order Now'), ('request time', 'Request Time'), ('join', 'Join'), ('open link', 'Open Link'), ('start order', 'Start Order'), ('install app', 'Install App'), ('get your code', 'Get Your Code'), ('see more', 'See More'), ('play now', 'Play Now'), ('see details', 'See Details'), ('open camera', 'Open Camera'), ('sell now', 'Sell Now'), ('buy', 'Buy'), ('about this website', 'About This Website'), ('messsage', 'Messsage'), ('follow', 'Follow'), ('try it', 'Try it'), ('like page', 'Like Page'), ('donate', 'Donate'), ('watch video', 'Watch Video'), ('visit website', 'Visit Website'), ('register now', 'Register Now'), ('email now', 'Email Now'), ('use offer', 'Use Offer'), ('add to profil', 'Add To Profil'), ('turn on', 'Turn On'), ('invite friends', 'Invite Friends'), ('see more', 'see more'), ('visit instagram profile', 'Visit Instagram Profile'), ('go live', 'go live'), ('add to cart', 'Add To Cart'), ('vote now', 'Vote Now'), ('intrested', 'Intrested'), ('see all events', 'See All Events'), ('save', 'Save'), ('search', 'Search'), ('remind me', 'Remind Me'), ('watch yours', 'Watch Yours'), ('save offer', 'Save Offer'), ('get deal', 'Get Deal'), ('get reminded', 'Get Reminded'), ('book test drive', 'Book Test Drive'), ('call', 'Call')], max_length=250),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(choices=[('art', 'Art'), ('automobliles & motorcycles', 'Automobliles & Motorcycles'), ('beauty & health', 'Beauty & Health'), ('camping & hiking', 'Camping & Hiking'), ('cellphones & telecommunications', 'Cellphones & Telecommunications'), ('computer & office', 'Computer & Office'), ('consumer electronics', 'Consumer Electronics'), ('festive & party suppliers', 'Festive & Party Suppliers'), ('home & garden', 'Home & Garden'), ('home improvement', 'Home Improvement'), ('jewelry & accessories', 'Jewelry & Accessories'), ('lights & lighting', 'Lights & Lighting'), ('luggage & bags', 'luggage & bags'), ("men's clothing & acccessories", "Men's Clothing & Acccessories"), ('mother & kids', 'Mother & Kids'), ('novelty & special use', 'Novelty & Special Use'), ('office & school supplies', 'Office & School Supplies'), ('pet products', 'Pet Products'), ('phones & telecommunications', 'Phones & Telecommunications'), ('security & protection', 'Security & Protection'), ('shoes', 'Shoes'), ('sports & entertainment', 'Sports & Entertainment'), ('toys & hobbies', 'Toys & Hobbies'), ('watches', 'Watches'), ("women's clothing & accessories", "Women's Clothing & Accessories"), ("women's shoes", "Women's Shoes"), ('general', 'General'), ('gaming', 'Gaming'), ('kitchen', 'Kitchen'), ('sewing', 'Sewing'), ('health', 'Health'), ('gifts', 'Gifts'), ('travel', 'Travel'), ('fishing', 'Fishing'), ('furniture', 'Furniture'), ('christmas', 'Christmas'), ('DIY', 'DIY'), ('baby', 'Baby'), ('wood working', 'Wood Working'), ('power tools', 'Power Tools'), ('hardware tools', 'Hardware Tools')], on_delete=django.db.models.deletion.PROTECT, to='product.category'),
        ),
    ]