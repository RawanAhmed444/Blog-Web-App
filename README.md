# Blog Website

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
 
### Screenshots

* **Homepage:** ![image](https://github.com/user-attachments/assets/8702240a-5bc8-4528-8d75-6f0f1d051edf)
* **Login Page** ![image](https://github.com/user-attachments/assets/d532157b-403f-4448-ba94-2fd13e722bc6)
* **Register Page:** ![image](https://github.com/user-attachments/assets/34653205-f8f6-4572-8911-4f39944ff42e)
* **Blog Post Creation Page:** ![image](https://github.com/user-attachments/assets/c79d03bd-c5c8-458f-8281-849ad73e2fe8)
* **Reset Password Page:** ![image](https://github.com/user-attachments/assets/79e59ef5-72bc-4d36-86d0-004ad1002407)

### Technologies
* ![Python](flaskblog/static/profile_pics/python.png)
* ![Flask](flaskblog/static/profile_pics/flask.png)
* ![SQLAlchemy](flaskblog/static/profile_pics/SQLAlchemy.png)
* ![HTML](flaskblog/static/profile_pics/html.png), ![CSS](flaskblog/static/profile_pics/css.png)

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

* Rawan Shoaib-(rawanshoaib585@gmail.com)-(https://www.linkedin.com/in/rawan-shoaib-a00471242)

### Acknowledgments

* [Flask Tutorials for Corey Schafer](https://youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&si=cDeca5Rm5cnKqxQx)
