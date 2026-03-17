# JSONPlaceholder API Post Fetcher

A Python script that fetches posts from the [JSONPlaceholder](https://jsonplaceholder.typicode.com/) REST API and saves the results to a local JSON file.

---

## Overview

This project demonstrates how to make an HTTP GET request to a public REST API, process the response data, and persist it locally as a formatted JSON file. It also displays the fetched post titles in the terminal.

---

## ✨ Features

- Fetches 100 posts from the JSONPlaceholder API
- Saves the posts along with a post count to a local `posts.json` file
- Displays all post IDs and titles in the terminal
- Handles request errors gracefully

---

## Requirements

- Python 3.x
- `requests` library

---

## 🛠️ Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Install dependencies:**
   ```bash
   pip install requests
   ```

---

## 🚀 Usage

Run the script with:

```bash
python main.py
```

**Expected terminal output:**

```
Fetched 100 posts from API.
================Posts from API================
======================Title===================
Post ID: 1, Title: sunt aut facere repellat provident occaecati...
Post ID: 2, Title: qui est esse
...
```

---

## 📁 Output

After running the script, a `posts.json` file is created in the project directory with the following structure:

```json
{
  "posts": [
    {
      "userId": 1,
      "id": 1,
      "title": "sunt aut facere...",
      "body": "quia et suscipit..."
    }
  ],
  "number_of_posts": 100
}
```

---

## 🗂️ Project Structure

```
your-repo-name/
│
├── main.py          # Main script
├── posts.json       # Generated output file (created on first run)
└── README.md        # Project documentation
```

---

## 📌 API Reference

| Property | Value                                  |
| -------- | -------------------------------------- |
| Base URL | `https://jsonplaceholder.typicode.com` |
| Endpoint | `/posts`                               |
| Method   | `GET`                                  |
| Response | Array of 100 post objects              |
