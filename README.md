# pokerbot

## Resources

Josiah is currently going through [this tutorial](https://dev.to/koladev/building-a-fullstack-application-with-django-django-rest-nextjs-3e26) setting up [Django](https://www.djangoproject.com/) and [Next.js](https://nextjs.org/).

## Get Started

These instructions assume you are on a Windows computer.

#### Backend

1. Ensure `python 3.11` or later is installed.
2. `cd backend-api` and run the following commands.

```bash
python -m venv venv
./venv/Scripts/activate
```

3. Install Django and the other necessary packages from the same wd.

```bash
python -m pip install django djangorestframework
python -m pip install django-cors-headers
# @Justin-Zwart put your other pip-installs here :)
```

If your VS Code isn't detecting your installs, follow [these instructions](https://stackoverflow.com/questions/66869413/visual-studio-code-does-not-detect-virtual-environments).

### Frontend

1. Ensure node.js is installed.
2. `cd frontend` and run the following commands.

```bash
npm i
```

3. You should be good to go!

## Usage

To run the Next.js development server:

```bash
cd frontend
npm run dev
```

To build and run the production Next.js server:

```bash
cd frontend
npm run build
npm run start
```
