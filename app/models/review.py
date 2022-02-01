class Review:

    all_reviews = []

    @classmethod
    def get_reviews(cls, id):
        response = []

        for review in cls.all_reviews:
            if review.movie_id == id:
                response.append(review)

        return response
