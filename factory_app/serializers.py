from rest_framework.fields import ListField, IntegerField, SerializerMethodField
from rest_framework.serializers import ModelSerializer, ValidationError
from factory_app.models import TableLeg, Table, Leg, Feet


class FeetSerializer(ModelSerializer):
    class Meta:
        model = Feet
        fields = '__all__'

    def validate(self, data):
        radius = data.get('radius')
        width = data.get('width')
        length = data.get('length')

        if not (radius or width or length):
            raise ValidationError("A foot must have either radius or length and width. Please try again.")

        """ Validations for foot: """
        # If radius is given it should not have length or width.
        if radius and (width or length):
            raise ValidationError("A foot with a radius must not have length or width. Please try again.")

        # If length is given then width must also be given.
        if length and not width:
            raise ValidationError("A foot with a length must also have a width. Please try again.")

        # If width is given then length must also be given.
        if width and not length:
            raise ValidationError("A foot with a width must also have a length. Please try again.")

        return data


class LegSerializer(ModelSerializer):
    class Meta:
        model = Leg
        fields = '__all__'


class TableLegSerializer(ModelSerializer):
    class Meta:
        model = TableLeg
        fields = '__all__'


class TableSerializer(ModelSerializer):
    legs = ListField(child=IntegerField(), allow_null=True, default=[])

    class Meta:
        model = Table
        fields = '__all__'

    def create(self, validated_data):
        legs = validated_data.pop('legs')
        instance = super().create(validated_data)
        for leg in legs:
            TableLeg.objects.create(table=instance, leg_id=leg)
        return instance

    def update(self, instance, validated_data):
        legs = validated_data.pop('legs')
        for leg in legs:
            TableLeg.objects.get_or_create(leg_id=leg, table=instance)

        TableLeg.objects.exclude(leg_id__in=legs).filter(table=instance).delete()

        return instance


class GETTableSerializer(ModelSerializer):
    legs = SerializerMethodField()

    class Meta:
        model = Table
        fields = '__all__'

    def get_legs(self, instance):
        return instance.tables.values_list("leg_id", flat=True)
