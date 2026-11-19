# weird-wonderverse
Question everything. Explore anything. Believe what resonates. You're safe here to wonder.

## Edit and preview the site

The root `index.html` is generated and checked into Git so the site can be
served directly. Edit its source files and regenerate it with Python 3.
The build uses only Python's standard library.

- `src/index.template.html` contains the entrance, forest, Wondermap, and
  the include markers that determine where the Wonder Bites appear.
- `src/wonder-bites/001-perception.html` contains the article and its
  “Two Ways to See” experiment.
- `src/wonder-bites/002-attention.html` contains the forest attention
  activity and its reveal sections.

From the repository root, run:

```sh
python3 build.py
python3 build.py --check
python3 -m http.server 8000 --bind 127.0.0.1
```

Open port 8000 in your local browser. The check command reports when the
checked-in homepage differs from what the sources produce.

## Add an approved Wonder Bite

1. Create a new fragment in `src/wonder-bites/`, such as `003-topic.html`.
   Use the existing fragments as examples. Give each view a unique
   `id` and `class="page"`. Image paths are relative to the generated
   homepage, such as `assets/example.png`.
2. Add `<!-- include: wonder-bites/003-topic.html -->` to
   `src/index.template.html` where the new view belongs. Add approved
   navigation in the source file that owns the link. The existing
   `go('view-id')` function opens a view by its ID.
3. Rebuild and run `python3 build.py --check`. Preview at desktop and
   mobile widths, test the new route and return path, and retest the
   Wondermap and existing bites. Include the source changes and generated
   `index.html` in the same development commit for review.
