from rest_framework import serializers

from Api.models import Product,Category

class ProductSerializers(serializers.ModelSerializer):

    product_object=serializers.StringRelatedField()

    category_object=serializers.StringRelatedField()

    brand_object=serializers.StringRelatedField()

    size_object=serializers.StringRelatedField(read_only=True)

    class Meta:

        

        model=Product

        fields="__all__"

        read_only_fields=["id","created_date","updated_date","is_active"]



class CategorySerializer(serializers.ModelSerializer):

    category_object=serializers.StringRelatedField()

    class Meta:

        

        model=Category

        fields="__all__"

        read_only_fields=["id","created_date","updated_date","is_active"]



