# Static Site Generator in Python
This repository is a Static Site Generator project that was developed as part of the Boot.dev static site generator course. The project focuses on building a static site generator from scratch while enhancing my own development skills.

### Features
- **Markdown Parsing:** Convert ```.md``` files into HTML.
- **Template Rendering:** Apply a consistent template across all generated pages.
- **Static Output:** Generates a fully navigable static website.
- **CLI Support:** Easily run and configure the generator from the command line.
- **Error Handling:** Manage invalid files and missing templates gracefully.

### Tech used
- **Python** is the core programming language.
- **Markdown** is used for content parsing.
- **HTML/CSS** is used for output styling and layout of the content.
- **Testing:** Python's ```unittest``` module for comprehensive unit tests.

### What I learned
- Parsing and processing markdown files. (A lot of string manipulation)
- Managing file I/O efficiently in python.
- Writing modular, maintainable, and testable Python code.

### Testing
Unit tests were created to ensure that the generator should function properly:
- Parsing .md to HMTL.
- Handles improper .md and/or invalid files.

Run tests with:
```python3 -m unittest discover -s src```

### Why this project?
Aside from being a part of the boot.dev curriculum, this project provided valuable hands-on experience with:
- Content rendering pipelines
- Building customizable tools for developers
- An understanding of how static site generates like Jekyll or Hugo function at a fundamental level (even though I'm sure their generators are more recursive / better... mines pretty basic)

### Related Resources
- [Boot.dev Course](https://www.boot.dev/courses/build-static-site-generator-python)
- [Official Python Documentation](https://docs.python.org/3/)
- [Markdown Documentation](https://www.markdownguide.org/)
- [Interactive Regex Testing](https://regexr.com/)

Feel free to explore, text, and build upon this project if you'd like!
