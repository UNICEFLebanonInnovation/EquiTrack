__author__ = 'jcranwellward'

from rest_framework import serializers

from .models import (
    ResultStructure,
    ResultType,
    Unit,
    Sector,
    Goal,
    Indicator,
    Result
)


class GoalSerializer(serializers.ModelSerializer):

    # TODO: ids are already readonly https://github.com/tomchristie/django-rest-framework/issues/2114#issuecomment-64095219
    goal_id = serializers.CharField(source='id', read_only=True)
    sector_id = serializers.CharField(source='sector.id', read_only=True)

    class Meta:
        model = Goal
        fields = ('goal_id', 'name', 'description', 'sector_id')


class SectorSerializer(serializers.ModelSerializer):

    sector_id = serializers.CharField(source='id', read_only=True)
    goals = GoalSerializer()

    class Meta:
        model = Sector
        fields = ('sector_id', 'name', 'description', 'goals')


class IndicatorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Indicator
        fields = ('id', 'name', 'unit', 'total', 'current', 'sector_total', 'sector_current')


class OutputSerializer(serializers.ModelSerializer):

    class Meta:
        model = Result
        fields = ('id', 'name', 'sector', 'humanitarian_tag')


class SectorCreateSerializer(serializers.ModelSerializer):

    id = serializers.CharField(read_only=True)

    class Meta:
        model = Sector


# class GoalCreateSerializer(serializers.ModelSerializer):
#
#     id = serializers.CharField(read_only=True)
#
#     class Meta:
#         model = Goal


class IndicatorCreateSerializer(serializers.ModelSerializer):

    id = serializers.CharField(read_only=True)

    class Meta:
        model = Indicator


class ResultSerializer(serializers.ModelSerializer):

    id = serializers.CharField(read_only=True)

    class Meta:
        model = Result


class ResultStructureSerializer(serializers.ModelSerializer):

    id = serializers.CharField(read_only=True)

    class Meta:
        model = ResultStructure


class ResultTypeSerializer(serializers.ModelSerializer):

    id = serializers.CharField(read_only=True)

    class Meta:
        model = ResultType


class UnitSerializer(serializers.ModelSerializer):

    id = serializers.CharField(read_only=True)

    class Meta:
        model = Unit
