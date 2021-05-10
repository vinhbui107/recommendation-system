from utils.helpers import connect_db


def export_data():
    cur = connect_db()
    if not cur:
        print("Connect Database failed")

    # export user table
    query_user = "SELECT \
                id as user_id, \
                date_part('year', CURRENT_DATE) - date_part('year', birthday) as age, \
                gender as sex, \
                occupation \
            FROM public.user \
            ORDER BY id"

    outputquery = "COPY ({0}) TO STDOUT WITH CSV HEADER".format(query_user)

    with open("model/data/users.csv", "w") as f:
        cur.copy_expert(outputquery, f)

    # export rating table
    query_rating = "SELECT user_id, movie_id, rating FROM rating ORDER BY user_id, movie_id"

    outputquery = "COPY ({0}) TO STDOUT WITH CSV HEADER".format(query_rating)

    with open("model/data/ratings.csv", "w") as f:
        cur.copy_expert(outputquery, f)

    cur.close()
    print("Finish export data :)")
