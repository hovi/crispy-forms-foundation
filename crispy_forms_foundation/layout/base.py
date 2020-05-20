"""
Basic elements
==============

.. _Foundation: http://github.com/zurb/foundation
.. _Foundation 6 Callout: http://foundation.zurb.com/sites/docs/callout.html

References:
    * `Foundation 6 Callout`_;

"""  # noqa: E501
from crispy_forms import layout as crispy_forms_layout


__all__ = [
    'Layout', 'UneditableField',
    'HTML', 'Div',
    'Callout',
]


class Layout(crispy_forms_layout.Layout):
    pass


class UneditableField(crispy_forms_layout.HTML):
    pass


class HTML(crispy_forms_layout.HTML):
    pass


class Div(crispy_forms_layout.Div):
    """
    It wraps fields inside a ``<div>`` element.

    You can set ``css_id`` for element id and ``css_class`` for a element
    class names.

    Example:

    .. sourcecode:: python

        Div('form_field_1', 'form_field_2', css_id='div-example',
            css_class='divs')
    """
    template = "%s/layout/div.html"


class Callout(crispy_forms_layout.Div):
    """
    Act like ``Div`` but add a ``callout`` class name.

    Example:

    .. sourcecode:: python

        Callout('form_field_1', 'form_field_2', css_id='div-example',
              css_class='divs')
    """
    def __init__(self, field, *args, **kwargs):
        kwargs['css_class'] = kwargs.get('css_class', '')+' callout'
        super(Callout, self).__init__(field, *args, **kwargs)
