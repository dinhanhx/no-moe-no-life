# No moe no life

>This project is based on [Huy-Ngo/skin-crawler](https://github.com/Huy-Ngo/skin-crawler). For backend, I completely implemented my own crawlers. For frontend, I just changed the colors.

`No moe no life` focuses on the cute, wholesome things of the internet.

Made with [Python 3.7](https://www.python.org/) and crawled from [Unsplash](https://unsplash.com/), [Burst](https://burst.shopify.com/).

## How to run

### Backend
Firstly, run `cd backend` at root.

#### Setup

Then, `pip install -r requirements.txt`.
```bash
py unsplash_crawler.py
py burst_crawler.py
```

#### Run

On UNIX systems and GNU/Linux systems, run
```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

On Windows systems, run
```bash
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
```

### Frontend

Open file `frontend/index.html`
