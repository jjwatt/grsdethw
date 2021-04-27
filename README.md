# grsdethw
Automation samples with Python selenium and the Page Object Model

## grsdethw package

The "Page Objects" for the Page Object model are all implemented in the `grsdethw` Python library. Tests that actually drive the web testing are in `tests`

Here, `grsdethw` stands for "** SDET HomeWork," but a little discreet.

### cars

Since it's for `cars.com` the `cars` module represents the main entrypoint for
the web pages. It contains a `Home` class that represents the home page or
initial (or landing) page for the website.

The `cars` module contains the primary `Page` objects, which for now is just
`Home` but will later contain the `SearchResults` page, too.

Additionally, `cars` holds some specific element modules. This is a bit of a
judgement call. These could have gone in `elements` or it might have been
better to put them directly into `Home`, but they may be shared by other `cars`
pages. I doubt they'd be shared by other websites, though, and that's why
they're in the `cars` module and not the main package. I.e., they live with the
`cars.com` website and its objects.

#### Home

`Home` inherits from a `BasePage` class to keep things POMy. As I add other
pages, they would inherit from this class as well.

`Home` provides the nice API for the website, so `get_home_page` and
`click_search_button` does what you'd expect without you having to build other
objects or specify arguments. In my understanding, this is part of what "POM"
is all about.

#### Home class members

I followed the examples from [selenium python](https://selenium-python.readthedocs.io/page-objects.html)
here and declared "static" class members for the element types. So, `Home` automatically can access its, e.g., `make_element` member. These are instantiated at class load time and so will always be those object types. There's a class for each element type in `cars` and they are `*PageElement` types from the `grsdethw.element` module. They have locators on them that are declared in `grsdethw.locators`.

This all means that you should be able to do things like:

```python
from grsdethw import cars

driver = somewebdriver()
home = cars.Home(driver)
home.get_home_page()
home.make_element = "Honda"
home.model_element = "Pilot"
home.stock_type_element = "Used Cars"
home.zip_code_element = "60008"
```

### element

I deviated from the examples I found a bit on `element` because I wanted some
different elements to work differently but use the same fundamental API, which
I think is the intent, but the example code didn't work for selectors, for
example, and it needlessly limited you to `find_element_by_name` which I didn't
like. I want to be able to use the best locator for the job, so I found the
Python selenium method `find_element` which seems to dispatch based on locator
type. Perfect!

For now, the `SelectorPageElement` type always uses `select_by_visible_text` on
the `Select` object because that seemed to work for everything in the
assignment, and because that makes the cleanest top-level API like the sample
above.

### locators

Locators might vary over time, so they get their own simple module. These are
used to build the `element` types. They're not in `cars` because it could be
that they apply to other web sites, too, right? And, I like that they're pretty
easily importable without all the trappings of the other POM components from a
Python repl for testing and experimentation.

## Usage

I started writing this on Linux using `poetry`. I used `pipenv` a lot before, and I wanted to try it out. It's not required, though. In fact, I switched to working a little bit with Windows and VS Code while I was on a Windows laptop to make sure it worked well. It does.

Do this on Linux:

```shell
poetry install
poetry shell
pytest tests
```

Do this on Windows or on Linux if you don't want to use `poetry`:

```shell
python -m venv .venv
```

Then activate your venv.

On Windows:
- Start a powershell or in VSCode `C-S-P` (command pallette) and say "python
teminal" and start a term

```shell
.venv/bin/Activate.ps1
```
- You may need to fix the PS execution policy for your session with
```shell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```
- You can look up how to open it up all the time

On Linux, do:

```shell
.venv/bin/activate
```

Once you're in your venv, run these commands to install and run.

```shell
pip install -r requirements-dev.txt
pip install .
pytest tests
```

### Web Driver

I did initial development with the remote Firefox web driver from WSL Linux to my Windows host (once I got it working). But, when I was on Linux, I got the Firefox headless version to work, too. That's what I'd be using for CI if/when I set it up. My latest develpment today (20210427) has been on Windows with the plain old Firefox web driver. I started coding up some pytest options to select the driver, and the POM is laid out in a way that you're not limited to a certain driver! However, for now I still have `Firefox` hard-coded in the `pytest` fixture in `tests/test_home.py`. You should be able to just change it there if you want to use a different one.

## Contributing

Submit a pull request. Please run code through `black` and `isort` before submitting. They're installed if you install the dev requirements.

## Notes

I'm almost completely new to selenium, but I'm an old test head and an old
Python head. I wouldn't necessarily do everything this way, but Python lets us
do POM sort of like Java but in a more Pythonic (pleasant) way. I'd probably do
this in a more functional style eventually, but I'm following the
assignment and this was easier since I'm learning about selenium and POM. 

I had really hoped to finish the CI/CD because part of the assignment was to
demonstrate who I am as an engineer, and to me that's one of my biggest assets.
Perhaps I should have started with that, but I wanted to show that I could code
in a requested style, too.

## TODO

- [ ] Finish asserts for assignment
- [ ] Finish pytest option to run headless
- [ ] Flesh out a `ci` target in `Makefile` for headless runs
- [ ] Setup CI with GitHub Actions
- [ ] Setup CD with GitHub Actions