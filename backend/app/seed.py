from app.models import Campaign
from app.database import SessionLocal

db = SessionLocal()

campaigns = [
    Campaign(name="Summer Sale", status="Active", clicks=150, cost=45.99, impressions=1000),
    Campaign(name="Black Friday", status="Paused", clicks=320, cost=89.50, impressions=2500),
    Campaign(name="Holiday Promo", status="Active", clicks=220, cost=60.00, impressions=1800),
    Campaign(name="New Year Blast", status="Active", clicks=180, cost=49.99, impressions=1600),
    Campaign(name="Spring Launch", status="Paused", clicks=90, cost=20.25, impressions=800),
    Campaign(name="Autumn Deals", status="Active", clicks=300, cost=75.00, impressions=2300),
    Campaign(name="Clearance Sale", status="Paused", clicks=110, cost=33.50, impressions=900),
    Campaign(name="Flash Friday", status="Active", clicks=260, cost=70.10, impressions=2100),
    Campaign(name="Weekend Promo", status="Paused", clicks=140, cost=40.00, impressions=1000),
    Campaign(name="Back to School", status="Active", clicks=200, cost=55.60, impressions=1500),
]

db.add_all(campaigns)
db.commit()
db.close()
