# The Boys Character Matcher

An interactive cinematic personality quiz inspired by *The Boys* universe that matches users with characters based on physical traits, personality traits, or a combined analysis.

## Features

- Physical / Personality / Combined quiz modes
- Dynamic one-question wizard interface
- Progress tracking
- Cinematic loading analyzer screen
- Character image-based results
- Top 3 character matches
- Trait breakdown analysis
- Archetype classification system
- Responsive UI for desktop and mobile

## Tech Stack

**Backend**
- Python
- Flask

**Frontend**
- HTML
- CSS
- JavaScript
- Jinja2 Templates

## Project Structure

```bash
boys_matcher/
│
├── app.py
├── scorer.py
├── characters.py
├── questions_data.py
├── descriptions.py
├── character_images.py
├── archetypes.py
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   └── images/
