# BS4 Scrape of JavaScript.info topics

This Python and BeautifulSoup4 app scrapes the titles and subtitles from the website JavaScript.info and organizes them to create a learning plan for JavaScript. The results can be copied/pasted into document to create a learning plan for JavaScript.

### How it works

The application reads the website https://javascript.info/ and builds a list of titles and subtitles which are stored in a dictionary. The dictionary contents are then printed in an outline format to screen.

### Installation

To install the repository, please clone this repository and install the requirements:

Using pip:

```bash
pip install -r requirements.txt
```

Once the environment is created, you can activate it using the following command:

```bash
source myvenv/bin/activate
```

Using conda:

```bash
conda env create -f environment.yml
```

The new environment will be named according to the name field in the environment.yml file and can be changed before creating it.

Once the environment is created, you can activate it using the following command:

```bash
conda activate environment_name
```

### Using the app

To use the application, run the app.py file either from the command line or open the file and run it within the code editor of your choice.

```bash
python3 app.py
```
