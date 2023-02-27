from rest_framework import serializers

from .models import Project, Pledge

from users.serializers import CustomUserSerializer

class PledgeSerializer(serializers.ModelSerializer):
    supporter = serializers.SerializerMethodField()
    class Meta:
        model = Pledge
        fields = '__all__'
        read_only_fields = ['id', 'supporter']

    def get_supporter(self, instance):
        if instance.anonymous:
            return "anonymous"
        else:
            return instance.supporter.username 
            
class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None)
    goal = serializers.IntegerField()
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField()
    closing_date = serializers.DateTimeField()
    owner = serializers.ReadOnlyField(source='owner.id')
    total = serializers.ReadOnlyField()

    def create(self, validated_data):
        return Project.objects.create(**validated_data)

class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)

    bookmarked_by = CustomUserSerializer(many=True, read_only=True)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description',instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open',instance.is_open)
        instance.date_created = validated_data.get('date_created',instance.date_created)
        instance.closing_date = validated_data.get('closing_date',instance.closing_date)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance

