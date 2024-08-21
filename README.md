# Blog Web Application

#### Video Demo:  [My Video Demo](https://youtu.be/NysQ3zOpDI0?si=j6e9Uj0EV4PYEImY)
#### Description: This project is a blog web application built using Python and Flask. It allows users to create accounts, manage their profiles, and write blog posts.

### Features

* **User Management:**
  * User registration, login, and logout functionality.
  * Secure password hashing using bcrypt.
  * Profile management, including profile picture updates.
  * Password reset functionality with email verification.
* **Blog Posts:**
  * Create, update, and delete blog posts.
  * Post categorization and pantigation.

### Technologies
* ![Python](python.png)
* ![Flask](flaskblog/static/profile_pics/flask.png)
* ![SQLAlchemy](flaskblog/static/profile_pics/SQLAlchemy.png)
* ![HTML](flaskblog/static/profile_pics/html.png), ![CSS](css.png)
* ![Bootstrap](flaskblog/static/profile_pics/bootstrap.png)
* bcrypt
* Flask-Login
* Flask-WTF
* Flask-Mail

### Installation

**Prerequisites:**
* Python 3.6 or later

**Steps:**

1. **Clone the repository:** (https://github.com/RawanAhmed444/Blog-Web-App.git)
2. **Create a virtual environment:**
   ```bash
   python -m venv venv
3. **Activate the virtual environment:**
   ```bash
   myenv\Scripts\activate  # Windows
   source myenv/bin/activate  # macOS and Linux
4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
5. **Set environment variables:**
   ```bash
   SECRET_KEY=your_strong_random_key
   MAIL_USERNAME = os.environ.get('your_email_usename')
   MAIL_PASSWORD = os.environ.get('your_email_password')
6. **Run The Application:**
   ```bash
   python run.py

### Contributing

**Contributions are welcome!**

If you have a suggestion that would make this better, please fork the repo and create a pull request.
You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

**Steps:**

1. **Fork the repository**
2. **Create your Feature Branch**
   ```bash
   git checkout -b feature/AmazingFeature
3. **Commit your Changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
4. **Push to the Branch**
   ```bash
   git push origin feature/AmazingFeature
5. **Open a Pull Request**

### Contact

* Rawan Shoaib-(rawanwalid978@gmail.com)-(https://www.linkedin.com/in/rawan-shoaib-a00471242)
* Project Link: (https://github.com/RawanAhmed444/Blog-Web-App.git)

### Acknowledgments

* [Flask Tutorials for Corey Schafer](https://youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&si=cDeca5Rm5cnKqxQx)
