with open("README.md", "r") as f:
    readme = f.read()

# I will add the screenshot at the top
screenshot_url = "https://lh3.googleusercontent.com/aida/AOfcidV1agzLwTtpWBpE3F_TPUl-nzUUxPudhXISwNEm9T_OhQWs8mgH-Km-dX_bsPvoOUl6Uc-EoMPKK4cbgyDHLXqkuNlWhQXcWnqodBwaP7AIFZmG_asWM6iVv0jPocgBx6UVDDhHiKxMdNkp8d4Zwxt8PMUddEnam1a1ICObcuFXWF3jo5zkCMOrf4fRfThA1NF66DPDwf0HB4oo6u_ysY5DywVoXz86ougzjcdwyxC2P-bFqI6T8x6J-Cwt"

new_readme = f"""# Celestial Sphere

![Celestial Sphere UI Design]({screenshot_url})

A generative art piece that creates a unique, calming starfield animation on each visit. Built with HTML, CSS, vanilla JavaScript, and designed using Tailwind CSS for a modern, high-quality dark mode landing page.

This project is part of the "Project Green" initiative to create and deploy a small, creative web project daily.

## How It Works

The JavaScript code uses the HTML Canvas API to:
1.  Create a black background representing space.
2.  Generate a number of "stars" with random positions, sizes, and opacities.
3.  Animate the stars, making them twinkle and slowly move to create a parallax effect.
4.  The animation is designed to be seamless and loop indefinitely.

## Running Locally

Simply open the `index.html` file in any modern web browser.

## Live Deployment

The site is deployed and automatically updated on [Render](https://celestial-sphere-stich.onrender.com).
"""

with open("README.md", "w") as f:
    f.write(new_readme)
