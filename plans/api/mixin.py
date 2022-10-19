import abc

from django.contrib.contenttypes.models import ContentType
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from plans.api.serailizers import PlanSerializer
from plans.models import Plan, PlanItem


class PlanMixin:
    @action(detail=False, url_path='plans')
    def plans(self, request, *args, **kwargs):
        plan = Plan.objects.get(user=request.user)
        return Response(PlanSerializer(plan).data)

    @plans.mapping.post
    def add_item_in_plan(self, request, *args, **kwargs):
        user_plan = Plan.objects.filter(user=request.user)
        content_id = request.data.get('content_id')

        if not user_plan.exists():
            user_plan = Plan.objects.create(user=request.user)
        else:
            user_plan = user_plan[0]

        content_type_model = ContentType.objects.get_for_model(self.queryset.model, for_concrete_model=False)
        item = content_type_model.get_object_for_this_type(id=content_id)
        plan_item = item.plan_items.filter(id=item.id)

        if not plan_item.exists():
            plan_item = PlanItem.objects.create(content_type=content_type_model, object_id=item.id)
        else:
            plan_item = plan_item[0]

        if user_plan.items.filter(id=plan_item.id).exists():
            return Response({'error': 'this item is already in the plans'})

        user_plan.items.add(plan_item)
        return Response(PlanSerializer(user_plan).data)

    @plans.mapping.delete
    def delete_plan_item(self, request, *args, **kwargs):
        user_plan = Plan.objects.get(user=request.user)
        item_plan_id = request.data.get('content_id')
        content_type_model = ContentType.objects.get_for_model(
            self.queryset.model, for_concrete_model=False
        )
        user_item_plan = PlanItem.objects.get(
            content_type=content_type_model, id=item_plan_id
        )
        user_item_plan.delete()
        if not user_plan.items.all().exists():
            user_plan.delete()
        return Response({'deleted': 'ok'}, status=status.HTTP_204_NO_CONTENT)

    @abc.abstractmethod
    def get_queryset(self):
        ...
