import pytest

from django import forms

from crispy_forms_foundation.layout import (Layout, InlineField,
                                            InlineSwitchField)

from forms import BasicInputForm, BoolInputForm
from utils import read_output, write_output


def test_inlinefield(output_test_path, rendered_template, helper, client):
    form = BasicInputForm()

    helper.layout = Layout(
        InlineField('simple', label_column='large-7', input_column='large-5', label_class='foobar')
    )

    rendered = rendered_template(form, helper=helper)

    attempted = read_output(output_test_path, "test_inlinefield.html")
    #attempted = ""
    #write_output(output_test_path, "test_inlinefield.html", rendered)

    assert rendered == attempted


def test_inlineswitchfield(output_test_path, rendered_template, helper, client):
    form = BoolInputForm()

    helper.layout = Layout(
        InlineSwitchField('opt_in', label_column='large-8', input_column='large-4', label_class='foobar', switch_class="inline")
    )

    rendered = rendered_template(form, helper=helper)

    attempted = read_output(output_test_path, "test_inlineswitchfield.html")
    #attempted = ""
    #write_output(output_test_path, "test_inlineswitchfield.html", rendered)

    assert rendered == attempted