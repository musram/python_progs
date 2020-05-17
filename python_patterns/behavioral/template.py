"""
An example of the Template pattern in Python
*TL;DR
Defines the skeleton of a base algorithm, deferring definition of exact
steps to subclasses.
*Examples in Python ecosystem:
Django class based views: https://docs.djangoproject.com/en/2.1/topics/class-based-views/
"""

def get_text():
    return "plain-text"


def get_pdf():
    return "pdf"


def get_csv():
    return "csv"


def convert_to_text(data):
    print("[CONVERT]")
    return "{} as text".format(data)


def saver():
    print("[SAVE]")


def template_function(getter, converter=False, to_save=False):
    data = getter()
    print("Got `{}`".format(data))

    if len(data) <= 3 and converter:
        data = converter(data)
    else:
        print("Skip conversion")

    if to_save:
        saver()

    print("`{}` was processed".format(data))

