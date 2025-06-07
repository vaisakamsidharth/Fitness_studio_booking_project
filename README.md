# Fitness_studio_booking_project

A Django REST API for a fictional fitness studio, allowing users to view fitness classes and book sessions. Built with `Django`, `SQLite`, and `Django REST Framework`.

---

#Features

- List available fitness classes
- Book a fitness class if slots are available
- View bookings by client email
- Timezone conversion to IST (Asia/Kolkata)
- Input validation and error handling
- Basic unit tests included

---

##tools used

- Python 3.11+ (3.13.4 compatible)
- Django 5.2.2
- Django REST Framework
- SQLite (default database)
- `pytz` for timezone handling

---

##Project Structure 

fitness_studio_booking/
├── fitness_booking/ # Project settings
├── fitness_booking_api/ # Main API app
│ ├── models.py
│ ├── views.py
│ ├── serializers.py
│ ├── urls.py
│ └── tests.py
├── db.sqlite3
└── manage.py


# Setup Instructions

### 1. Clone the repository
bash
git clone https://github.com/your-username/fitness_studio_booking.git
cd fitness_studio_booking

2. Create and activate a virtual environment

python -m venv venv
venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

4. Migrate the database

python manage.py makemigrations
python manage.py migrate

5. (Optional) Seed sample class data
   
python manage.py shell
from fitness_booking_api.models import FitnessClass
from datetime import datetime
import pytz

ist = pytz.timezone('Asia/Kolkata')
FitnessClass.objects.create(name="Yoga", instructor="Anu", datetime=ist.localize(datetime(2025, 6, 10, 8, 0)), available_slots=10)
FitnessClass.objects.create(name="Zumba", instructor="Rahul", datetime=ist.localize(datetime(2025, 6, 10, 10, 0)), available_slots=5)
exit()

python manage.py runserver
Visit: 

1)http://127.0.0.1:8000/fitness_booking_api/class_record

eg: [
  {
    "id": 1,
    "name": "Yoga",
    "instructor": "Anu",
    "datetime": "2025-06-10T02:30:00Z",
    "available_slots": 10,
    "class_time_ist": "2025-06-10 08:00:00"
  }
]

2)http://127.0.0.1:8000/fitness_booking_api/class_record

{
  "class_id": 1,
  "client_name": "John Doe",
  "client_email": "john@example.com"
}

Response (on success):  { "message": "Booking successful" }
Response (if no slots):  { "message": "No available slots" }

3)http://127.0.0.1:8000/itness_booking_api/booking_record?email=john@example.com

[
  {
    "id": 1,
    "client_name": "John Doe",
    "client_email": "john@example.com",
    "booking_time": "2025-06-07T12:10:00Z",
    "fitness_class": 1
  }
]
