import abc

from rest_framework import status
from rest_framework.response import Response


class PaginatedElasticSearchAPIView:
    serializer_class = None
    document_class = None

    @abc.abstractmethod
    def generate_q_expression(self, query):
        """This method should be overridden
        and return a Q() expression."""

    def list(self, request, *args, **kwargs):
        if (search_param := request.query_params.get('search')) is not None:
            q = self.generate_q_expression(search_param)
            search = self.document_class.search().query(q)
            response = search.execute()
        else:
            response = self.get_queryset()

        serializer = self.get_serializer_class()(response, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
