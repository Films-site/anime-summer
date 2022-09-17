from django.db.models import Avg


class RatingCalculation:

    @staticmethod
    def сalculation_average_score(ratings_model):
        average_score = ratings_model.values_list(
            'estimation', flat=True
        ).aggregate(Avg('estimation'))
        return average_score
