from .data_application_base import DataApplicationBase


class DataContext:
    def __init__(self, application: DataApplicationBase):
        self.application = application
        return