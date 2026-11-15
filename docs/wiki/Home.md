**English** · [Dansk](Home-da) · [Bahasa Melayu](Home-ms)

# Hirst Painting

A turtle program that draws a Hirst-style spot painting of 100 coloured dots.

## What is it?

Day 18 of the Udemy course *100 Days of Code: The Complete Python Pro Bootcamp*, the Hirst painting project. The program extracts a palette of colours from a reference image with `colorgram`, removes white shades and faint colours that would hardly show on the white background, and then draws 100 dots of size 20, 50 units apart, in 10 rows of 10. Each dot gets a random colour from the palette. The window stays open until you click it.

## What the exercise teaches

- Using `turtle` to move, lift the pen and draw dots
- Looping over rows and columns to place a grid
- Choosing random items with the `random` module
- Using a third-party library (`colorgram`) to read colours from an image
- Writing automated pytest tests, and running a linter and a strict type checker

## What it does

- A 10 by 10 grid of 100 dots, centred in the window
- A palette extracted from a reference image, without white shades and faint colours (contrast with white below 2.0)
- A random palette colour for each dot
- A fast drawing without animation, and a window that stays open until you click

## Next

- [Getting Started](Getting-Started)
- [Project Documents](Project-Documents)
