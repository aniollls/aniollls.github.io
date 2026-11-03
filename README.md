# Aniol Llorente-Saguer — personal website

A single-page academic site for GitHub Pages. No build step is needed to publish:
`index.html` is a complete, self-contained page.

## Files to upload to the repository

```
index.html            the page
cv.pdf                your CV (linked from the sidebar)
photo.jpg             optional — see the TODO comment in index.html
papers/
  ballot-richness.pdf                 (included)
  forward-backward-disclosure.pdf     (included)
build/                optional — only needed if you want to regenerate the page (see below)
```

## Publishing on GitHub Pages

1. Create a **public** repository named exactly `<your-username>.github.io`.
2. **Add file → Upload files**, drag everything above in, **Commit changes**.
3. After a minute, open `https://<your-username>.github.io`.

Every later edit is the same: open the file in the repository, click the pencil, edit, commit.

## Editing

The quickest way is to edit `index.html` directly: each paper is an `<article class="paper">`
block; copy one, paste it in the right place, change the text and links.

If you prefer, the `build/` folder keeps the paper list as data:
`build/papers.py` has one entry per paper, `build/abstracts.json` holds the abstracts
(keyed by the paper's `key`), and `python3 build/build.py` regenerates `index.html`.
An "Abstract" button appears automatically on any paper that has an abstract in the JSON.

Search `index.html` (or `build/template.html`) for `TODO` to find the remaining placeholders:
your photo, Google Scholar URL, and the office-hours booking link.
