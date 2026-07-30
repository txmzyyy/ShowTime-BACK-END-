from app import app
from extensions import db
from models import Movie, Hall, Screening

with app.app_context():
    Screening.query.delete()
    Hall.query.delete()
    Movie.query.delete()

    movie1 = Movie(
        title="Spiderman: Brand new day",
        genre="Adventure/Sci-fi",
        duration=145,
        description="Peter Parker devotes his life to protecting New York City as a full-time Spider-Man. But as the demands on him intensify, the pressure sparks a surprising physical evolution that threatens his existence, even as a strange new pattern of crimes gives rise to one of the most powerful threats he's ever faced.",
        poster_url="https://example.com/spiderman.jpg"
    )
    movie2 = Movie(
        title="The Odyssey",
        genre="Action/Fantasy",
        duration=173,
        description="Odysseus, king of Ithaca, embarks on a perilous journey to return home after the Trojan War. Crossing the Mediterranean Sea with his fellow soldiers, they soon find themselves battling not only the elements, but an array of deadly obstacles and mythical creatures along the way.",
        poster_url="https://example.com/odyssey.jpg"
    )

    hall1 = Hall(
        hall_name="Hall 1",
        screen_type="3D"
    )

    db.session.add_all([movie1, movie2, hall1])
    db.session.commit()

    screening1 = Screening(
        movie_id=movie1.id,
        hall_id=hall1.id,
        date="2026-08-01",
        time="18:00",
        available_seats=50
    )

    screening2 = Screening(
        movie_id=movie2.id,
        hall_id=hall1.id,
        date="2026-08-01",
        time="21:00",
        available_seats=40
    )

    db.session.add_all([screening1, screening2])
    db.session.commit()

    print("Database has been seeded successfully!")