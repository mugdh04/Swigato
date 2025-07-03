# Swigato

**Swigato** is a Django-based food delivery web application enhanced with **Bite.AI**, an intelligent food categorization and recommendation engine. This project is designed to simulate the operations of a modern food delivery service, complete with product listings, user authentication, restaurant browsing, and AI-driven personalization.

---

## 🌟 Key Features

### ✅ Core Functionality:

* **User Signup/Login System** (`signupuser.html`, `loginuser.html`)
* **Restaurant Listings** (`restaurant.html`)
* **Product Browsing & Ordering** (`products.html`, `order_online.html`)
* **Admin Interface for Product Management**
* **JSON-Based Product Importing** (`products.json`)
* **Dynamic Navigation Bars** (`navbar.html`, `navbar_bite.html`)

### 🤖 Bite.AI Integration:

* **Smart Categorization of Food Items** (`ai.html`)
* Personalized food suggestions using embedded AI
* Efficient search and filtering system
* Ideal for enhancing customer engagement and decision-making

---

## 🚀 Tech Stack

| Layer            | Technologies               |
| ---------------- | -------------------------- |
| Backend          | Django 4.x                 |
| Frontend         | HTML, Bootstrap            |
| Database         | SQLite3                    |
| AI Integration   | Bite.AI + FAISS embeddings |
| Environment Mgmt | `.env` file (for secrets)  |

---

## 💡 Folder Structure Overview

```
Swigato/
├── project1/               # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── test1/                  # Core app with all logic
│   ├── admin.py
│   ├── views.py
│   ├── models.py
│   ├── templates/
│   │   └── test1/
│   │       ├── home2.html
│   │       ├── restaurant.html
│   │       ├── order_online.html
│   │       ├── ai.html              # Bite.AI UI
│   │       └── ...
│   ├── static/             # CSS/JS/Images
│   └── documents/          # Any uploads or reports
│
├── media/                  # Uploaded images/files
├── products.json           # JSON data for products
├── requirements.txt        # Python dependencies
└── manage.py
```

---

## 🚪 Setup Instructions

```bash
# 1. Clone the repository
$ git clone https://github.com/mugdh04/Swigato.git
$ cd Swigato

# 2. Create a virtual environment
$ python -m venv venv
$ source venv/bin/activate    # On Windows: venv\Scripts\activate

# 3. Install dependencies
$ pip install -r requirements.txt

# 4. Run migrations
$ python manage.py migrate

# 5. Load sample product data (optional)
$ python manage.py loaddata products.json

# 6. Run server
$ python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to view the app.

---

## 🌐 Deployment Tips

* Make sure `.env` is in `.gitignore`
* Use `whitenoise` or `gunicorn` for production
* Store static/media using Amazon S3 or similar services
* Secure your secret keys and database in production

---

## 🌍 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🤝 Contributors

* Mugdh Kumar Sharma
* Twinkle Kaushik
* Team Swigato

---

## 🚀 Future Enhancements

* Integrate Razorpay/Stripe for payments
* Add real-time order tracking
* Expand AI recommendations to include previous history

---

For any queries or collaboration, feel free to connect via GitHub or email.
