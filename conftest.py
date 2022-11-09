import os
import pytest
import shutil


@pytest.fixture()
def create_and_delete_resources_directory():

    current_dir = os.path.dirname(os.path.abspath(__file__))
    os.mkdir(current_dir + '/resources')

    yield

    shutil.rmtree(current_dir + '/resources')
