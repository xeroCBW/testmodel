from collections import OrderedDict

from pandas import DataFrame
from rest_framework import status
from rest_pandas import PandasExcelRenderer
from rest_pandas.renderers import RESPONSE_ERROR


class CustomPandasExcelRender(PandasExcelRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):
        if renderer_context and 'response' in renderer_context:
            status_code = renderer_context['response'].status_code
            if not status.is_success(status_code):
                return "Error: %s" % data.get('detail', status_code)


        if isinstance(data,OrderedDict):
            data = data['results']

        if not isinstance(data, DataFrame):
            raise Exception(
                RESPONSE_ERROR % type(data).__name__
            )

        name = getattr(self, 'function', "to_%s" % self.format)
        if not hasattr(data, name):
            raise Exception("Data frame is missing %s property!" % name)

        self.init_output()
        args = self.get_pandas_args(data)
        kwargs = self.get_pandas_kwargs(data, renderer_context)
        self.render_dataframe(data, name, *args, **kwargs)
        return self.get_output()
