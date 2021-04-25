from helpers import connect_db


def export_daily():
    cur = connect_db()
    if not cur:
        print("Connect Database failed")

    query_rating = "SELECT user_id, movie_id, rating FROM rating ORDER BY user_id, movie_id"

    outputquery = "COPY ({0}) TO STDOUT WITH CSV HEADER".format(query_rating)

    with open("model/data/ratings.csv", "w") as f:
        cur.copy_expert(outputquery, f)


if __name__ == "__main__":
    export_daily()
