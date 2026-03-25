# Train Reservation System

A **console-based Train Reservation System** built using **Python** to demonstrate **Object-Oriented Programming (OOP)** concepts such as classes, objects, methods, attributes, and booking logic.

This project simulates a simple railway ticket booking platform where users can:

- View available trains
- Check train details
- View fare information
- Book tickets
- Track booked and available seats

---

## Features

- Display list of available trains
- View train details such as:
  - Train name
  - Class type
  - Departure time
  - Arrival time
  - Total seats
  - Available seats
- Book one or more seats
- Calculate total fare
- Prevent invalid bookings such as:
  - Booking zero seats
  - Booking more seats than available
  - Booking on unavailable trains

---

## Tech Stack

- **Language:** Python
- **Concepts Used:** Object-Oriented Programming (OOP), Conditional Statements, Loops, Functions, Dictionary Data Structure

---

## OOP Concepts Demonstrated

This project was created primarily to showcase **OOP skills** in Python.

### Class Used
- `Train`

### Object Attributes
Each train object stores:
- `train_name`
- `seats`
- `fare`
- `class_type`
- `departure_time`
- `arrival_time`
- `booked_seats`

### Methods Used
- `book_ticket()` → Books seats and updates seat count
- `get_status()` → Displays train details and seat availability
- `get_fare_info()` → Displays fare information

This project demonstrates how **real-world entities (trains)** can be modeled using **classes and objects**.

---

## Project Structure

```bash
train-reservation-system/
│
├── main.py
└── README.md
