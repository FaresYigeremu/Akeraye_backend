# Akeraye - Fullstack Rental-Based Web App

Akeraye is a fullstack web application for rental services, developed using **Next.js**, **React**, **Tailwind CSS**, **Django**, **Django REST Framework**, and containerized using **Docker/Podman Compose**. This project is part of my final year academic requirement.

---

## 🌐 Live Demo

> _will add the link here once deployed, e.g.:_  
> [https://akeraye.vercel.app](https://akeraye.vercel.app)

---

## 📚 Tech Stack

**Frontend:-**
- [Next.js](https://nextjs.org/)
- [React](https://reactjs.org/)
- [Tailwind CSS](https://tailwindcss.com/)

**Backend(This repo covers the backend only):-**
- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [PostgreSQL](https://www.postgresql.org/)

**Other Tools:-**
- [Docker](https://www.docker.com/) / [Podman](https://podman.io/)
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/)
- [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) (for live chat)
- [react-date-range](https://www.npmjs.com/package/react-date-range)
- [Chapa](https://developer.chapa.co/)



## 🚀 Features

- 🔐 **Authentication:-** Email login via Django Allauth
- 📆 **Booking Interface:-** Date range selection using react-date-range
- 🖼️ **Image Upload:-** Upload property images using `fetch`
- 💬 **Real-time Chat:-** Live messaging via WebSockets
- 💳 **Payment Integration:** Secure online payments via Chapa (Ethiopia-based payment gateway)
- 📱 **Responsive Design:-** Tailored UI for mobile and desktop screens
- 🐳 **Containerization:-** Easily deployable using Docker/Podman Compose


## 🧠 What We Learnt

- Fullstack development with React, Django, and REST APIs
- Frontend design with Tailwind CSS and Next.js features
- Image uploads, authentication, and state management
- Setting up WebSocket-based communication
- Deploying a web app using Docker and hosting on Digital Ocean



## 🛠️ Getting Started

### Prerequisites

- Node.js
- Docker or Podman
- PostgreSQL (if running backend locally without containers)

### Running the Frontend

```bash
npm install
npm run dev
```
Visit http://localhost:3000 in your browser.

### Running the Backend
Make sure Docker/Podman is installed, then:

```bash
docker-compose up --build
```
Or with Podman:

```bash
podman-compose up --build
```
This sets up the backend server and database.


## 📁 Project Structure
```bash
/frontend    → Next.js React frontend  
/backend     → Django / Django REST backend  
/docker      → Docker/Podman setup files
```

## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. This is a first iteration of the project as I learn and implement new features. When a feature is complete, it will be merged into the main branch.


## 📄 License
MIT is common for open source.
This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍🎓 Author
Fares Yigeremu

Final Year Student | Electrical & Computer Engineering