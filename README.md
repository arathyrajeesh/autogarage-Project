# 🔧 Auto Garage Web Management System

A full-featured Django web application for managing an auto garage business.

## Features

| Module | Features |
|--------|----------|
| **Owner** | Dashboard, Reports, Staff Management, Full System Access |
| **Service Advisor** | Customers, Vehicles, Job Cards, Invoices |
| **Mechanic** | View & Update Assigned Jobs |
| **Store Manager** | Spare Parts, Stock In/Out, Suppliers, Categories |

## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Create Owner (Superuser)
```bash
python manage.py createsuperuser
```

### 4. Run the Server
```bash
python manage.py runserver
```

Visit: **http://127.0.0.1:8000/**

---

## System Roles

### Owner
- Created via `createsuperuser`
- Full access to all modules
- Create staff accounts for other roles

### Service Advisor
- Register customers and vehicles
- Create job cards, assign mechanics
- Generate invoices

### Mechanic
- View assigned job cards
- Update job progress and status

### Store Manager
- Manage spare parts inventory
- Record stock in/out transactions
- Manage suppliers and categories

---

## URL Overview

| URL | Description |
|-----|-------------|
| `/login/` | Login page |
| `/owner/` | Owner dashboard |
| `/advisor/` | Advisor dashboard |
| `/mechanic/` | Mechanic dashboard |
| `/store/` | Store manager dashboard |
| `/staff/` | Staff management |
| `/customers/` | Customer management |
| `/vehicles/` | Vehicle management |
| `/jobs/` | Job card management |
| `/parts/` | Spare parts inventory |
| `/invoices/` | Billing & invoices |
| `/reports/` | Business reports |

---

## Tech Stack

- **Backend:** Python 3.10+ / Django 4.2
- **Database:** SQLite (development) — easily swap to PostgreSQL
- **Frontend:** Pure CSS (no framework) — Industrial Dark theme
- **Fonts:** Rajdhani (display) + Source Code Pro (data)
