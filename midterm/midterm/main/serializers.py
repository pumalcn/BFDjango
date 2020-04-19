from midterm.auth_.serializers import UserSerializer
from rest_framework import serializers
from . import models, constants


class BookShortSerializer(serializers.ModelSerializer):
    num_pages = serializers.SerializerMethodField
    genre = serializers.SerializerMethodField

    class Meta:
        model = models.Book
        fields = ('id', 'name', 'price', 'num_pages', 'genre')




class BookSerializer(BookShortSerializer):
    created_at = serializers.DateTimeField(read_only=True)

    class Meta(BookShortSerializer.Meta):
        fields = BookShortSerializer.Meta.fields + ('description', 'created_at',)

    def validate_num_pages(self, value):
        if value < 0:
            raise seri
            alizers.ValidationError('Number of pages must be > than 0')
        return value

class JournalShortSerializer(serializers.ModelSerializer):
    type_name = serializers.SerializerMethodField

    class Meta:
        model = models.Journal
        fields = ('id', 'name', 'price', 'type', 'publisher')

    def get_product_type_name(self, obj):
            return constants.JOURNAL_TYPES[obj.product_type - 1][1]


class JournalSerializer(JournalShortSerializer):
    created_at = serializers.DateTimeField(read_only=True)

    class Meta(JournalShortSerializer.Meta):
        fields = JournalShortSerializer.Meta.fields + ('description', 'created_at')
