from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()

class Category(db.Model):
    __tablename__ = 'pages_category'
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    products = db.relationship('Product', backref='category', lazy=True)

class Product(db.Model):
    __tablename__ = 'pages_product'
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    image = db.Column(db.String(100), nullable=True)
    category_id = db.Column(db.BigInteger, db.ForeignKey('pages_category.id'), nullable=False)

    @property
    def image_url(self):
        if self.image:
            # Берем только имя файла из поля image, игнорируем products/
            filename = self.image.split('/')[-1]
            return f'/static/images/site_images/{filename}'
        return '/static/images/site_images/no-image.jpg'
            
class Lead(db.Model):
    __tablename__ = 'pages_lead'
    id = db.Column(db.BigInteger, primary_key=True)
    full_name = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(254), nullable=True)
    comment = db.Column(db.Text, nullable=True)
    product_name = db.Column(db.String(255), nullable=True)
    product_id = db.Column(db.BigInteger, nullable=True)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)