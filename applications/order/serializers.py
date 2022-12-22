from rest_framework import serializers

from applications.order.models import Order
from applications.order.send_mail import send_confirmation_email


class OrderSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(required=False)

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        amount = validated_data['amount']
        product = validated_data['product']
        if amount > product.amount:
            raise serializers.ValidationError('Нет такого количества!')
        if amount == 0:
            raise serializers.ValidationError('Нужно заказать минимум 1 товар')

        product.amount -= amount
        product.save(update_fields=['amount'])

    def create(self, validated_data):
        order = Order.objects.create(**validated_data)
        send_confirmation_email(order.owner.email, order.activation_code, order.product.name, order.total_price)
        return order